# -*- coding: utf-8 -*-
from project import db, Print, Log, app
from bs4 import BeautifulSoup
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat import Sarjis
from project.models import Strippi
from werkzeug.urls import url_fix
import feedparser

class RSSReader(Sarjis):

	def __init__(self, sarjakuva ):
		Sarjis.__init__(self, sarjakuva )

	def Init(self, url=None, ):
		self.urli = url
		if url is None:
			self.urli = self.sarjakuva.last_url			
		

		#fo = open("foo.html", "wb")
		

		
		self.Print("Finding url", self.urli)
		print("\nFinding url", self.urli)
		
		self.soup = feedparser.parse(self.urli)

		self.Print(self.soup)
		self.Print("\n\n")
		#fo.write(str(self.soup));
		#fo.close()

	def Kuvat(self):
		kuvat = []
		
		images = []
		for i in self.soup.entries:
			tmp = i.description
			tt = BeautifulSoup(tmp, 'html.parser')
			try: images.insert(0, { "src": tt.find("img")["src"] })
			except: continue
		
		# quicklist = [{ "src": "http://66.media.tumblr.com/ff7026041c3f67c507adad2c298d92a7/tumblr_ns2sxsI5241uacv0ho1_1280.jpg" },
		# 			{ "src": "http://65.media.tumblr.com/b2a6036e69f2d6b11ab2feb8f54f4081/tumblr_ns4io1WXWC1uacv0ho1_1280.jpg" },
		# 			{ "src": "http://65.media.tumblr.com/266c8a43bacf12c132e5cc8c2802953d/tumblr_ns9v3b8UcQ1uacv0ho1_1280.jpg" },
		# 			{ "src": "http://66.media.tumblr.com/e193bfbddc6b564b25b1234d11de4066/tumblr_nsh9o2lUpn1uacv0ho1_1280.jpg" },
		# 			{ "src": "http://66.media.tumblr.com/751d25c993ab6244ee0361c3bc4e9ca2/tumblr_nt11ubw6Ux1uacv0ho1_1280.jpg" },
		# 			{ "src": "http://66.media.tumblr.com/09494df2a6bdbaad9231d7b3d9be5c86/tumblr_nt8agnIOgI1uacv0ho1_1280.jpg" },
		# 			{ "src": "http://66.media.tumblr.com/7e3b9deaf0bed53eb529e06e40805de5/tumblr_ntqri5b7LO1uacv0ho1_1280.jpg" },
		# 			{ "src": "http://67.media.tumblr.com/b7a8e00cc4a81e33aaf5a43eb2b39b17/tumblr_ntye14dnrA1uacv0ho1_1280.jpg" },
		# 			{ "src": "http://67.media.tumblr.com/e80fc68177962d4237322f9af32d98f4/tumblr_nubxkrVV5E1uacv0ho1_1280.jpg" },
		# 			{ "src": "http://66.media.tumblr.com/65538a528bdb5e4d838b9bfbec04b8b9/tumblr_nuowswpmVL1uacv0ho1_1280.jpg" },
		# 			{ "src": "http://66.media.tumblr.com/260a251c64d49cfd22ffa13582380052/tumblr_nuzu1lCrYS1uacv0ho1_1280.jpg" },
		# 			{ "src": "http://66.media.tumblr.com/65f84ffd7f078bd0c71936c821073aba/tumblr_nvyp9gptW81uacv0ho1_1280.jpg" },]

		#images = quicklist + images
		
		
		for image in images:
			kuva = dict(nimi=None, src=None)
			image["src"] = image["src"].split("?")[0]

			try:
				if image["src"].index("//") == 0:
					image["src"] = "http:{}".format(image["src"])
			except: pass
			try:
				if image["src"].index("./") == 0:
					image["src"] = image["src"].replace("./", "/")
			except: pass
			image["src"] = "{}".format(image["src"].replace("_250.", "_1280."))
			image["src"] = "{}".format(image["src"].replace("_500.", "_1280."))
			kuva["nimi"] = "{}".format(image["src"].split("/")[-1]) # kuvan nimi = tiedoston nimi
			
			kuva["src"] = image["src"]
				
			kuva["filetype"] = "{}".format(image["src"].split(".")[-1])

			found = self.sessio.query(Strippi).filter(
						Strippi.sarjakuva_id == self.sarjakuva.id,
						Strippi.url == image["src"]
					).first()

			if not found:
				kuvat.append(kuva)
			
		#print(len(kuvat))
		return kuvat

		
		
	def Next(self):
		return None
	# def Next(self):
	# 	ret = self.urli
	# 	try:

	# 		link = self.soup.find("a", {"class": "forward"})
	# 		if not link:
	# 			link = self.soup.find("a", {"class": "forward_dark"})
		
	# 		tmp = self.urli.split("/")

	# 		if "://" in link["href"]:
	# 			ret = link["href"]
	# 		else:
	# 			if "../" in link["href"]:
	# 				link["href"] = link["href"].replace("../", "")
	# 				tmp = tmp[:-1]
	# 			tmp[-1] = link["href"]

	# 			ret = "/".join(tmp)
			
	# 	except: pass

	# 	if ret == self.urli or not "/comic/" in ret:
	# 		return None
		
	# 	return ret

