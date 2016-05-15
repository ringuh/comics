# -*- coding: utf-8 -*-
from project import db, app, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.error, urllib.parse, os, requests, hashlib
from project.models import Strippi

class Sarjis(object):
	
	def __init__(self, sarjakuva ):
		self.sarjakuva = sarjakuva
		self.sessio = db.session
	
	def Init(self, url=None, ):
		self.urli = url
		if url is None:
			self.urli = self.sarjakuva.last_url			
		

		#fo = open("foo.html", "wb")
		

		
		print(("\nFinding url", self.urli)) 
		r = requests.get(self.urli, headers=app.config["REQUEST_HEADER"] )
		self.soup = BeautifulSoup(r.text, 'html.parser')

		#fo.write(str(self.soup));
		#fo.close()

		

	def Loop(self, url=None, sessio=db.session):
		self.sessio = sessio
		self.Init(url)
		
		
		try: # haetaan kuvat, yhdellä sivulla voi olla useita strippejä
			kuvat = self.Kuvat()
			
			if len(kuvat) == 0:
				return self.Next()
		except Exception as e:
			Log(self.sarjakuva.id, self.urli, "Kuvan haku epäonnistui", e)
			raise e
		
		for kuva in kuvat:
			try:
				if self.sarjakuva.download:
					self.Save(kuva["nimi"], kuva["src"], kuva["filetype"])
				else:
					self.Iframe(kuva["nimi"], kuva["src"], kuva["filetype"])

			except Exception as e:
				Log(self.sarjakuva.id, self.urli, "Kuvan tallennus epäonnistui", e, kuva["src"])
	
		return self.Next() # jos None looppi loppuu
	

	def Ehdot(self, soup, lauseke):
		
		print(("ehdot", lauseke))
		ret = []
		if lauseke[0] == "#":
			tmp = soup.find(id=lauseke[1:])
			if tmp:
				ret = [tmp]
		elif lauseke[0] == "!":
			print(soup)
			attr, type, value = lauseke[1:].split(":")
			print(("!!", attr, type, value))
			get = soup.get(attr)
			if get:
				get = str(get)
				print(("vrt", get.lower().strip(), value))
				if type == "=":
					if get.lower().strip() == value:
						ret = [soup]
				elif type == "in":
					if value in get.lower().strip():
						ret = [soup]
			
		elif "." in lauseke:
			a, b = lauseke.split(".")
			ret =  soup.find_all(a, { "class": b })
					
		else:
			ret = soup.find_all(lauseke)

		return ret

	def Find(self, soup, lauseke, ehdot=[]):
		# # id
		# . luokka
		# | ehto
		# : indexi
		# ! get-attribuutti 
		print(("lause", lauseke, ehdot))
		
		#ehto = ehdot[0]
		#ehdot.pop(0)
		arr = self.Ehdot(soup, lauseke)
		print(arr)
		ret = []
		for i in arr:
			ok = True
			keitto = [i]
			for ehto in ehdot:
				print(ehto)
				for j in keitto:
					
					keitto = self.Ehdot(j, ehto)
					print((ehto, len(keitto)))
					if len(keitto) == 0:
						ok = False
			if ok:
				ret.append(i)

		
		print(("find palauttaa", ret))
		return ret

	def Level(self, soup, lvl):
		print(("in level", lvl))
		level = lvl[0]
		tmp_lvl = [i for i in lvl]
		tmp_lvl.pop(0)
		
		ehdot = level.split("|")
		lauseke = ehdot[0] # rivin alkupää, esim #div
		ehdot = ehdot[1:] # rivin loppupää |#comic

		soups = []
		soups = self.Find(soup, lauseke, ehdot)
		print("------")
		
		if len(tmp_lvl) > 0:
			ret = []
			for s in soups:
				for i in self.Level(s, tmp_lvl):
					ret.append(i)
			return ret
		return soups


	# article > figure > img
	def ELEMENT(self, soup, lauseke):
		ret = []

		# pilkotaan lauseke tasoihin > perusteella
		tasot = lauseke.split(">")
		print(tasot)
		# lähdetään ylimmästä tasosta liikenteeseen. esim "nav">img
		ret = self.Level(soup, tasot)

		return ret

	def Kuvat(self):
		kuvat = []
		#return kuvat
		if self.sarjakuva.tags is None:
			return []

		#filters = self.sarjakuva.tags.split(",")

		#for filt in filters:
		soup = self.ELEMENT(self.soup, self.sarjakuva.tags)
		for image in soup:
			print(image)
			kuva = dict(nimi=None, src=None, filetype=self.sarjakuva.filetype)
			try:
				try:
					image["src"] = "{}".format(image["src"].replace("_250.", "_1280."))
					image["src"] = "{}".format(image["src"].replace("_500.", "_1280."))
					#image["src"] = image["src"].split("?")[0]
					if image["src"].index("//") == 0:
						image["src"] = "http:{}".format(image["src"])
				except: pass
				try:
					if image["src"][0] in [".", "#"]:
						image["src"] = image["src"][1:]
				except: pass
				
				if "://" in image["src"]:
					kuva["src"] = image["src"]
				else:
					if self.sarjakuva.url[-1] == "/" and image["src"][0] == "/":
						kuva["src"] = "{}{}".format(self.sarjakuva.url[:-1], image["src"])
					elif self.sarjakuva.url[-1] != "/" and image["src"][0] != "/":
						kuva["src"] = "{}/{}".format(self.sarjakuva.url[:-1], image["src"])
					else:
						kuva["src"] = "{}{}".format(self.sarjakuva.url, image["src"])
				
				kuva["nimi"] = "{}".format(image["src"].split("?")[0].split("/")[-1]) # kuvan nimi = tiedoston nimi
				
				if "." in kuva["nimi"]:
					kuva["filetype"] = "{}".format(image["src"].split("?")[0].split(".")[-1])
				

				kuvat.append(kuva)
			except Exception as e:
				print(e)

				#id, element, luokka, tbc = (None,)*4
			



		return kuvat

	def Next(self):
		ret = self.urli
		if self.sarjakuva.next_tags is None:
			return None
		try:
			soup = self.ELEMENT(self.soup, self.sarjakuva.next_tags)
			print(("next", soup))
			for link in soup:
				print(link)
				try:
					#link["href"] = link["href"].split("?")[0]
					if link["href"].index("//") == 0:
						link["href"] = "http:{}".format(link["href"])
				except: pass
				try:
					if link["href"][0] in [".", "#"]:
						link["href"] = link["href"][1:]
				except: pass
				
				if "://" in link["href"]:
					ret = link["href"]
				else:
					if self.sarjakuva.url[-1] == "/" and link["href"][0] == "/":
						ret = "{}{}".format(self.sarjakuva.url[:-1], link["href"])
					elif self.sarjakuva.url[-1] != "/" and link["href"][0] != "/":
						ret = "{}/{}".format(self.sarjakuva.url[:-1], link["href"])
					else:
						ret = "{}{}".format(self.sarjakuva.url, link["href"])
				break
		except Exception as e: 
			print(e)
			pass
		print(("return", ret))
		
		
		if ret == self.urli:
			return None
		
		return ret



	def Save(self, nimi, url, filetype, urli=None):
		if urli is None: urli = self.urli
		
		loaded = self.sessio.query(Strippi.url).filter(
				Strippi.sarjakuva_id==self.sarjakuva.id
			).all()
		loaded = [i.url for i in loaded]

		if url in loaded:
			return True
		
		print(("save", url))
		# katsotaan oliko kyseisestä sarjasta jo kyseinen kuva
		#url = url"
		tmp_file = ""
		if not "base64" in url:
			headers = app.config["REQUEST_HEADER"]
			req = urllib.request.Request(url, None, headers)
			try:
				tmp_file = urllib.request.urlopen(req).read()
				
			except Exception as e:
				try:
					tmp_file = urllib.request.urlopen(url).read()
					
				except Exception as e:
					Log(self.sarjakuva.id, urli, "Kuvan lataus epäonnistui", e, url)
					return False
			
			if len(tmp_file) < 10:
				Log(self.sarjakuva.id, urli, "Liian pieni kuva", None, url)
				return False
		else:
			order = self.sessio.query(Strippi).filter(Strippi.sarjakuva_id==self.sarjakuva.id).count()+1
			nimi = "{}_{}".format(self.sarjakuva.nimi, order)
			filetype = "jpeg"
			url = url.split(",", 2)[-1]
			tmp_file = url.decode('base64')



		md5 = "{}".format(hashlib.md5(tmp_file).hexdigest())

		found = self.sessio.query(Strippi).filter(
				Strippi.sarjakuva_id == self.sarjakuva.id,
				Strippi.md5 == md5
			).first()

			
		if found:
			return True
		
		order = self.sessio.query(Strippi).filter(Strippi.sarjakuva_id==self.sarjakuva.id).count()+1
		md5_name = "{}_{}.{}".format(self.sarjakuva.lyhenne, order, filetype)

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
		
		tmp = Strippi(self.sarjakuva.id, urli, md5_name, nimi, url, md5, order)
		self.sessio.add(tmp)

		# löydettiin kuva, tallennetaan vikaksi urliksi
		self.sarjakuva.last_url = urli
		self.sarjakuva.last_parse = datetime.datetime.now()
		self.sessio.commit()

		Log(self.sarjakuva.id, urli, "Tallennetaan kuva", None, url, self.sessio)

		return True
	def Iframe(self, nimi, url, filetype, urli=None): 
		if urli is None: urli = self.urli
		# ei oikeasti ladata kovolle, näytetään vain
		# lisätään kantaan tieto, että kuva on haettu
		md5 = "{}".format(hashlib.md5(url).hexdigest())

		found = self.sessio.query(Strippi).filter(
					Strippi.sarjakuva_id == self.sarjakuva.id,
					Strippi.md5 == md5
				).first()

		if found:
			return False

		md5_name = "{}_{}.{}".format(self.sarjakuva.lyhenne, md5, filetype)
		order = self.sessio.query(Strippi).filter(
					Strippi.sarjakuva_id==self.sarjakuva.id).count()+1
		
		tmp = Strippi(self.sarjakuva.id, urli, md5_name, nimi, url, md5, order)
		self.sessio.add(tmp)

		# löydettiin kuva, tallennetaan vikaksi urliksi
		self.sarjakuva.last_url = urli
		self.sarjakuva.last_parse = datetime.datetime.now()
		self.sessio.commit()

		Log(self.sarjakuva.id, urli, "Tallennetaan linkki", None, url, self.sessio)

		return True