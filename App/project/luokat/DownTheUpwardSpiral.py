# -*- coding: utf-8 -*-
from project import app, db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat import Sarjis
from werkzeug.urls import url_fix

class DownTheUpwardSpiral(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self):
		kuvat = []
		div = self.soup.find(id="wsite-content")
		
		figures = div.find_all("div", {"class": "wsite-image"})
		for figure in figures:
			images = figure.find_all("img")
			for image in images:
				kuva = dict(nimi=None, src=None)
				try:
					if image["src"].index("//") == 0:
						image["src"] = "http:{}".format(image["src"])
				except: pass
				try:
					if image["src"].index("./") == 0:
						image["src"] = image["src"].replace("./", "/")
				except: pass
				image["src"] = image["src"].split("?")[0]
				image["src"] = "{}".format(image["src"].replace("_250.", "_1280."))
				image["src"] = "{}".format(image["src"].replace("_500.", "_1280."))
				kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
				kuva["src"] = url_fix(
								"{}{}".format(self.sarjakuva.url, image["src"])
							)
				kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

				kuvat.append(kuva)
		
		return kuvat

		
		
	def Loop(self, url=None, sessio=db.session):
		self.sessio = sessio
		url = "http://www.downtheupwardspiral.com/gallery.html"
		# ylikirjoitetaan last_url tässä tapauksessa
		self.Init(url)

		from project.models import Strippi

		loaded = sessio.query(Strippi.page_url).filter(
				Strippi.sarjakuva_id==self.sarjakuva.id
			).all()
		loaded = [i.page_url for i in loaded]
		#count = 0
		tds = self.soup.find_all("td", {"class": "wsite-multicol-col"})
		for td in tds:
			div = td.find("div", {"class": "wsite-image"})
			if div is None:
				#print "not div"
				continue
			link = div.find("a")
			urli = link.get("href")

			if not urli:
				#print "not urli"
				continue
			
			urli = "{}{}".format(self.sarjakuva.url, urli)
			
			if urli in loaded:
				#print "skip", urli
				continue
			try:
				r = requests.get(urli, headers=app.config["REQUEST_HEADER"] )
				self.soup = BeautifulSoup(r.text, "html.parser")
				kuvat = self.Kuvat()
			except Exception as e:
				Log(self.sarjakuva.id, urli, "Kuvan haku epäonnistui", e)
				continue

			for kuva in kuvat:
				try:
					if self.sarjakuva.download:
						self.Save(kuva["nimi"], kuva["src"], kuva["filetype"], urli)
					else:
						self.Iframe(kuva["nimi"], kuva["src"], kuva["filetype"], urli)
					
				except Exception as e:
					Log(self.sarjakuva.id, urli, "Kuvan tallennus epäonnistui", e, kuva["src"])
		
		
			
		return None

				




