# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class Oglaf(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvan_nimi = None
		src = None
		
		kuvat = []
		
		
		image = self.soup.find(id="strip")
		kuva = dict(nimi=None, src=None)
		#image["src"] = u"{}".format(image["src"].replace(u"_250.", u"_1280."))
		kuva["nimi"] = u"{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
		kuva["src"] = url_fix(
						u"{}".format(image["src"])
					)
		kuva["filetype"] = u"{}".format("jpg")
					#image["src"].split(".")[-1])

		kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		nav = self.soup.find(id="nav")
		nav_links = nav.find_all('a')
		for nn in nav_links:
			link = nn.find(id="nx")
			if link is not None and nn["href"] is not None:
				ret = u"{}{}".format(u"http://oglaf.com", nn["href"])

		if ret == self.urli:
			return None
		
		return ret

