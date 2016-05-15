# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class NerdRage(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		#div = self.soup.find("div", { "class": "comic-content"})
		
		#images = div.find_all("img")
		#for image in images:
		table = self.soup.find(id="comic")
		if table is None:
			table = self.soup.find("table", { "class": "shadow"} )
		
		images = table.find_all("img")
		for image in images:
			kuva = dict(nimi=None, src=None, filetype=None)
			try:
				if image["src"].index("//") == 0:
					image["src"] = "http:{}".format(image["src"])
			except: pass
			try:
				if image["src"].index("./") == 0:
					image["src"] = image["src"].replace("./", "/")
			except: pass
			
			#image["src"] = u"{}".format(image["src"].replace(u"_250.", u"_1280."))
			
			kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
			if "://" in image["src"]:
				kuva["src"] = url_fix("{}".format(image["src"]))
			else:
				kuva["src"] = url_fix("{}/{}".format(self.sarjakuva.url, image["src"]))
			kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

			kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		
		links = self.soup.find_all("a")
		for link in links:
			img = link.find("img")
			if img:
				alt = img.get("alt")
				if alt and "next comic" in alt.lower():
					ret = "{}/{}".format(self.sarjakuva.url, link["href"])

		if ret == self.urli:
			return None
		
		return ret

