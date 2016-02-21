# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class Gunshow(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvan_nimi = None
		src = None
		
		kuvat = []
		# articles = self.soup.find_all("article")
		# for article in articles:
		# 	figures = article.find_all("figure")
		# 	for figure in figures:
		# 		images = figure.find_all("img")
		# 		for image in images:
		div = self.soup.find(id="comic")
		image = div.find("img", { "class": "strip" })
		kuva = dict(nimi=None, src=None)
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
		links = self.soup.find_all("a")
		for link in links:
			img = link.find("img")
			if img is not None and img["src"] == "menu/small/next.gif":
				ret = u"{}{}".format(self.sarjakuva.url, link["href"])
				break
		
		if ret == self.urli:
			return None
		
		return ret

