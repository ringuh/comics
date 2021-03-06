# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class OrderOfTheStick(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvan_nimi = None
		src = None
		
		kuvat = []
		images = self.soup.find_all("img")
		for image in images:
			if "/comics/images/" in image["src"]:
				kuva = dict(nimi=None, src=None)
				kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
				kuva["src"] = url_fix(
								"{}{}".format(self.sarjakuva.url, image["src"])
							)
				kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

				kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		
		links = self.soup.find_all("a")

		for link in links:
			img = link.find("img")

			if img is not None and img.get("title") is not None and img.get("title").lower() == "next comic":
				if link["href"] != "#":
					ret = "{}{}".format(self.sarjakuva.url, link["href"])


		if ret == self.urli:
			return None
		
		return ret

