# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat import Sarjis
from werkzeug.urls import url_fix

class RomanticallyApocalyptic(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		div = self.soup.find("div", { "class": "comicpanel"})
		
		div = div.find("center")
		
		images = div.find_all("img")
		for image in images:
			kuva = dict(nimi=None, src=None)
			try:
				if image["src"].index("//") == 0:
					image["src"] = u"http:{}".format(image["src"])
			except: pass
			try:
				if image["src"].index("./") == 0:
					image["src"] = image["src"].replace("./", "/")
			except: pass
			image["src"] = u"{}".format(image["src"].replace(u"_250.", u"_1280."))
			image["src"] = u"{}".format(image["src"].replace(u"_500.", u"_1280."))
			kuva["nimi"] = u"{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
			kuva["src"] = url_fix(
							u"{}".format(image["src"])
						)
			kuva["filetype"] = u"{}".format(image["src"].split(".")[-1])

			kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		try:
			div = self.soup.find("div", { "class": "comicpanel"})
			links = div.find_all("a")
		
			for link in links:
				access = link.get("accesskey")
				if access and "n" in access:
					ret = link["href"]
					break
		except: pass

		if ret == self.urli:
			return None
		
		return ret

