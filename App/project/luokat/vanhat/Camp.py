# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat import HappleTea, Sarjis
from werkzeug.urls import url_fix

class Camp(HappleTea):

	def __init__(self, sarjakuva ):
		HappleTea.__init__(self, sarjakuva )

	# def Kuvat(self):
	# 	kuvat = []

	# 	kuva = dict(nimi=None, src=None)
	# 	div = self.soup.find(id="comic")
	# 	image = div.find("img")
	# 	print image
	# 	if image["src"].index("//") == 0:
	# 		image["src"] = u"http:{}".format(image["src"])
	# 	image["src"] = u"{}".format(image["src"].replace(u"_250.", u"_1280."))
	# 	kuva["nimi"] = u"{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
	# 	kuva["src"] = url_fix(
	# 					u"{}".format(image["src"])
	# 				)
	# 	kuva["filetype"] = u"{}".format(image["src"].split(".")[-1])

	# 	kuvat.append(kuva)
		
	# 	return kuvat
	
		

	def Next(self):
		ret = self.urli
		
		link = self.soup.find("a", { "class":"btnNext" })
		
		if link and link["href"] != "#":
			ret = "{}".format(link["href"])

		if ret == self.urli:
			return None
		
		return ret
