# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat import Sarjis
from werkzeug.urls import url_fix

class ExtraLife(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		articles = self.soup.find_all("article")
		# for article in articles:
		# 	figures = article.find_all("figure")
		# 	for figure in figures:
		images = self.soup.find_all("img", { "class": "comic"})
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
			link = self.soup.find("a", { "class": "next_comic_link"})
			if link and link["href"] != "#":
				ret = "{}".format(link["href"])
		except: pass

		if ret == self.urli:
			return None
		
		return ret

