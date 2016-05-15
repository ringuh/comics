# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class Dilbert(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		#div = self.soup.find("div", { "class": "comic-content"})
		
		#images = div.find_all("img")
		#for image in images:
		image = self.soup.find("img", { "class": "img-comic" })
		kuva = dict(nimi=None, src=None, filetype="jpg")
		try:
			if image["src"].index("//") == 0:
				image["src"] = "http:{}".format(image["src"])
		except: pass
		try:
			if image["src"].index("./") == 0:
				image["src"] = image["src"].replace("./", "/")
		except: pass
		
		image["src"] = "{}".format(image["src"].replace("_250.", "_1280."))
		
		kuva["nimi"] = "{}.{}".format(image["src"].split("/")[-1], kuva["filetype"]) # kuvan nimi = tiedoston nimi
		kuva["src"] = url_fix(
						"{}".format(image["src"])
					)
		#kuva["filetype"] = u"{}".format(image["src"].split(".")[-1])

		kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		
		links = self.soup.find_all("a")
		for link in links:
			alt = link.get("alt")
			if alt and "newer strip" in alt.lower():
				ret = "{}{}".format(self.sarjakuva.url, link["href"])

		if ret == self.urli:
			return None
		
		return ret

