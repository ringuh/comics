# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class StandStill(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
	
		div = self.soup.find(id="wrapper2")
		images = div.find_all("img")
		for image in images:
			
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
				kuva["src"] = url_fix("{}".format(image["src"].strip()))
			else:
				kuva["src"] = url_fix("{}/{}".format(self.sarjakuva.url, image["src"].strip()))
			kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

			kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		
		try:			
			div = self.soup.find(id="navtop")
			links = div.find_all("a")
			for link in links:
				btn = link.find(id="navnext")
				if btn:
					ret = "{}/comic.php{}".format(self.sarjakuva.url, link["href"])
					break
		except: pass

		if ret == self.urli:
			return None
		
		return ret

