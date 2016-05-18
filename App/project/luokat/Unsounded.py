# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat import Sarjis
from project.models import Strippi
from werkzeug.urls import url_fix

class Unsounded(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		# div = self.soup.find(id="comic")
		# if div is None:
		# 	div = self.soup.find(id="contentbody2")
		images = self.soup.find_all("img")
		for image in images:				
			kuva = dict(nimi=None, src=None)
			image["src"] = image["src"].split("?")[0]
			
			# oletetaan, että kaikki sisältö on "pageart/"
			if not "pageart/" in image["src"]: continue

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
			
			tmp = self.urli.split("/")
			tmp[-1] = image["src"]
			kuva["src"] = url_fix("/".join(tmp))
				
			kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

			found = self.sessio.query(Strippi).filter(
						Strippi.sarjakuva_id == self.sarjakuva.id,
						Strippi.url == image["src"]
					).first()

			if not found:
				kuvat.append(kuva)
			
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		try:

			link = self.soup.find("a", {"class": "forward"})
			if not link:
				link = self.soup.find("a", {"class": "forward_dark"})
		
			tmp = self.urli.split("/")

			if "://" in link["href"]:
				ret = link["href"]
			else:
				if "../" in link["href"]:
					link["href"] = link["href"].replace("../", "")
					tmp = tmp[:-1]
				tmp[-1] = link["href"]

				ret = "/".join(tmp)
			
		except: pass

		if ret == self.urli or not "/comic/" in ret:
			return None
		
		return ret

