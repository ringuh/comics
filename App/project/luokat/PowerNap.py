# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat import Sarjis
from werkzeug.urls import url_fix

class PowerNap(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvan_nimi = None
		src = None
		
		kuvat = []
		
		centers = self.soup.find_all("center")
		
		for i in centers:
			center = i.find("center")
			image = i.find("img")
			br = i.find("br")
			if center is None and image and br:		
				kuva = dict(nimi=None, src=None)
				image["src"] = image["src"].replace("\n", "")
				if image["src"].index("//") == 0:
					image["src"] = u"http:{}".format(image["src"])
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
		
		try:
			links = self.soup.find_all("a")
			for link in links:
				img = link.find("img")

				if img and img.get("alt") and "next" in img.get("alt").lower():
					if link["href"] != "#":
						ret = u"{}".format(link["href"])
						break
		except: pass

		if ret == self.urli:
			return None
		
		return ret

