# -*- coding: utf-8 -*-
from project import db, app, Print, Log
from bs4 import BeautifulSoup
from project.models import Sarjakuva as SK, Strippi
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat import *
import sys
#from multiprocessing import Pool
#from sqlalchemy.pool import NullPool

def run():
	sarjakuvat = db.session.query(SK).order_by(SK.id).all()
	#pool = Pool(processes=2)
	#pool.map(Looper, list([i.id for i in sarjakuvat]))
	for comic in sarjakuvat:
		if "parseri" in sys.argv:
			if comic.parseri != sys.argv[3]:
				continue
		elif "id" in sys.argv:
			tmp_id = sys.argv[3].split("-")
			if comic.id < int(tmp_id[0]) or comic.id > int(tmp_id[-1]):
				continue
			f = open("logit/loki{}.tmp".format(comic.id), "w+")
			f.write("")
			f.close()
		else:
			if not "force" in sys.argv:
				# interval 0 == loppunut
				if comic.interval == 0:
					continue

				if comic.weekday:
					try: 
						days = [int(i.strip()) for i in comic.weekday.split(",")]
						today = datetime.datetime.now()
						if not today.weekday() in days:
							continue

					except: pass

				if comic.last_parse is not None:
					if comic.last_parse + datetime.timedelta(hours=comic.interval) > datetime.datetime.now():
						continue

		Looper(comic.id)
	return True


def Looper(id):
	try:
		from sqlalchemy import create_engine
		from sqlalchemy.orm import sessionmaker, scoped_session
		
		db_engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=False)#, poolclass=NullPool)
		sessio = scoped_session(
		    sessionmaker(
		        autoflush=True,
		        autocommit=False,
		        bind=db_engine
		    )
		)

		comic = sessio.query(SK).get(id)
				

		Print("----\n")
		Print(comic.id, comic.nimi, comic.parseri)
		
		
		olio = Sarjis(comic)
		if comic.parseri:
			if comic.parseri == "dragonarte":
				olio = Dragonarte(comic)
			elif comic.parseri == "avasdemon":
				olio = AvasDemon(comic)
			elif comic.parseri == "dorkly":
				olio = Dorkly(comic)
			elif comic.parseri == "tubeytoons":
				olio = TubeyToons(comic)
			elif comic.parseri == "standstill":
				olio = StandStill(comic)
			elif comic.parseri == "downtheupwardspiral":
				olio = DownTheUpwardSpiral(comic)
			elif comic.parseri == "catsu":
				olio = Catsu(comic)
			elif comic.parseri.lower() == "unsounded":
				olio = Unsounded(comic)
			elif comic.parseri.lower() == "TumblrIframe".lower():
				olio = TumblrIframe(comic)
			elif comic.parseri.lower() == "RSSReader".lower():
				olio = RSSReader(comic)


		last_url = comic.last_url
		count = 0
		while last_url is not None:
			count += 1

			last_url = olio.Loop(last_url, sessio)
			
			if last_url is None:
				Log(comic.id, None, "Haku päättyi", count)
				break
			
			if("short" in sys.argv and count > 2) or count > app.config["MAX_QUERY"]: # ei ikilooppeja
				return False
		
		sessio.close()

		return True
	except Exception as e:
		Log(id, None, "Looppi epäonnistui", e)
		sessio.close()
		return False
	return True

