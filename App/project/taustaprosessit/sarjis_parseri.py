# -*- coding: utf-8 -*-
from project import db, app, Print, Log
from bs4 import BeautifulSoup
from project.models import Sarjakuva as SK, Strippi
import datetime, urllib.request, urllib.parse, urllib.error, os, requests, hashlib
from project.luokat import *
import sys
from multiprocessing.dummy import Pool as ThreadPool
#from sqlalchemy.pool import NullPool


def run():
	sarjakuvat = db.session.query(SK).order_by(SK.id).all()
	pool = ThreadPool(3)
	pool.map(Looper, list([i.id for i in sarjakuvat]))
	
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

		if "parseri" in sys.argv:
			
			if comic.parseri != sys.argv[3]:
				sessio.close()
				return False
		elif "id" in sys.argv:
			if comic.id != int(sys.argv[3]):
				sessio.close()
				return False
			f = open("logit/loki{}.tmp".format(comic.id), "w+")
			f.write("")
			f.close()
		else:
			if not "force" in sys.argv:
				# interval 0 == loppunut
				if comic.interval == 0:
					sessio.close()
					return False

				if comic.weekday:
					try: 
						days = [int(i.strip()) for i in comic.weekday.split(",")]
						today = datetime.datetime.now()
						if not today.weekday() in days:
							sessio.close()
							return False

					except: pass

				if comic.last_parse is not None:
					if comic.last_parse + datetime.timedelta(hours=comic.interval) > datetime.datetime.now():
						sessio.close()
						return False
				

		Print("----\n")
		Print(comic.id, comic.nimi)
		
		
		olio = None
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
		else:
			olio = Sarjis(comic)

		last_url = comic.last_url
		count = 0
		while last_url is not None:
			count += 1

			last_url = olio.Loop(last_url, sessio)
			
			if last_url is None:
				Log(comic.id, None, "Haku päättyi", count)
				break
			
			if("short" in sys.argv and count > 2) or count > 5: # ei ikilooppeja
				return False
		
		sessio.close()

		return True
	except Exception as e:
		Log(id, None, "Looppi epäonnistui", e)
		sessio.close()
		return False
	return True

