# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class HiveWorks(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		
		#mages = self.soup.find_all("img", { "class": "strip" })
		#for image in images:
		image = self.soup.find(id="cc-comic")
		kuva = dict(nimi=None, src=None, filetype="gif")
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
		kuva["filetype"] = "{}".format(image["src"].split(".")[-1])
		
		kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		
		#nav = self.soup.find("ul", {"class":"feature-nav"})
		link = self.soup.find("a", {"class": "next"})
		if link and link["href"] != "#":
			ret = "{}".format(link["href"])
		
		if ret == self.urli:
			return None
		
		return ret

