# -*- coding: utf-8 -*-
from project import app, db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class CtrlAltDel(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvan_nimi = None
		src = None
		
		kuvat = []

		# articles = self.soup.find_all("center")
		# for article in articles:
		
		figure = self.soup.find(id="content")
		images = figure.find_all("img")
		for image in images:
			kuva = dict(nimi=None, src=None)
			if image["src"].index("//") == 0:
				image["src"] = u"http:{}".format(image["src"])
			
			if not "/comics/" in image["src"]: continue

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
		link = self.soup.find("a", { "class": "nav-next" })

		if len(link["href"]) < 8:
			date = self.urli.split("/")[-1]
			date = datetime.datetime.strptime(date, "%Y%m%d")
			while date < datetime.datetime.now():
				date = date + datetime.timedelta(days=1)
				stamp = date.strftime("%Y%m%d")

				url = u"{}{}{}".format(self.sarjakuva.url, "/cad/", stamp)
				r = requests.get(url, headers=app.config["REQUEST_HEADER"] )
				self.soup = BeautifulSoup(r.text)
				tmp = self.soup.find("a", { "class": "nav-next" })
				
				if tmp and len(tmp["href"]) < 8:
					ret = url
					break
		else:		
			ret = u"{}{}".format(self.sarjakuva.url, link["href"])

		if ret == self.urli:
			return None
		
		return ret

