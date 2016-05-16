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
		test="http://oglaf.com/twostars/",

		tags="#strip", # tags
		next="#nav>a|#nx",
		weekday="6,0", # haetaan korkeintaan näinä viikonpäivinä
		
	),
	Sarjakuva(
		"Fingerpori", #nimi
		"fingerpori", # lyhenne
		
		"http://www.hs.fi", # baseurl
		"http://www.hs.fi/fingerpori/s1349775187323",
		test="http://www.hs.fi/fingerpori/s1306040940065",

		tags="#full-comic>img",
		next="a.next-cm",
		ext="jpg",
	),
	Sarjakuva(
		"Wiivi ja Wagner", #nimi
		"wiivijawagned", # lyhenne
		"http://www.hs.fi", # baseurl
		"http://www.hs.fi/viivijawagner/s1349773144978",
		test="http://www.hs.fi/viivijawagner/s1306041112180",

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
		"Jäätävä spede", #nimi
		"spede", # lyhenne
		"http://www.hs.fi", # baseurl
		"http://www.hs.fi/jaatavaspede/s1305997430512",
		test="http://www.hs.fi/jaatavaspede/s1306037906288",
		
		tags="#full-comic>img",
		next="a.next-cm",
		ext="jpg",
		weekday="0,6",
	),


	Sarjakuva(
		"Rosianna Rabbit", #nimi
		"rosiannarabbit", 		
		"http://rosiannarabbit.com", # baseurl
		"http://rosiannarabbit.com/post/131180644576",
		test="http://rosiannarabbit.com/post/143122075580/",

		tags="article>figure>img",
		next="nav.comic-pagination>a.next-button",
	),

	Sarjakuva(
		"Justice League 8", 
		"justiceleague8", 
		"http://jl8comic.tumblr.com", 
		"http://jl8comic.tumblr.com/post/13372482444/jl8-1-by-yale-stewart-based-on-characters-in-dc",
		test="http://jl8comic.tumblr.com/post/142267512776/",

		tags="article>figure>img",
		next="nav.comic-pagination>a.next-button",
	),

	Sarjakuva(
		"Dire Circumstances", 
		"dire",
		"http://fruitscs.tumblr.com", 
		"http://fruitscs.tumblr.com/post/117225884584",
		test="http://fruitscs.tumblr.com/post/143199707004",

		tags="article>figure>img",
		next="nav.comic-pagination>a.next-button",
	),

	Sarjakuva(
		"nellucnhoj", 
		"nellucnhoj", 

		"http://nellucnhoj.com", 
		"http://nellucnhoj.com/post/72259187580/back-in-2010-i-decided-to-punish-myself-by-doing",
		test="http://nellucnhoj.com/post/144203005681/",

		tags="article>figure>img",
		next="nav.comic-pagination>a.next-button",
	),


	Sarjakuva(
		"The Order of the Stick", #nimi
		"oots", # lyhenne		
		"http://www.giantitp.com", # baseurl
		"http://www.giantitp.com/comics/oots0001.html", # 96
		test="http://www.giantitp.com/comics/oots1034.html",

		tags="img|!src:in:/comics/images/",
		next="a|img|!title:=:next comic",
	),

	Sarjakuva(
		"Toonhole", #nimi
		"toonhole", # lyhenne
		
		"http://toonhole.com", # baseurl
		"http://toonhole.com/2010/01/smart-questions-get-smart-answers/", # 96
		test="http://toonhole.com/2016/05/dallas-t-washington-pages-8-9/",
		
		tags="#comic>img",
		next="a|!rel:in:next",
		weekday="0,2,4", # haetaan korkeintaan näinä viikonpäivinä
	),

	Sarjakuva(
		"xkcd", 
		"xkcd", 
		
		"http://xkcd.com", 
		"http://xkcd.com/1670/",

		tags="#comic>img",
		next="a|!rel:in:next",
	),

	Sarjakuva(
		"Nedroid", 
		"nedroid", 

		"http://nedroid.com", 
		"http://nedroid.com/2016/02/birthdayto/",

		tags="#comic>img",
		next="a|!rel:in:next",

	),

	Sarjakuva(
		"Scandinavia and the World", #nimi
		"satw", # lyhenne
		
		"http://satwcomic.com", # baseurl
		"http://satwcomic.com/sweden-denmark-and-norway", # 96
		test="http://satwcomic.com/hatee-hatee-hatee-ho",

		tags="center>img|!src:in:/art/",
		next="a|!accesskey:in:n",
	),

	Sarjakuva(
		"Cyanide and Happiness", #nimi
		"explosm", # lyhenne

		"http://explosm.net", # baseurl
		"http://explosm.net/comics/15", # 
		test="http://explosm.net/comics/4299/",

		tags="#main-comic",
		next="a.next-comic",
	),

	Sarjakuva(
		"Paintrain", #nimi
		"paintrain", # lyhenne
		
		"http://paintraincomic.com",  # baseurl
		"http://paintraincomic.com/comic/romance/",
		test="http://paintraincomic.com/comic/sign-language/",

		tags="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		u"Garfield", 
		u"garfield",

		u"http://garfield.com/comic", 
		u"http://garfield.com/comic/2016-02-01",
		test="https://garfield.com/comic/2016/05/14",

		tags=".comic>img",
		next="a.comic-arrow-right",
	),

	Sarjakuva(
		u"Calvin and Hobbes", 
		u"calvinandhobbes",

		u"http://www.gocomics.com/", 
		u"http://www.gocomics.com/calvinandhobbes/2014/06/13",
		test="http://www.gocomics.com/calvinandhobbes/2016/05/14",

		tags="img.strip",
		next="ul.feature-nav>a.next",
	),

	Sarjakuva(
		u"The Flying MCCoys", 
		u"mccoys",

		"http://www.gocomics.com/", 
		"http://www.gocomics.com/theflyingmccoys/2016/05/14",
		test="http://www.gocomics.com/theflyingmccoys/2016/05/14",
		tags="img.strip",
		next="ul.feature-nav>a.next",
	),
	Sarjakuva(
		u"Pearls Before Swine", 
		u"pearls",

		"http://www.gocomics.com/", 
		"http://www.gocomics.com/pearlsbeforeswine/2016/05/14",
		test="http://www.gocomics.com/pearlsbeforeswine/2016/05/14",
		tags="img.strip",
		next="ul.feature-nav>a.next",
	),
	Sarjakuva(
		u"9 Chickweed Lane", 
		u"9chickweedlane",

		u"http://www.gocomics.com/", 
		u"http://www.gocomics.com/9chickweedlane/2016/05/14",
		test="http://www.gocomics.com/9chickweedlane/2016/05/14",
		tags="img.strip",
		next="ul.feature-nav>a.next",
	),

	Sarjakuva(
		u"Jim Benton", 
		u"jimbenton",

		"http://www.gocomics.com/", 
		"http://www.gocomics.com/jim-benton-cartoons/2014/10/27",
		test="http://www.gocomics.com/jim-benton-cartoons/2016/05/11",
		tags="img.strip",
		next="ul.feature-nav>a.next",
	),
	Sarjakuva(
		u"Over the Hedge", 
		u"overthehedge", 

		"http://www.gocomics.com/", 
		"http://www.gocomics.com/overthehedge/2016/05/14",
		test="http://www.gocomics.com/overthehedge/2016/05/14",
		tags="img.strip",
		next="ul.feature-nav>a.next",
	),
	Sarjakuva(
		u"Sunny Street",
		u"sunnystreet",
		
		"http://www.gocomics.com/", 
		"http://www.gocomics.com/sunny-street/2016/02/18",
		test="http://www.gocomics.com/sunny-street/2016/05/02",
		tags="img.strip",
		next="ul.feature-nav>a.next",
	),

	Sarjakuva(
		"Ctrl+Alt+Del", #nimi
		"cad", # lyhenne
		
		"http://www.cad-comic.com", # baseurl
		"http://www.cad-comic.com/cad/20021023", # 
		test="http://www.cad-comic.com/cad/20160511",

		tags="#content>img|!src:in:comics",
		next="a.nav-next",
		ending="cad",
	),

		Sarjakuva(
		"Dragonarte", #nimi
		"dragonarte", # lyhenne
		
		
		"http://dragonarte.com.br",  # baseurl
		"http://dragonarte.com.br/admin/tirinhas/",
		parseri="dragonarte", # parseri
		test="http://pienirinkula.com",
	),

	Sarjakuva(
		"Completely Normal People", 
		"completelynormal",

		"http://completelynormalpeople.com", 
		"http://completelynormalpeople.com/images/toons/",
		test="http://pienirinkula.com",
		parseri="dragonarte", # parseri
	),

	Sarjakuva(
		"Avas Demon", 
		"avasdemon",

		"http://www.avasdemon.com/", 
		"http://www.avasdemon.com/chapters.php",
		test="http://pienirinkula.com",
		parseri="avasdemon", # parseri
	),


	# hiveworks
	Sarjakuva( 
		u"The Rock Cocks", 
		u"rockcocks", 
		
		u"http://www.therockcocks.com", 
		u"http://www.therockcocks.com/comic/page-1-nsfw-track-1-start",
		test="http://www.therockcocks.com/comic/page-176",

		tags="#cc-comicbody>img",
		next="div.nav>a.next",
	),


	# END OF HIVEWORKS

	Sarjakuva(
		"Hamlet's Danish", 
		"hamlet",

		"http://clayyount.com/", 
		"http://clayyount.com/hamlets-danish-comic/2014/4/7/one-question",
		test="http://clayyount.com/hamlets-danish-comic/2015/9/14/lies-damn-lies-and-statistics",

		tags="div.intrinsic>img",
		next="a.next-btn",
	),

	Sarjakuva( 
		"Dilbert", 
		"dilbert",

		"http://dilbert.com", 
		"http://dilbert.com/strip/2015-01-11",
		test="http://dilbert.com/strip/2016-05-13",
		tags="img.img-comic",
		next="div.nav-right>a|!title:in:next",
	),


	Sarjakuva( 
		"The Perry Bible Fellowship", 
		"perrybible",

		"http://pbfcomics.com", 
		"http://pbfcomics.com/1/",
		test="http://pbfcomics.com/273",
		tags="#topimg",
		next="a|img|!src:in:newer",
		
	),
	Sarjakuva( 
		"Rational Comics", 
		"rational",

		"http://www.rationalcomics.com", 
		"http://www.rationalcomics.com/001-mountain-moving-man/",
		test="http://www.rationalcomics.com/058-the-customer-is-the-most-important-visitor/",
		tags="figure.post-image>img",
		next="a|!rel:in:next",		
	),
	Sarjakuva( 
		"Loading Artist", 
		"loadingartist",

		"http://www.loadingartist.com", 
		"http://www.loadingartist.com/comic/born/",
		test="http://www.loadingartist.com/comic/punstoppable-punishment/",
		tags="div.comic>div.comic>img",
		next="a.next",
				
	),

	Sarjakuva( 
		"Saturday Morning Breakfast Cereal", 
		"smbc",

		"http://www.smbc-comics.com", 
		"http://www.smbc-comics.com/index.php?id=4100",
		test="http://www.smbc-comics.com/index.php?id=4109",
		tags="#comic",
		next="a.next",
		download=True,		
	),

	Sarjakuva(
		"Its the Tie", 
		"itsthetie",
		
		"http://itsthetie.com/", 
		"http://itsthetie.com/?comic=no-world-for-a-squirrel-4",
		test="http://itsthetie.com/comic/global-warming/",
		tags="div.comic-content>img.size-full",
		next="a|!rel:in:next",	
	),

]
count = db.session.query(Sarjakuva).count()
for i in content:
	found = db.session.query(Sarjakuva).filter(Sarjakuva.lyhenne == i.lyhenne).first()
	if not found:
		count += 1
		Print(count, i.nimi)
		db.session.add(i)
		

db.session.commit()


#http://www.pixietrixcomix.com/
#http://www.strawberrycomics.com/