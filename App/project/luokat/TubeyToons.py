# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class TubeyToons(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		#div = self.soup.find("div", { "class": "comic-content"})
		
		divs = self.soup.find_all("div", { "class": "comic-image"})
		for div in divs:
			images = div.find_all("img")
			for image in images:
				#print image
				try:
					if not "/comics/" in image["src"]:
						continue
				except Exception, e:
					continue
				
				kuva = dict(nimi=None, src=None, filetype=None)
				try:
					if image["src"].index("//") == 0:
						image["src"] = u"http:{}".format(image["src"])
				except: pass
				try:
					if image["src"].index("./") == 0:
						image["src"] = image["src"].replace("./", "/")
				except: pass
				
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
			span = self.soup.find("span", { "class": "hvr-skew-forward"})
		
			g = span.get("onclick")

			g = g.replace("goCom(", "").replace(")", "")
			id, cmd = g.split(",") 

			ret = u"{}/{}".format(self.sarjakuva.url, int(id)+1)
		except Exception, e: pass

		if ret == self.urli:
			return None
		
		return ret

