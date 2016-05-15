# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class Paintrain(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):		
		kuvat = []
	# 	articles = self.soup.find_all("article")
	# 	for article in articles:
	# 		figures = article.find_all("figure")
	# 		for figure in figures:
	# 			images = figure.find_all("img")
	# #for image in images:
		
		kuva = dict(nimi=None, src=None)
		div = self.soup.find(id="comic-page")
		if div is None:
			div = self.soup.find(id="comic")
			if div is None:
				div = self.soup.find("div", { "class": "comic" })
		

		images = div.find_all("img")
		for image in images:
			if "?" in image["src"]:
				image["src"] = image["src"].split("?")[0]

			
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
		#nav = self.soup.find("nav", { "class": "comic-pagination" })
		try:
			link = self.soup.find("a", { "class": "comic-nav-next"})
			if not link:
				link = self.soup.find("a", { "class": "next" })
				if not link:
					link = self.soup.find("a", { "class": "nav-next" })

			
			if link and link["href"] != "#":
				ret = "{}".format(link["href"])
		except: pass

		if ret == self.urli:
			return None
		
		return ret

