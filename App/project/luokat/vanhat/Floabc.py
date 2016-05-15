# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class Floabc(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		
		#mages = self.soup.find_all("img", { "class": "strip" })
		#for image in images:
		image = self.soup.find(id="comicimg")
		if image:
			kuva = dict(nimi=None, src=None, filetype=None)
			try:
				if image["src"].index("//") == 0:
					image["src"] = "http:{}".format(image["src"])
			except: pass
			try:
				if image["src"].index("./") == 0:
					image["src"] = image["src"].replace("./", "/")
			except: pass

			kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
			kuva["src"] = url_fix(
							"{}".format(image["src"])
						)
			if not "://" in kuva["src"]:
				kuva["src"] = url_fix(
							"{}/{}".format(self.sarjakuva.url, image["src"])
						)
			kuva["filetype"] = "{}".format(image["src"].split(".")[-1])
			
			kuvat.append(kuva)

		return kuvat

		
		

	def Next(self):
		ret = self.urli
		try:
			div = self.soup.find("div", { "class": "navbar" })
			links = div.find_all("a")
			for link in links:
				if "next" in link.text.strip().lower()[:4] and link["href"] != "#":
					ret = "{}".format(link["href"])
					if not "://" in ret:
						ret = "{}/{}".format(self.sarjakuva.url, ret)
					break
		except: pass
		
		if ret == self.urli:
			return None
		
		return ret

