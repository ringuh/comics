# -*- coding: utf-8 -*-
from project import app, db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, urllib2, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from project.models import Strippi
from werkzeug.urls import url_fix

class AvasDemon(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Loop(self, url=None, sessio=db.session):
		self.sessio = sessio
		self.Init(url)

		kuvat = ["jpg", "jpeg", "gif", "png", "svg"]

		arr = []
		div = self.soup.find(id="chapters")
		links = div.find_all("a")

		for link in links:
			if "page=" in link["href"]:
				text, nr = link["href"].split("=")
				arr.append(nr)

		arr.sort()
		

		for nr in arr:
			src = u"{}pages/{}.png".format(self.sarjakuva.url, nr)
			
			
			nimi = u"{}.png".format(nr)
			filetype = "png"

			
			filetype = u"{}".format(nimi.split(".")[-1])
			
			if not filetype in kuvat: # ei oikeanlainen kuva
				continue

			if not self.Save(nimi, src, filetype):
				src = u"{}{}.png".format(self.sarjakuva.url, nr)
				if not self.Save(nimi, src, filetype):
					src = u"{}{}.gif".format(self.sarjakuva.url, nr)
					filetype = "gif"
					if not self.Save(nimi, src, filetype):
						src = u"{}{}.gif".format(self.sarjakuva.url, int(nr))


		return None
			

			
