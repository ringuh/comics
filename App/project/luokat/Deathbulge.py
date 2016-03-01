# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class Deathbulge(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		
		#mages = self.soup.find_all("img", { "class": "strip" })
		#for image in images:
		#print self.soup
		image = self.soup.find(id="next-button")
		print image
		#images = self.soup.find_all("img")
		
		kuva = dict(nimi=None, src=None, filetype="gif")
		try:
			if image["src"].index("//") == 0:
				image["src"] = u"http:{}".format(image["src"])
		except: pass
		try:
			if image["src"].index("./") == 0:
				image["src"] = image["src"].replace("./", "/")
		except: pass

		try:
			if image["src"].index("#/") == 0:
				image["src"] = image["src"].replace("#/", "/")
		except: pass

		kuva["nimi"] = u"{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
		
		if "://" in image["src"]:
			kuva["src"] = url_fix(u"{}".format(image["src"]))
		else:
			kuva["src"] = url_fix(u"{}{}".format(self.sarjakuva.url, image["src"]))
		kuva["filetype"] = u"{}".format(image["src"].split(".")[-1])
		
		kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		
		#nav = self.soup.find("ul", {"class":"feature-nav"})
		
		try:
			link = self.soup.find(id="next-button")
			try:
				if image["src"].index("#/") == 0:
					image["src"] = image["src"].replace("#/", "/")
			except: pass
			if link and link["href"] != "#":
				ret = u"{}{}".format(self.sarjakuva.url, link["href"])
		except: pass
		
		if ret == self.urli:
			return None
		
		return ret

