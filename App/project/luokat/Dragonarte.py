# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from project.models import Strippi
from werkzeug.urls import url_fix

class Dragonarte(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )



	def Loop(self, url=None, sessio=db.session):
		self.sessio = sessio
		self.Init(url)

		kuvat = ["jpg", "jpeg", "gif", "png", "svg"]
		links = self.soup.find_all("a")
		count = 0
		loaded = sessio.query(Strippi.url).filter(
				Strippi.sarjakuva_id==self.sarjakuva.id
			).all()
		loaded = [i.url for i in loaded]
		
		for link in links:
			
			nimi = link["href"]

			src = url_fix(
					"{}{}".format(self.sarjakuva.last_url, nimi)
				)
			filetype = "{}".format(nimi.split(".")[-1])
			
			if src in loaded:
				continue

			count += 1
			if not filetype in kuvat: # ei oikeanlainen kuva
				continue
			
			self.Save(nimi, src, filetype)

		return None
			

			
