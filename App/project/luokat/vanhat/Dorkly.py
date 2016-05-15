# -*- coding: utf-8 -*-
from project import app, db, Print, Log
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat.Sarjis import Sarjis
from werkzeug.urls import url_fix

class Dorkly(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )


	def Kuvat(self, soup):
		kuvan_nimi = None
		src = None
		
		kuvat = []
		#div = soup.find("div", { "class": "content"})
		#divs = div.find_all("div", { "class": "post-content"})
		#for div in divs:
		images = soup.find_all("img")
		for image in images:
			if not "media.dorkly.cvcdn.com" in image["src"] or image.find_parent("noscript"):
				continue
			kuva = dict(nimi=None, src=None)
			#image["src"] = u"{}".format(image["src"].replace(u"_250.", u"_1280."))
			kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
			kuva["src"] = url_fix(
							"{}".format(image["src"])
						)
			kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

			kuvat.append(kuva)
		
		return kuvat

		
		

	def Next(self):
		ret = self.urli
		
		link = self.soup.find("a", { "class": "previous"})
		
		if link is not None and link["href"] != "#":
			ret = "{}{}".format(
					"http://www.dorkly.com",
					link["href"]
					)

		if ret == self.urli:
			return None
		
		return ret


	# dorklyssä ei voi loopata sarjakuvasta toiseen vaan pitää käydä archiven läpi
	def Loop(self, url=None, sessio=db.session):
		self.sessio = sessio
		self.Init(url)

		linkit = []
		div = self.soup.find("div", { "class": "pods-media"})
		articles = div.find_all("article")
		for article in articles:
			links = article.find_all("a")
			for link in links:
				linkit.insert(0, "{}{}".format(
					"http://www.dorkly.com",
					link["href"]
					))
		for link in linkit:
			soups = []
			next_page = link
			while next_page:
				#print next_page
				r = requests.get(next_page, headers=app.config["REQUEST_HEADER"] )
				soup = BeautifulSoup(r.text)
				soups.append(soup)
					
				nxt = soup.find("a", { "class": "next" })
				if nxt:
					next_page = "{}{}".format(
						"http://www.dorkly.com",
						nxt["href"]
					)
				else:
					next_page = False


			for soup in soups:
				kuvat = self.Kuvat(soup)
				for kuva in kuvat:
					try:
						self.Save(kuva["nimi"], kuva["src"], kuva["filetype"])
					except Exception as e:
						Log(self.sarjakuva.id, self.urli, "Kuvan tallennus epäonnistui", e.message)
		
		return self.Next()
		