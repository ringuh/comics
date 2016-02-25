# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class LoadingArtist(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		content = self.soup.find("div", { "class": "comic"})
		
		#images = div.find_all("img")
		#for image in images:
		divs = content.find_all("div", { "class": "comic" })
		for div in divs:
			images = div.find_all("img")
			for image in images:
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
								u"{}".format(image["src"])
							)
				kuva["filetype"] = u"{}".format(image["src"].split(".")[-1])

				kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli

		#content = self.soup.find("div", { "class": "comic"})
		#div = content.find("div", { "class": "comic"})
		try:
			link = self.soup.find("a", { "class": "next" })
			if link:
				ret = link["href"]
		except: pass

		if ret == self.urli:
			return None
		
		return ret

