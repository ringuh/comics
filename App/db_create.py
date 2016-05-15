# -*- coding: utf-8 -*-
# windows console koment: chcp 65001
from project import app, db, Print
import random, datetime, sys, os
from project.models import *
from project.luokat import *

if "create" in sys.argv:
	db.drop_all()
	db.create_all()
	db.session.flush()
	db.session.commit()
	u = User("ringuh", "zerg", True)
	db.session.add(u)

	db.session.add(User("vieras", "vieras"))

	polku = os.path.join(app.config["SARJAKUVA_FOLDER"], "x")
	dir = os.path.dirname(polku) 
	try: os.stat(dir)
	except: os.mkdir(dir)

# sarjikset
content = [
	Sarjakuva(
		"Oglaf", #nimi
		"oglaf", # lyhenne
		
		"http://oglaf.com", # baseurl
		"http://oglaf.com/cumsprite/",

		tags="#strip", # tags
		next="#nav>a|#nx",
		weekday="6,0", # haetaan korkeintaan näinä viikonpäivinä
		
	),
	Sarjakuva(
		"Fingerpori", #nimi
		"fingerpori", # lyhenne
		
		"http://www.hs.fi", # baseurl
		"http://www.hs.fi/fingerpori/s1349775187323",
		tags="#full-comic>img",
		next="a.next-cm",
		ext="jpg",
	),
	Sarjakuva(
		"Wiivi ja Wagner", #nimi
		"wiivijawagned", # lyhenne
		"http://www.hs.fi", # baseurl
		"http://www.hs.fi/viivijawagner/s1349773144978",
		tags="#full-comic>img",
		next="a.next-cm",
		ext="jpg",
	),

	Sarjakuva(
		"Karlsson", 
		"karlsson",
		"http://www.hs.fi", 
		"http://www.hs.fi/karlsson/s1305951536460",
		tags="#full-comic>img",
		next="a.next-cm",
		ext="jpg",
	),
	Sarjakuva(
		"Rosianna Rabbit", #nimi
		"rosiannarabbit", 		
		"http://rosiannarabbit.com", # baseurl
		"http://rosiannarabbit.com/post/131180644576",
		tags="article>figure>img",
		next="nav.comic-pagination>a.next-button",
	),

	Sarjakuva(
		"Justice League 8", 
		"justiceleague8", 
		"http://jl8comic.tumblr.com", 
		"http://jl8comic.tumblr.com/post/13372482444/jl8-1-by-yale-stewart-based-on-characters-in-dc",
		tags="article>figure>img",
		next="nav.comic-pagination>a.next-button",
	),

	Sarjakuva(
		"Dire Circumstances", 
		"dire",
		"http://fruitscs.tumblr.com", 
		"http://fruitscs.tumblr.com/post/117225884584",

		tags="article>figure>img",
		next="nav.comic-pagination>a.next-button",
	),

	Sarjakuva(
		"nellucnhoj", 
		"nellucnhoj", 

		"http://nellucnhoj.com", 
		"http://nellucnhoj.com/post/72259187580/back-in-2010-i-decided-to-punish-myself-by-doing",
		tags="article>figure>img",
		next="nav.comic-pagination>a.next-button",
	),


	Sarjakuva(
		"The Order of the Stick", #nimi
		"oots", # lyhenne		
		"http://www.giantitp.com", # baseurl
		"http://www.giantitp.com/comics/oots0001.html", # 96

		tags="img|!src:in:/comics/images/",
		next="a|img|!title:=:next comic",
	),

	Sarjakuva(
		"Toonhole", #nimi
		"toonhole", # lyhenne
		
		"http://toonhole.com", # baseurl
		"http://toonhole.com/2010/01/smart-questions-get-smart-answers/", # 96
		
		tags="#comic>img",
		next="a|!rel:in:next",
		weekday="0,2,4", # haetaan korkeintaan näinä viikonpäivinä
	),

	Sarjakuva(
		"xkcd", 
		"xkcd", 
		
		"http://xkcd.com", 
		"http://xkcd.com/1500/",

		tags="#comic>img",
		next="a|!rel:in:next",
	),

	Sarjakuva(
		"Nedroid", 
		"nedroid", 

		"http://nedroid.com", 
		"http://nedroid.com/2015/04/gobs/",

		tags="#comic>img",
		next="a|!rel:in:next",

	),

	Sarjakuva(
		"Scandinavia and the World", #nimi
		"satw", # lyhenne
		
		"http://satwcomic.com", # baseurl
		"http://satwcomic.com/sweden-denmark-and-norway", # 96

		tags="center>img|!src:in:/art/",
		next="a|!accesskey:in:n",
	),

	Sarjakuva(
		"Cyanide and Happiness", #nimi
		"explosm", # lyhenne

		"http://explosm.net", # baseurl
		"http://explosm.net/comics/15", # 

		tags="#main-comic",
		next="a.next-comic",
	),

	Sarjakuva(
		"Paintrain", #nimi
		"paintrain", # lyhenne
		
		"http://paintraincomic.com",  # baseurl
		"http://paintraincomic.com/comic/romance/",

		tags="#comic-page>img",
		next="a.comic-nav-next",
	),


]

for i in content:
	found = db.session.query(Sarjakuva).filter(Sarjakuva.lyhenne == i.lyhenne).first()
	if not found:
		Print(i.nimi)
		db.session.add(i)

db.session.commit()


#http://www.pixietrixcomix.com/
#http://www.strawberrycomics.com/