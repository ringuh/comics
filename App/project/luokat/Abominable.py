# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat import Sarjis
from werkzeug.urls import url_fix

class Abominable(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		
		figures = self.soup.find_all("div", { "class": "photo" })
		for figure in figures:
			images = figure.find_all("img")
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
			div = self.soup.find("div", { "class": "photo-btn-next"})
			link = div.find("a")
		
			if link and link["href"] != "#":
				ret = u"{}".format(link["href"])
		except: pass

		if ret == self.urli:
			return None
		
		return ret

