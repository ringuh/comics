# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
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
		kuva = dict(nimi=None, src=None, filetype=None)
		try:
			if image["src"].index("//") == 0:
				image["src"] = u"http:{}".format(image["src"])
		except: pass
		try:
			if image["src"].index("./") == 0:
				image["src"] = image["src"].replace("./", "/")
		except: pass

		kuva["nimi"] = u"{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
		kuva["src"] = url_fix(
						u"{}".format(image["src"])
					)
		if not "://" in kuva["src"]:
			kuva["src"] = url_fix(
						u"{}/{}".format(self.sarjakuva.url, image["src"])
					)
		kuva["filetype"] = u"{}".format(image["src"].split(".")[-1])
		
		kuvat.append(kuva)

		return kuvat

		
		

	def Next(self):
		ret = self.urli
		
		div = self.soup.find("div", { "class": "navbar" })
		links = div.find_all("a")
		for link in links:
			if "next" in link.text.strip().lower()[:4] and link["href"] != "#":
				ret = u"{}".format(link["href"])
				if not "://" in ret:
					ret = u"{}/{}".format(self.sarjakuva.url, ret)
		
		if ret == self.urli:
			return None
		
		return ret

