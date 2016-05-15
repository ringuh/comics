# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class Blastwave(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
	
		div = self.soup.find(id="comic_ruutu")
		images = div.find_all("img")
		for image in images:
			if not "comics" in image["src"]:
				continue
			kuva = dict(nimi=None, src=None, filetype=None)
			try:
				if image["src"].index("//") == 0:
					image["src"] = "http:{}".format(image["src"])
			except: pass
			try:
				if image["src"].index("./") == 0:
					image["src"] = image["src"].replace("./", "/")
			except: pass

			
			kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
			if "://" in image["src"]:
				kuva["src"] = url_fix("{}".format(image["src"]))
			else:
				kuva["src"] = url_fix("{}/{}".format(self.sarjakuva.url, image["src"]))
			kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

			kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		
		try:
			links = self.soup.find_all("a")
			for link in links:
				img = link.find("img")
				if img and "next.jpg" in img["src"]:
					ret = "{}/{}".format(self.sarjakuva.url, link["href"])
		except: pass

		if ret == self.urli:
			return None
		
		return ret

