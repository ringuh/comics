# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class VGCats(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		
		kuvat = []

		# table = self.soup.find("table")
		# table = table.find("tbody")
		# table = self.soup.find("tr").find("td")

		found = self.soup.find_all("img")
		for image in found:
			try:
				if image["src"].index("images/") == 0:
					kuva = dict(nimi=None, src=None)
					# if image["src"].index("//") == 0:
					# 	image["src"] = u"http:{}".format(image["src"])
					#image["src"] = u"{}".format(image["src"].replace(u"_250.", u"_1280."))
					kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
					kuva["src"] = url_fix(
									"{}{}".format(self.sarjakuva.url, image["src"])
								)
					kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

					kuvat.append(kuva)
					
					break

			except Exception as e: pass

		return kuvat

		
		

	def Next(self):
		ret = self.urli
		linkit = self.soup.find_all("a")
		
		for i in linkit:
			tmp = i.find("img")
			if tmp is not None and tmp["src"] == "next.gif":
				ret =  "{}{}".format(self.sarjakuva.url, i["href"])
				break

		if ret == self.urli:
			return None
		
		return ret

