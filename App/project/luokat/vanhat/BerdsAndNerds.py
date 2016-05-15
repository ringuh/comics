# -*- coding: utf-8 -*-
from project import app, db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat import Sarjis
from werkzeug.urls import url_fix

class BerdsAndNerds(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		div = self.soup.find("noscript")
		image = div.find("img")
			
		kuva = dict(nimi=None, src=None, filetype="png")
		try:
			if image["src"].index("//") == 0:
				image["src"] = "http:{}".format(image["src"])
		except: pass
		try:
			if image["src"].index("./") == 0:
				image["src"] = image["src"].replace("./", "/")
		except: pass
		image["src"] = image["src"].split("?")[0]
		image["src"] = "{}".format(image["src"].replace("_250.", "_1280."))
		image["src"] = "{}".format(image["src"].replace("_500.", "_1280."))
		kuva["nimi"] = "{}.{}".format(image["src"].split("/")[-1], kuva["filetype"]) # kuvan nimi = tiedoston nimi
		
		kuva["src"] = url_fix("{}".format(image["src"]))
		if not "://" in image["src"]:
			kuva["src"] = url_fix(
							"{}{}".format(self.sarjakuva.url, image["src"])
						)
		#kuva["filetype"] = u"{}".format(image["src"].split(".")[-1])

		kuvat.append(kuva)
		
		return kuvat

		
		
	def Loop(self, url=None, sessio=db.session):
		self.sessio = sessio
		url = "http://berdsandnerds.com/thearchive/"
		# ylikirjoitetaan last_url tässä tapauksessa
		self.Init(url)

		from project.models import Strippi

		loaded = sessio.query(Strippi.page_url).filter(
				Strippi.sarjakuva_id==self.sarjakuva.id
			).all()
		loaded = [i.page_url for i in loaded]
		#count = 0
		ol = self.soup.find("ol")
		lis = ol.find_all("li")
		for li in lis:
			link = li.find("a")
			urli = link.get("href")

			if not urli:
				continue
			if not "://" in urli:
				urli = "{}{}".format(self.sarjakuva.url, urli)
			
			if urli in loaded:
				continue
			try:
				r = requests.get(urli, headers=app.config["REQUEST_HEADER"] )
				self.soup = BeautifulSoup(r.text)
				kuvat = self.Kuvat()
			except Exception as e:
				Log(self.sarjakuva.id, urli, "Kuvan haku epäonnistui", e)
				continue

			for kuva in kuvat:
				try:
					if self.sarjakuva.download:
						self.Save(kuva["nimi"], kuva["src"], kuva["filetype"], urli)
					else:
						self.Iframe(kuva["nimi"], kuva["src"], kuva["filetype"], urli)
					
				except Exception as e:
					Log(self.sarjakuva.id, urli, "Kuvan tallennus epäonnistui", e, kuva["src"])
		
		
			
		return None

				




