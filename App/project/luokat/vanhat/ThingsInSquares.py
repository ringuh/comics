# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat import Sarjis
from werkzeug.urls import url_fix

class ThingsInSquares(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		div = self.soup.find(id="content")
		article = div.find("article")
		divs = article.find_all("div", {"class": "entry-content"})
		for div in divs:
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
				image["src"] = "{}".format(image["src"].replace("_500.", "_1280."))
				kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
				kuva["src"] = url_fix(
								"{}".format(image["src"])
							)
				kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

				kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		try:
			div = self.soup.find("div", {"class": "nav-links"})
			if div is None:
				div = self.soup.find("div", {"class": "entry-navarrows"})
		
			links = div.find_all("a")
			for link in links:
				rel = link.get("rel")
				if rel and "next" in rel:
					if link["href"] is not None:
						ret = link["href"]

		except: pass

		if ret == self.urli:
			return None
		
		return ret

