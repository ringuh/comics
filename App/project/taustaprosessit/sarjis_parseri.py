# -*- coding: utf-8 -*-
from project import db, app, Print, Log
from bs4 import BeautifulSoup
from project.models import Sarjakuva as SK, Strippi
import datetime, urllib, os, requests, hashlib
from project.luokat import *
import sys
from multiprocessing.dummy import Pool as ThreadPool


def run():
	sarjakuvat = db.session.query(SK).order_by(SK.id).all()
	pool = ThreadPool(3)
	pool.map(Looper, list([i.id for i in sarjakuvat]))

	return True


def Looper(id):
	try:
		from sqlalchemy import create_engine
		from sqlalchemy.orm import sessionmaker, scoped_session
		
		db_engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"], echo=False)
		sessio = scoped_session(
		    sessionmaker(
		        autoflush=True,
		        autocommit=False,
		        bind=db_engine
		    )
		)

		comic = sessio.query(SK).get(id)

		if "parseri" in sys.argv:
			
			if comic.parseri != sys.argv[3]:
				return
		elif "id" in sys.argv:
			if comic.id != int(sys.argv[3]):
				return
		else:
			if not "force" in sys.argv:
				if comic.last_parse is not None:
					if comic.last_parse + datetime.timedelta(hours=comic.interval) > datetime.datetime.now():
						return False
				# interval 0 == loppunut
				if comic.interval == 0:
					return False

		
		Print("----\n")
		Print(comic.nimi)
		
		olio = None
		if comic.parseri == u"oglaf":
			olio = Oglaf(comic)
		elif comic.parseri == u"fingerpori":
			olio = Fingerpori(comic)
		elif comic.parseri == u"rosiannarabbit":
			olio = Rosianna(comic)
		elif comic.parseri == u"dorkly":
			olio = Dorkly(comic)
		elif comic.parseri == u"oots":
			olio = OrderOfTheStick(comic)

		else:
			olio = Sarjis(comic)

		last_url = comic.last_url
		count = 0
		while last_url is not None:
			count += 1

			last_url = olio.Loop(last_url, sessio)
			
			if last_url is None:
				Log(comic.id, None, u"Haku päättyi", count)
			
			if("short" in sys.argv and count > 2) or count > 5: # ei ikilooppeja
				return False

		return True
	except Exception, e:
		Log(id, None, u"Looppi epäonnistui", e.message)
		return False

