# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class Garfield(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		
		div = self.soup.find(id="comic_wrap")

		images = div.find_all("img")
		for image in images:
			
			kuva = dict(nimi=None, src=None)
			if image["src"].index("//") == 0:
				image["src"] = "http:{}".format(image["src"])
			#image["src"] = u"{}".format(image["src"].replace(u"_250.", u"_1280."))
			kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
			kuva["src"] = url_fix(
							"{}".format(image["src"])
						)
			kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

			kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		link = self.soup.find("a", {"class": "comic-arrow-right"})
		
		if link and link["href"] != "#":
			ret = "{}".format(link["href"])

		if ret == self.urli:
			return None
		
		return ret

