# -*- coding: utf-8 -*-
from project import db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib, os, requests, hashlib
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
		
		count = 0
		loaded = sessio.query(Strippi.rname).filter(
				Strippi.sarjakuva_id==self.sarjakuva.id
			).all()
		for nr in arr:
			src = u"{}pages/{}.png".format(self.sarjakuva.url, nr)
			nimi = u"{}.png".format(nr)
			filetype = ".png"

			
			filetype = u"{}".format(nimi.split(".")[-1])
			if nimi in loaded:
				continue
			#if count > 5:
			#	return
			count += 1
			if not filetype in kuvat: # ei oikeanlainen kuva
				continue
			
			self.Save(nimi, src, filetype)

		return None
			

			
