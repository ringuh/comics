# -*- coding: utf-8 -*-
from project import db, app, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib2, os, requests, hashlib
from project.models import Strippi

class Sarjis(object):
	
	def __init__(self, sarjakuva ):
		self.sarjakuva = sarjakuva
		self.sessio = db.session
	
	def Init(self, url=None, ):
		self.urli = url
		if url is None:
			self.urli = sarjakuva.last_url			
		
		r = requests.get(self.urli, headers=app.config["REQUEST_HEADER"] )
		self.soup = BeautifulSoup(r.text)
		print u"\nFinding url", url 

	def Loop(self, url=None, sessio=db.session):
		self.sessio = sessio
		self.Init(url)
		
		
		try: # haetaan kuvat, yhdellä sivulla voi olla useita strippejä
			kuvat = self.Kuvat()
			if len(kuvat) == 0:
				return self.Next()
		except Exception, e:
			Log(self.sarjakuva.id, self.urli, u"Kuvan haku epäonnistui", e)
			return self.Next()
		
		for kuva in kuvat:
			try:
				if self.sarjakuva.download:
					self.Save(kuva["nimi"], kuva["src"], kuva["filetype"])
				else:
					self.Iframe(kuva["nimi"], kuva["src"], kuva["filetype"])

			except Exception, e:
				Log(self.sarjakuva.id, self.urli, u"Kuvan tallennus epäonnistui", e, kuva["src"])
	
		return self.Next() # jos None looppi loppuu
	

	def Kuvat(self):
		print "SARJIS KUVA"
		return dict(nimi=None, src=None, filetype=None)

	def Next(self):
		print "SARJIS NEXT"
		return None



	def Save(self, nimi, url, filetype):
		
		#print "save", nimi
		# katsotaan oliko kyseisestä sarjasta jo kyseinen kuva
		#url = url"
		
		tmp_file = u""
		headers = app.config["REQUEST_HEADER"]
		req = urllib2.Request(url, None, headers)
		try:
			tmp_file = urllib2.urlopen(req).read()
			
		except Exception, e:
			try:
				tmp_file = urllib2.urlopen(url).read()
				
			except Exception, e:
				Log(self.sarjakuva.id, self.urli, u"Kuvan lataus epäonnistui", e, url)
				return False
		
		if len(tmp_file) < 10:
			Log(self.sarjakuva.id, self.urli, u"Liian pieni kuva", None, url)
			return False

		md5 = u"{}".format(hashlib.md5(tmp_file).hexdigest())

		found = self.sessio.query(Strippi).filter(
				Strippi.sarjakuva_id == self.sarjakuva.id,
				Strippi.md5 == md5
			).first()

			
		if found:
			return False
		
		md5_name = u"{}_{}.{}".format(self.sarjakuva.lyhenne, md5, filetype)

		polku = os.path.join(app.config["SARJAKUVA_FOLDER"], self.sarjakuva.lyhenne)
		polku = os.path.join(polku, md5_name)

		# luodaan kansio if needed
		dir = os.path.dirname(polku) 
		try:
			os.stat(dir)
		except:
			os.mkdir(dir)

		f = open(polku,'wb')
		f.write(tmp_file)
		f.close()

		# lisätään kantaan tieto, että kuva on haettu
		order = self.sessio.query(Strippi).filter(Strippi.sarjakuva_id==self.sarjakuva.id).count()+1
		
		tmp = Strippi(self.sarjakuva.id, self.urli, md5_name, nimi, url, md5, order)
		self.sessio.add(tmp)

		# löydettiin kuva, tallennetaan vikaksi urliksi
		self.sarjakuva.last_url = self.urli
		self.sarjakuva.last_parse = datetime.datetime.now()
		self.sessio.commit()

		Log(self.sarjakuva.id, self.urli, u"Tallennetaan kuva", None, url, self.sessio)

		return True
	def Iframe(self, nimi, url, filetype): # ei oikeasti ladata kovolle, näytetään vain
		# lisätään kantaan tieto, että kuva on haettu
		md5 = u"{}".format(hashlib.md5(url).hexdigest())

		found = self.sessio.query(Strippi).filter(
					Strippi.sarjakuva_id == self.sarjakuva.id,
					Strippi.md5 == md5
				).first()

		if found:
			return False

		md5_name = u"{}_{}.{}".format(self.sarjakuva.lyhenne, md5, filetype)
		order = self.sessio.query(Strippi).filter(
					Strippi.sarjakuva_id==self.sarjakuva.id).count()+1
		
		tmp = Strippi(self.sarjakuva.id, self.urli, md5_name, nimi, url, md5, order)
		self.sessio.add(tmp)

		# löydettiin kuva, tallennetaan vikaksi urliksi
		self.sarjakuva.last_url = self.urli
		self.sarjakuva.last_parse = datetime.datetime.now()
		self.sessio.commit()

		Log(self.sarjakuva.id, self.urli, u"Tallennetaan linkki", None, url, self.sessio)

		return True