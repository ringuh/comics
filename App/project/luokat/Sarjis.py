# -*- coding: utf-8 -*-
from project import db, app, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.error, urllib.parse, os, requests, hashlib, imagehash
from project.models import Strippi
from PIL import Image


class Sarjis(object):
	
	def __init__(self, sarjakuva ):
		self.sarjakuva = sarjakuva
		self.sessio = db.session


	def Print(self, *args):
		import unicodedata
		f = open("logit/loki{}.tmp".format(self.sarjakuva.id), "a")
		text = None;
		for i in args:
			i = unicodedata.normalize('NFKD', str(i)).encode('ASCII', 'ignore').decode("ascii")
			if text:
				text = "{}, {}".format(text, i)
			else:
				text = i;
		text = "{}\n".format(text)
		f.write(text)
		f.close()

	
	def Init(self, url=None, ):
		self.urli = url
		if url is None:
			self.urli = self.sarjakuva.last_url			
		

		#fo = open("foo.html", "wb")
		

		
		self.Print("Finding url", self.urli)
		print("\nFinding url", self.urli)
		r = requests.get(self.urli, headers=app.config["REQUEST_HEADER"] )
		
		self.soup = BeautifulSoup(r.text, 'html.parser')
		self.Print(self.soup)
		self.Print("\n\n")
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
			self.Print(self.sarjakuva.id, self.urli, "Kuvan haku epäonnistui", e)
			raise e
		
		for kuva in kuvat:
			try:
				if self.sarjakuva.download:
					self.Save(kuva["nimi"], kuva["src"], kuva["filetype"])
				else:
					self.Iframe(kuva["nimi"], kuva["src"], kuva["filetype"])

			except Exception as e:
				Log(self.sarjakuva.id, self.urli, "Kuvan tallennus epäonnistui", e, kuva["src"])
				self.Print(self.sarjakuva.id, self.urli, "Kuvan tallennus epäonnistui", e, kuva["src"])
	
		return self.Next() # jos None looppi loppuu
	

	def Ehdot(self, soup, lauseke):
		
		self.Print("EHDOT", lauseke)
		ret = []
		if lauseke[0] == "#":
			tmp = soup.find(id=lauseke[1:])
			if tmp:
				ret = [tmp]
		elif lauseke[0] == "!":
			attr, type, value = lauseke[1:].split(":")
			
			get = soup.get(attr)
			self.Print(get)
			
			if get:
				get = str(get)
				if type == "=" and get.lower().strip() == value:
					ret = [soup]
				elif type == "in" and value in get.lower().strip():
					ret = [soup]

			if attr == "text":
				if type == "=" and value == soup.text.lower():
					ret = [soup]
				elif type == "in" and value in soup.text.lower():
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
		self.Print("FIND", lauseke, ehdot)
		
		#ehto = ehdot[0]
		#ehdot.pop(0)
		arr = self.Ehdot(soup, lauseke)
		
		ret = []
		for i in arr:
			ok = True
			keitto = [i]
			for ehto in ehdot:
				
				for j in keitto:
					
					keitto = self.Ehdot(j, ehto)
					
					if len(keitto) == 0:
						ok = False
			if ok:
				ret.append(i)

		
		self.Print("find palauttaa", ret)
		return ret

	def Level(self, soup, lvl):
		self.Print("LEVEL", lvl)
		level = lvl[0]
		tmp_lvl = [i for i in lvl]
		tmp_lvl.pop(0)
		
		ehdot = level.split("|")
		lauseke = ehdot[0] # rivin alkupää, esim #div
		ehdot = ehdot[1:] # rivin loppupää |#comic

		soups = []
		soups = self.Find(soup, lauseke, ehdot)
		self.Print("------")
		
		if len(tmp_lvl) > 0:
			ret = []
			for s in soups:
				for i in self.Level(s, tmp_lvl):
					ret.append(i)
			return ret
		return soups


	# article > figure > img
	def ELEMENT(self, soup, lauseke):
		self.Print("ELEMENT")
		ret = []

		# pilkotaan lauseke tasoihin > perusteella
		tasot = lauseke.split(">")
		self.Print(tasot)
		# lähdetään ylimmästä tasosta liikenteeseen. esim "nav">img
		ret = self.Level(soup, tasot)

		return ret

	def Kuvat(self):
		self.Print("KUVAT")
		kuvat = []
		#return kuvat
		if self.sarjakuva.image is None:
			return []

		#filters = self.sarjakuva.tags.split(",")

		#for filt in filters:
		soup = self.ELEMENT(self.soup, self.sarjakuva.image)
		for image in soup:
			self.Print("IMAGE", image)
			kuva = dict(nimi=None, src=None, filetype=self.sarjakuva.filetype)
			try:
				try:
					image["src"] = image["src"].strip()
					image["src"] = "{}".format(image["src"].replace("_250.", "_1280."))
					image["src"] = "{}".format(image["src"].replace("_500.", "_1280."))
					image["src"] = image["src"].replace(" ", "%20")
					image["src"] = image["src"].replace("\n", "")
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
						kuva["src"] = "{}/{}".format(self.sarjakuva.url, image["src"])
					else:
						kuva["src"] = "{}{}".format(self.sarjakuva.url, image["src"])
				
				# poistetaan "/comics/../comics/"
				ksplit = kuva["src"].split("/")
				if ".." in ksplit:
					#print( kuva["src"],ksplit)
					indx = ksplit.index("..")
					if indx > 0:
						del ksplit[indx-1]
						del ksplit[indx-1]
				kuva["src"] = "/".join(ksplit)

				kuva["src"] = kuva["src"].replace("/./", "/")

				kuva["nimi"] = "{}".format(image["src"].split("?")[0].split("/")[-1]) # kuvan nimi = tiedoston nimi
				
				if "." in kuva["nimi"]:
					kuva["filetype"] = "{}".format(image["src"].split("?")[0].split(".")[-1])
				
				kuva["src"] = urllib.parse.urlsplit(kuva["src"])
				kuva["src"] = kuva["src"].geturl()
				kuvat.append(kuva)
			except Exception as e:
				self.Print("KUVAT ERROR", e)
				print(e)

				#id, element, luokka, tbc = (None,)*4
			



		return kuvat

	def Next(self):
		ret = self.urli
		if self.sarjakuva.next is None:
			return None
		try:
			self.Print("NEXT")
			soup = self.ELEMENT(self.soup, self.sarjakuva.next)
			self.Print("next", soup)
			for link in soup:
				self.Print(link)
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
			self.Print("NEXT ERROR", str(e))
			print(str(e))
			pass
		
		self.Print("NEXT RET", ret)
		
		
		if ret == self.urli:
			return None
		
		return ret



	def Save(self, nimi, url, filetype, urli=None):
		if urli is None: urli = self.urli
		

		self.Print("SAVE", nimi, url, filetype)

		loaded = self.sessio.query(Strippi.url).filter(
				Strippi.sarjakuva_id==self.sarjakuva.id
			).all()
		loaded = [i.url for i in loaded]

		# if url in loaded:
		# 	return True
		
		print("save", url)
		# katsotaan oliko kyseisestä sarjasta jo kyseinen kuva
		#url = url"
		tmp_file = ""
		img = None
		if not "base64" in url:
			headers = app.config["REQUEST_HEADER"]
			#req = urllib.request.Request(url, None, headers)
			
			try:
				#tmp_file = urllib.request.urlopen(req).read()
				tmp_file = requests.get(url, headers=headers).content
				
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

		polku = os.path.join(app.config["SARJAKUVA_FOLDER"], self.sarjakuva.lyhenne)

		import io
		img = Image.open(io.BytesIO(tmp_file))
		width, height = img.size
		dhash = imagehash.dhash(img)

		found = self.sessio.query(Strippi).filter(
				Strippi.sarjakuva_id == self.sarjakuva.id,
				Strippi.dhash == str(dhash)
			).first()
		
		if found is None:
			for i in self.sarjakuva.stripit:
				polku_old = os.path.join(polku, i.filename)
				old = Image.open(polku_old)
				if (dhash - imagehash.dhash(old)) < 5:
					found = i
					break

			
		if found and found.width >= width:
			self.Print("ALREADY HAD THIS PICTURE", dhash)
			return True
		
		order = self.sessio.query(Strippi).filter(Strippi.sarjakuva_id==self.sarjakuva.id).count()+1
		if found: 
			order = found.Order()
			print("Suurempi resoluutio. Korvataan kuva", found.width, "vs", width)
		md5_name = "{}_{}.{}".format(self.sarjakuva.lyhenne, order, filetype)

		
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
		if found:
			tmp = found
		else:
			tmp = Strippi(self.sarjakuva.id, urli, md5_name, nimi, url, str(dhash))
			self.sessio.add(tmp)

		tmp.width = width
		tmp.height = height

		# löydettiin kuva, tallennetaan vikaksi urliksi
		save_urli = True
		if self.sarjakuva.ending:
			lopetukset = self.sarjakuva.ending.split(",")

			turli = urli
			while turli[-1] == "/":
				turli = turli[:-1]
			if turli.split("/")[-1] in lopetukset:
				save_urli = False 

		if save_urli:
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