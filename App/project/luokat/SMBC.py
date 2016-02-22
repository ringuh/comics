# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class SMBC(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		#div = self.soup.find("div", { "class": "comic-content"})
		
		#images = div.find_all("img")
		#for image in images:
		div = self.soup.find(id="comicbody")
		image = div.find("img")
		kuva = dict(nimi=None, src=None, filetype=None)
		try:
			if image["src"].index("//") == 0:
				image["src"] = u"http:{}".format(image["src"])
		except: pass
		try:
			if image["src"].index("./") == 0:
				image["src"] = image["src"].replace("./", "/")
		except: pass
		
		#image["src"] = u"{}".format(image["src"].replace(u"_250.", u"_1280."))
		
		kuva["nimi"] = u"{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
		kuva["src"] = url_fix(
						u"{}/{}".format(self.sarjakuva.url, image["src"])
					)
		kuva["filetype"] = u"{}".format(image["src"].split(".")[-1])

		kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		
		div = self.soup.find(id="comicbody")
		link = div.find("a")
		
		if link is not None:
			if self.sarjakuva.url in link["href"]:
				ret = link["href"]
			else:
				ret = u"{}{}".format(self.sarjakuva.url, link["href"])

		if ret == self.urli:
			return None
		
		return ret