# if comic.parseri == "oglaf":
		# 	olio = Oglaf(comic)
		# elif comic.parseri == "fingerpori":
		# 	olio = Fingerpori(comic)
		# elif comic.parseri == "rosiannarabbit":
		# 	olio = Rosianna(comic)
		# elif comic.parseri == "dorkly":
		# 	olio = Dorkly(comic)
		# elif comic.parseri == "oots":
		# 	olio = OrderOfTheStick(comic)
		# elif comic.parseri == "toonhole":
		# 	olio = Toonhole(comic)
		# elif comic.parseri == "satw":
		# 	olio = SatW(comic)
		# elif comic.parseri == "cad":
		# 	olio = CtrlAltDel(comic)
		# elif comic.parseri == "explosm":
		# 	olio = Explosm(comic)
		# elif comic.parseri == "dragonarte":
		# 	olio = Dragonarte(comic)
		# elif comic.parseri == "avasdemon":
		# 	olio = AvasDemon(comic)
		# elif comic.parseri == "paintrain":
		# 	olio = Paintrain(comic)
		# cheerup saattaa puuttua kuva, odd1s out saattaa puuttua kuva
		# elif comic.parseri == "gunshow":
		# 	olio = Gunshow(comic)
		# elif comic.parseri == "happletea":
		# 	olio = HappleTea(comic)
		# elif comic.parseri == "vgcats":
		# 	olio = VGCats(comic)
		# elif comic.parseri == "nerfnow":
		# 	olio = NerfNow(comic)
		# elif comic.parseri == "sinfest":
		# 	olio = Sinfest(comic)
		# elif comic.parseri == "camp":
		# 	olio = Camp(comic)
		# elif comic.parseri == "pennyarcade":
		# 	olio = PennyArcade(comic)
		# elif comic.parseri == "pidjin":
		# 	olio = Pidjin(comic)
		# elif comic.parseri == "garfield":
		# 	olio = Garfield(comic)
			# issues with us acres, ok?
		# elif comic.parseri == "leasticoulddo":
		# 	olio = LeastICouldDo(comic)
		# elif comic.parseri == "questionablecontent":
		# 	olio = QuestionableContent(comic)
		# elif comic.parseri == "wumo":
		# 	olio = Wumo(comic)
		# elif comic.parseri == "gocomics":
		# 	olio = GoComics(comic)
		# sunny street kusee
		# elif comic.parseri == "hiveworks":
		# 	olio = HiveWorks(comic)
		# elif comic.parseri == "floabc":
		# 	olio = Floabc(comic)
		# 	# fixed?
		# elif comic.parseri == "hamlet":
		# 	olio = HamletsDanish(comic)
		# elif comic.parseri == "interrobang":
		# 	# fixed?
		# 	olio = InterroBang(comic)
		# elif comic.parseri == "dilbert":
		# 	olio = Dilbert(comic)
		# elif comic.parseri == "perrybible":
		# 	olio = PerryBible(comic)
		# elif comic.parseri == "rational":
		# 	olio = Rational(comic)
		# elif comic.parseri == "loadingartist":
		# 	olio = LoadingArtist(comic) 
		# 	# fixed ?
		# elif comic.parseri == "smbc":
		# 	olio = SMBC(comic)
		# 	#fixed? http://www.smbc-comics.com/index.php?id=3846
		# elif comic.parseri == "itsthetie":
		# 	olio = ItsTheTie(comic)
		# 	# fixed?
		# elif comic.parseri == "nerdrage":
		# 	olio = NerdRage(comic)
		# elif comic.parseri == "tubeytoons":
		# 	olio = TubeyToons(comic)
		# elif comic.parseri == "darklegacy":
		# 	olio = DarkLegacy(comic)
		# elif comic.parseri == "pvponline":
		# 	olio = PVPOnline(comic)
		# elif comic.parseri == "userfriendly":
		# 	olio = UserFriendly(comic)
		# elif comic.parseri == "grog":
		# 	olio = Grog(comic)
		# elif comic.parseri == "vattu":
		# 	olio = Vattu(comic)
		# elif comic.parseri == "powernap":
		# 	olio = PowerNap(comic)
		# # parseri jumii
		# elif comic.parseri == "extralife":
		# 	olio = ExtraLife(comic)
		# elif comic.parseri == "poorlydrawnlines":
		# 	olio = PoorlyDrawnLines(comic)
		# elif comic.parseri == "existential":
		# 	olio = Existential(comic)
		# elif comic.parseri == "abominable":
		# 	olio = Abominable(comic)
		# elif comic.parseri == "ma3":
		# 	olio = Ma3(comic)
		# elif comic.parseri == "blastwave":
		# 	olio = Blastwave(comic)
		# elif comic.parseri == "standstill":
		# 	olio = StandStill(comic)
		# elif comic.parseri == "romanticallyapocalyptic":
		# 	olio = RomanticallyApocalyptic(comic)
		# elif comic.parseri == "downtheupwardspiral":
		# 	olio = DownTheUpwardSpiral(comic)

		# elif comic.parseri == "thingsinsquares":
		# 	olio = ThingsInSquares(comic)
		# elif comic.parseri == "berdsandnerds":
		# 	olio = BerdsAndNerds(comic)
		# elif comic.parseri == "pepperandcarrot":
		# 	olio = PepperAndCarrot(comic)
		# elif comic.parseri == "catsu":
		# 	olio = Catsu(comic)
		# elif comic.parseri == "unsounded":
		# 	olio = Unsounded(comic)
		# elif comic.parseri == "deathbulge":
		# 	olio = Deathbulge(comic)
		# elif comic.parseri == "webtoons":
		# 	olio = Webtoons(comic)

		# elif comic.parseri == "grog":
		# 	olio = Grog(comic)
		# elif comic.parseri == "grog":
		# 	olio = Grog(comic)
		# elif comic.parseri == "grog":
		# 	olio = Grog(comic)
		# elif comic.parseri == "grog":
		# 	olio = Grog(comic)
		# elif comic.parseri == "grog":
		# 	olio = Grog(comic)
		