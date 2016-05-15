# -*- coding: utf-8 -*-
from project import app, db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, urllib.request, urllib.error, urllib.parse, os, requests, hashlib
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
		
		loaded = self.sessio.query(Strippi.rname).filter(
				Strippi.sarjakuva_id==self.sarjakuva.id
			).all()
		loaded = [i.rname for i in loaded]
		for nr in arr:
			src = "{}pages/{}.png".format(self.sarjakuva.url, nr)
			
			
			nimi = "{}.png".format(nr)
			filetype = "png"

			if nimi in loaded:
				continue
			
			filetype = "{}".format(nimi.split(".")[-1])
			
			if not filetype in kuvat: # ei oikeanlainen kuva
				continue

			if not self.Save(nimi, src, filetype):
				src = "{}{}.png".format(self.sarjakuva.url, nr)
				if not self.Save(nimi, src, filetype):
					src = "{}{}.gif".format(self.sarjakuva.url, nr)
					filetype = "gif"
					if not self.Save(nimi, src, filetype):
						src = "{}{}.gif".format(self.sarjakuva.url, int(nr))


		return None
			

			
