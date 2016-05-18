# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat import Sarjis
from project.models import Strippi
from werkzeug.urls import url_fix

class Catsu(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		ul = self.soup.find("ul", {"class":"latest-blog-posts-list"})
		images = ul.find_all("img")
		for image in images:
			if not "comic" in image["src"]:
				continue

				
			kuva = dict(nimi=None, src=None)
			image["src"] = image["src"].split("?")[0]
			try:
				if image["src"].index("//") == 0:
					image["src"] = "http:{}".format(image["src"])
			except: pass
			try:
				if image["src"].index("./") == 0:
					image["src"] = image["src"].replace("./", "/")
			except: pass
			image["src"] = "{}".format(image["src"].replace("_250.", "_1280."))
			image["src"] = "{}".format(image["src"].replace("_500.", "_1280."))
			kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
			kuva["src"] = url_fix("{}".format(image["src"]))
			kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

			found = self.sessio.query(Strippi).filter(
						Strippi.sarjakuva_id == self.sarjakuva.id,
						Strippi.url == image["src"]
					).first()

			if not found:
				kuvat.append(kuva)
			
		
		return kuvat

		
		

	def Next(self):
		return None

