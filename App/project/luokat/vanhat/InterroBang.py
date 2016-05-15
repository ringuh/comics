# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class InterroBang(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		div = self.soup.find("div", { "class": "comic-content"})
		
		images = div.find_all("img")
		for image in images:
			kuva = dict(nimi=None, src=None)
			try:
				if image["src"].index("//") == 0:
					image["src"] = "http:{}".format(image["src"])
			except: pass
			try:
				if image["src"].index("./") == 0:
					image["src"] = image["src"].replace("./", "/")
			except: pass
			
			image["src"] = "{}".format(image["src"].replace("_250.", "_1280."))
			kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
			kuva["src"] = url_fix(
							"{}{}".format("http://www.interrobangstudios.com/", image["src"])
						)
			kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

			kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		div = self.soup.find("div", { "class": "comic-rightnav"})
		links = div.find_all("a")
		for link in links:
			img = link.find("img")
			if img and "nav_next.png" in img["src"]:
				if link["href"] != "#":
					if "http:" in link["href"]:
						ret = link["href"]
					else:
						ret = "{}{}".format("http://www.interrobangstudios.com/", link["href"])

		if ret == self.urli:
			return None
		
		return ret

