# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class NerfNow(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvan_nimi = None
		src = None
		
		kuvat = []
		
		div = self.soup.find(id="comic")
		image = div.find("img")
		kuva = dict(nimi=None, src=None)
		if image["src"].index("//") == 0:
			image["src"] = "http:{}".format(image["src"])
		image["src"] = "{}".format(image["src"].replace("_250.", "_1280."))
		kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
		kuva["src"] = url_fix(
						"{}".format(image["src"])
					)
		kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

		kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		link = self.soup.find(id="nav_next").find("a")

		if link and link["href"] != "#":
			ret = link["href"]
		

		if ret == self.urli:
			return None
		
		return ret

