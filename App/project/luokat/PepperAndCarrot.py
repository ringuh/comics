# -*- coding: utf-8 -*-
from project import app, db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat import Sarjis
from project.models import Strippi
from werkzeug.urls import url_fix

class PepperAndCarrot(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		links = self.soup.find_all("a")
		for link in links:
			url = link.text.strip().lower()
			if url[:3] == "en_" and "xxl" in url:
				image = dict(src=link["href"])

				kuva = dict(nimi=None, src=None, filetype=None)
				try:
					if image["src"].index("//") == 0:
						image["src"] = u"http:{}".format(image["src"])
				except: pass
				try:
					if image["src"].index("./") == 0:
						image["src"] = image["src"].replace("./", "/")
				except: pass
				image["src"] = image["src"].split("?")[0]
				image["src"] = u"{}".format(image["src"].replace(u"_250.", u"_1280."))
				image["src"] = u"{}".format(image["src"].replace(u"_500.", u"_1280."))
				kuva["nimi"] = u"{}.{}".format(image["src"].split("/")[-1], kuva["filetype"]) # kuvan nimi = tiedoston nimi
				
				kuva["src"] = url_fix(u"{}".format(image["src"]))
				if not "://" in image["src"]:
					kuva["src"] = url_fix(
									u"{}{}".format(self.sarjakuva.url, image["src"])
								)
				kuva["filetype"] = u"{}".format(image["src"].split(".")[-1])

				found = self.sessio.query(Strippi).filter(
						Strippi.sarjakuva_id == self.sarjakuva.id,
						Strippi.url == image["src"]
					).first()

				if not found:
					kuvat.append(kuva)
		kuvat.sort()

		return kuvat

		
		
	def Next(self):
		return None
				




