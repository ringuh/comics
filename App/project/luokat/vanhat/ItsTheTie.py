# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class ItsTheTie(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		#div = self.soup.find("div", { "class": "comic-content"})
		
		#images = div.find_all("img")
		#for image in images:
		
		# image = self.soup.find("img", { "class": "alignnone"})
		# if image is None:
		# 	image = self.soup.find("img", { "class": "aligncenter"})
		
		images = self.soup.find_all("img")
		for image in images:
			
			try:
				width = image.get("width")
				
				if int(width) < 400:
					continue
			except Exception as e: 
				#print e
				continue
			

			
			kuva = dict(nimi=None, src=None, filetype=None)
			try:
				image["src"] = image["src"].split("?")[0]
				if image["src"].index("//") == 0:
					image["src"] = "http:{}".format(image["src"])
			except: pass
			try:
				if image["src"].index("./") == 0:
					image["src"] = image["src"].replace("./", "/")
			except: pass
			
			#image["src"] = u"{}".format(image["src"].replace(u"_250.", u"_1280."))
			
			kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
			
			if "data:image" in image["src"]:
				kuva["src"] = image["src"]
			elif "://" in image["src"]:
				kuva["src"] = url_fix("{}".format(image["src"]))
			else:
				kuva["src"] = url_fix("{}{}".format(self.sarjakuva.url, image["src"]))
			kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

			kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		try:
			

			nav = self.soup.find("div", {"class":"nav-next"})
			if nav is None:
				nav = self.soup.find("span", {"class":"nav-next"})

			link = nav.find("a")
			if link:
				ret = link["href"]

			# rikkonainen nginx
			if ret == "http://www.commitstrip.com/en/2013/03/22/commitstrip-fete-ses-1-an-o/":
				ret = "http://www.commitstrip.com/en/2013/03/25/cest-ce-que-jallais-faire/"
		except: pass

		if ret == self.urli:
			return None
		
		return ret

