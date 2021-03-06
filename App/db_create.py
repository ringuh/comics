# -*- coding: utf-8 -*-
# windows console koment: chcp 65001
from project import app, db, Print
import random, datetime, sys, os
from project.models import *
from project.luokat import *

if "create" in sys.argv and sys.platform == "win32":
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

		image="#strip", # tags
		next="#nav>a|#nx",
		weekday="6,0", # haetaan korkeintaan näinä viikonpäivinä
		
	),
	Sarjakuva(
		"Fingerpori", #nimi
		"fingerpori", # lyhenne
		
		"http://www.hs.fi", # baseurl
		"http://www.hs.fi/fingerpori/s1349775187323",
		test="http://www.hs.fi/fingerpori/s1306040940065",

		image="#full-comic>img",
		next="a.next-cm",
		ext="jpg",
	),
	Sarjakuva(
		"Wiivi ja Wagner", #nimi
		"wiivijawagner", # lyhenne
		"http://www.hs.fi", # baseurl
		"http://www.hs.fi/viivijawagner/s1349773144978",
		test="http://www.hs.fi/viivijawagner/s1306041112180",

		image="#full-comic>img",
		next="a.next-cm",
		ext="jpg",
	),

	Sarjakuva(
		"Karlsson", 
		"karlsson",
		"http://www.hs.fi", 
		"http://www.hs.fi/karlsson/s1305951536460",
		image="#full-comic>img",
		next="a.next-cm",
		ext="jpg",
	),

	Sarjakuva(
		"Jäätävä spede", #nimi
		"spede", # lyhenne
		"http://www.hs.fi", # baseurl
		"http://www.hs.fi/jaatavaspede/s1305997430512",
		test="http://www.hs.fi/jaatavaspede/s1306037906288",
		
		image="#full-comic>img",
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

		image="article>figure>img",
		next="nav.comic-pagination>a.next-button",
	),

	Sarjakuva(
		"Justice League 8", 
		"justiceleague8", 
		"http://jl8comic.tumblr.com", 
		"http://jl8comic.tumblr.com/post/13372482444/jl8-1-by-yale-stewart-based-on-characters-in-dc",
		test="http://jl8comic.tumblr.com/post/142267512776/",

		image="article>figure>img",
		next="nav.comic-pagination>a.next-button",
	),

	Sarjakuva(
		"Dire Circumstances", 
		"dire",
		"http://fruitscs.tumblr.com", 
		"http://fruitscs.tumblr.com/post/117225884584",
		test="http://fruitscs.tumblr.com/post/143199707004",

		image="article>figure>img",
		next="nav.comic-pagination>a.next-button",
	),

	Sarjakuva(
		"nellucnhoj", 
		"nellucnhoj", 

		"http://nellucnhoj.com", 
		"http://nellucnhoj.com/post/72259187580/back-in-2010-i-decided-to-punish-myself-by-doing",
		test="http://nellucnhoj.com/post/144203005681/",

		image="article>figure>img",
		next="nav.comic-pagination>a.next-button",
	),


	Sarjakuva(
		"The Order of the Stick", #nimi
		"oots", # lyhenne		
		"http://www.giantitp.com", # baseurl
		"http://www.giantitp.com/comics/oots0001.html", # 96
		test="http://www.giantitp.com/comics/oots1034.html",

		image="img|!src:in:/comics/images/",
		next="a|img|!title:=:next comic",
	),

	Sarjakuva(
		"Toonhole", #nimi
		"toonhole", # lyhenne
		
		"http://toonhole.com", # baseurl
		"http://toonhole.com/2010/01/smart-questions-get-smart-answers/", # 96
		test="http://toonhole.com/2016/05/dallas-t-washington-pages-8-9/",
		
		image="#comic>img",
		next="a|!rel:in:next",
		weekday="0,2,4", # haetaan korkeintaan näinä viikonpäivinä
	),

	Sarjakuva(
		"xkcd", 
		"xkcd", 
		
		"http://xkcd.com", 
		"http://xkcd.com/1670/",

		image="#comic>img",
		next="a|!rel:in:next",
	),

	Sarjakuva(
		"Nedroid", 
		"nedroid", 

		"http://nedroid.com", 
		"http://nedroid.com/2016/02/birthdayto/",

		image="#comic>img",
		next="a|!rel:in:next",

	),

	Sarjakuva(
		"Scandinavia and the World", #nimi
		"satw", # lyhenne
		
		"http://satwcomic.com", # baseurl
		"http://satwcomic.com/sweden-denmark-and-norway", # 96
		test="http://satwcomic.com/hatee-hatee-hatee-ho",

		image="center>img|!src:in:/art/",
		next="a|!accesskey:in:n",
	),

	Sarjakuva(
		"Cyanide and Happiness", #nimi
		"explosm", # lyhenne

		"http://explosm.net", # baseurl
		"http://explosm.net/comics/15", # 
		test="http://explosm.net/comics/4299/",

		image="#main-comic",
		next="a.next-comic",
	),

	Sarjakuva(
		"Paintrain", #nimi
		"paintrain", # lyhenne
		
		"http://paintraincomic.com",  # baseurl
		"http://paintraincomic.com/comic/romance/",
		test="http://paintraincomic.com/comic/sign-language/",

		image="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		u"Garfield", 
		u"garfield",

		u"http://garfield.com/comic", 
		u"http://garfield.com/comic/2016-02-01",
		test="https://garfield.com/comic/2016/05/14",

		image=".comic>img",
		next="a.comic-arrow-right",
	),

	Sarjakuva(
		u"Calvin and Hobbes", 
		u"calvinandhobbes",

		u"http://www.gocomics.com/", 
		u"http://www.gocomics.com/calvinandhobbes/2014/06/13",
		test="http://www.gocomics.com/calvinandhobbes/2016/05/14",

		image="img.strip",
		next="ul.feature-nav>a.next",
	),

	Sarjakuva(
		u"The Flying MCCoys", 
		u"mccoys",

		"http://www.gocomics.com/", 
		"http://www.gocomics.com/theflyingmccoys/2016/05/14",
		test="http://www.gocomics.com/theflyingmccoys/2016/05/14",
		image="img.strip",
		next="ul.feature-nav>a.next",
	),
	Sarjakuva(
		u"Pearls Before Swine", 
		u"pearls",

		"http://www.gocomics.com/", 
		"http://www.gocomics.com/pearlsbeforeswine/2016/05/14",
		test="http://www.gocomics.com/pearlsbeforeswine/2016/05/14",
		image="img.strip",
		next="ul.feature-nav>a.next",
	),
	Sarjakuva(
		u"9 Chickweed Lane", 
		u"9chickweedlane",

		u"http://www.gocomics.com/", 
		u"http://www.gocomics.com/9chickweedlane/2016/05/14",
		test="http://www.gocomics.com/9chickweedlane/2016/05/14",
		image="img.strip",
		next="ul.feature-nav>a.next",
	),

	Sarjakuva(
		u"Jim Benton", 
		u"jimbenton",

		"http://www.gocomics.com/", 
		"http://www.gocomics.com/jim-benton-cartoons/2014/10/27",
		test="http://www.gocomics.com/jim-benton-cartoons/2016/05/11",
		image="img.strip",
		next="ul.feature-nav>a.next",
	),
	Sarjakuva(
		u"Over the Hedge", 
		u"overthehedge", 

		"http://www.gocomics.com/", 
		"http://www.gocomics.com/overthehedge/2016/05/14",
		test="http://www.gocomics.com/overthehedge/2016/05/14",
		image="img.strip",
		next="ul.feature-nav>a.next",
	),
	Sarjakuva(
		u"Sunny Street",
		u"sunnystreet",
		
		"http://www.gocomics.com/", 
		"http://www.gocomics.com/sunny-street/2016/02/18",
		test="http://www.gocomics.com/sunny-street/2016/05/02",
		image="img.strip",
		next="ul.feature-nav>a.next",
	),

	Sarjakuva(
		"Ctrl+Alt+Del", #nimi
		"cad", # lyhenne
		
		"http://www.cad-comic.com", # baseurl
		"http://www.cad-comic.com/cad/20021023", # 
		test="http://www.cad-comic.com/cad/20160511",

		image="#content>img|!src:in:comics",
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
		"Down the Upward Spiral", 
		"downtheupwardspiral",
		
		"http://www.downtheupwardspiral.com", 
		"http://www.downtheupwardspiral.com/gallery.html",
		parseri="downtheupwardspiral",
		test="http://pienirinkula.com"
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

		image="#cc-comicbody>img",
		next="div.nav>a.next",
	),


	# END OF HIVEWORKS

	Sarjakuva(
		"Hamlet's Danish", 
		"hamlet",

		"http://clayyount.com/", 
		"http://clayyount.com/hamlets-danish-comic/2014/4/7/one-question",
		test="http://clayyount.com/hamlets-danish-comic/2015/9/14/lies-damn-lies-and-statistics",

		image="div.intrinsic>img",
		next="a.next-btn",
	),

	Sarjakuva( 
		"Dilbert", 
		"dilbert",

		"http://dilbert.com", 
		"http://dilbert.com/strip/2015-01-11",
		test="http://dilbert.com/strip/2016-05-13",
		image="img.img-comic",
		next="div.nav-right>a|!title:in:next",
	),


	Sarjakuva( 
		"The Perry Bible Fellowship", 
		"perrybible",

		"http://pbfcomics.com", 
		"http://pbfcomics.com/1/",
		test="http://pbfcomics.com/273",
		image="#topimg",
		next="a|img|!src:in:newer",
		
	),
	Sarjakuva( 
		"Rational Comics", 
		"rational",

		"http://www.rationalcomics.com", 
		"http://www.rationalcomics.com/001-mountain-moving-man/",
		test="http://www.rationalcomics.com/058-the-customer-is-the-most-important-visitor/",
		image="figure.post-image>img",
		next="a|!rel:in:next",		
	),
	Sarjakuva( 
		"Loading Artist", 
		"loadingartist",

		"http://www.loadingartist.com", 
		"http://www.loadingartist.com/comic/born/",
		test="http://www.loadingartist.com/comic/punstoppable-punishment/",
		image="div.comic>div.comic>img",
		next="a.next",
				
	),

	Sarjakuva( 
		"Saturday Morning Breakfast Cereal", 
		"smbc",

		"http://www.smbc-comics.com", 
		"http://www.smbc-comics.com/index.php?id=4100",
		test="http://www.smbc-comics.com/index.php?id=4109",
		image="#comic",
		next="a.next",
		download=True,		
	),

	Sarjakuva(
		"Its the Tie", 
		"itsthetie",
		
		"http://itsthetie.com/", 
		"http://itsthetie.com/?comic=no-world-for-a-squirrel-4",
		test="http://itsthetie.com/comic/global-warming/",
		image="div.comic-content>img.size-full",
		next="a|!rel:in:next",	
	),

	Sarjakuva(
		"Dorkly", #nimi
		"dorkly", # lyhenne
		
		"http://www.dorkly.com/comics", # baseurl
		"http://www.dorkly.com/comics/page:108", # 96
		test="http://www.dorkly.com/comics/page:2",
		parseri="dorkly",
	),
	# Sarjakuva( uusi content siirtynyt webtoons
	# 	"Merkworks", 
	# 	"merkworks",
		
	# 	"http://www.webtoons.com/en/comedy/mercworks/list?title_no=426",
	# 	"http://www.webtoons.com/en/comedy/mercworks/ep-42-the-passion-of-the-koopa/viewer?title_no=426&episode_no=42",
	# 	test="http://mercworks.net/comicland/sensible-minicomics-i/",
	# 	image="#comic>img",
	# 	next="a.comic-nav-next",
	# 	weekday="0",
	# ),

	Sarjakuva(
		"Evil Inc.", 
		"evilinc",

		"http://evil-inc.com/", 
		"http://evil-inc.com/comic/santa-villain-poem-1/",
		test="http://evil-inc.com/comic/goo-monster/",

		image="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		"Last Place", 
		"lastplace",

		"http://lastplacecomics.com/", 
		"http://lastplacecomics.com/comic/wide-range-of-super-powers/",
		test="http://lastplacecomics.com/comic/final-fantasy-high-school/",

		image="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		"Fowl Language", 
		"fowllanguage",
		
		"http://www.fowllanguagecomics.com/", 
		"http://www.fowllanguagecomics.com/comic/part-of-the-process/",
		test="http://www.fowllanguagecomics.com/comic/bread-crust/",

		image="div.comic>img.main-img",
		next="ul.com-btns>a|!text:in:next",

	),

	Sarjakuva(
		"Looking For Group", 
		"lfg", 

		"http://www.lfg.co/", 
		"http://www.lfg.co/page/1/",
		test="http://www.lfg.co/page/981/",

		image="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		"Non-Player Character", 
		"npc", 
	
		"http://www.lfg.co/", 
		"http://www.lfg.co/npc/tale/1-1/",
		test="http://www.lfg.co/npc/tale/21-9/",

		image="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		"Tiny Dick Adventures", 
		"tinydickadventures", 
	
		"http://www.lfg.co/", 
		"http://www.lfg.co/tda/strip/1/",
		test="http://www.lfg.co/tda/strip/114/",

		image="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		"The Fox Sisters", 
		"foxsisters",
				
		"http://www.thefoxsister.com/", 
		"http://www.thefoxsister.com/index.php?id=1",
		test="http://thefoxsister.com/index.php?id=126",

		image="#comicimg",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		"The Odd 1s Out", 
		"theodd1sout",
		
		"http://theodd1sout.com/", 
		"http://theodd1sout.com/comic/god-its-awful/",
		test="http://theodd1sout.com/comic/my-child/",

		image="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva( 
		"Cheer Up, Emo Kid", 
		"cheerup",
		
		"http://www.cheerupemokid.com", 
		"http://www.cheerupemokid.com/comic/truth",
		test="http://www.cheerupemokid.com/comic/permit",

		image="#comic>img",
		next="a.next",
		#"http://www.cheerupemokid.com/comic/frank",	
	),

	Sarjakuva(
		"Manly Guys Doing Manly Things", 
		"machismo",


		"http://thepunchlineismachismo.com/", 
		"http://thepunchlineismachismo.com/archives/comic/02222010",
		test="http://thepunchlineismachismo.com/archives/comic/2755",
		image="#comic>img",
		next="a.comic-nav-next"
	),

	Sarjakuva( 
		"Commit Strip", 
		"commitstrip",

		"http://www.commitstrip.com/", 
		"http://www.commitstrip.com/en/2012/02/22/interview/",
		test="http://www.commitstrip.com/en/2016/05/12/coder-superpower/",

		image="div.entry-content>img.size-full",
		next="a|!rel:in:next",	
	),

	Sarjakuva(
		"Girls with Slingshots", 
		"girlswithslingshots",

		"http://www.girlswithslingshots.com", 
		"http://www.girlswithslingshots.com/comic/gws-chaser-1",
		test="http://www.girlswithslingshots.com/comic/gws-chaser-307",

		image="#cc-comic",
		next="a.next",
	),

	Sarjakuva( 
		"Strong Female Protagonist", 
		"strongfemaleprotagonist", 
		
		"http://strongfemaleprotagonist.com/", 
		"http://strongfemaleprotagonist.com/issue-1/page-0/",
		test="http://strongfemaleprotagonist.com/issue-6/page-44-5/",
		image="article.post>img.size-full",
		next="a|!rel:in:next",
	),
	Sarjakuva( 
		"Nerd Rage", 
		"nerdrage",

		"http://nerdragecomic.com/", 
		"http://nerdragecomic.com/index.php?date=2010-09-28",
		test="http://nerdragecomic.com/index.php?date=2016-04-22",

		image="img|!src:in:strips",
		next="a|img|!alt:in:next comic",
	),

	Sarjakuva(
		"Tubey Toons", 
		"tubeytoons",
		

		"http://tubeytoons.com/", 
		"http://tubeytoons.com/comic/stay-put",
		test="http://tubeytoons.com/comic/last-wish",
		parseri="tubeytoons",
	),

	Sarjakuva( 
		"Dark Legacy", 
		"darklegacy", 
	
		"http://www.darklegacycomics.com/", 
		"http://www.darklegacycomics.com/1",
		test="http://www.darklegacycomics.com/535",

		image="img.comic-image",
		next="a.nextLink",
		
	),
	Sarjakuva(
		"Awkward Zombie", 
		"awkwardzombie",

		"http://www.awkwardzombie.com/", 
		"http://www.awkwardzombie.com/index.php?page=0&comic=092006",
		test="http://www.awkwardzombie.com/index.php?page=0&comic=041816",

		image="#comic>img",
		next="a|img|!alt:in:next comic",
	),

	Sarjakuva( 
		"Player vs. Player", 
		"pvponline",

		"http://www.pvponline.com/", 
		"http://www.pvponline.com/comic/2015/06/01/birds-of-a-feather1",
		test="http://pvponline.com/comic/2016/05/12/the-one-time",

		image="section.comic-art>img",
		next="div.comic-nav>a.left|!text:in:next",
	),
	Sarjakuva( 
		"Table Titans", 
		"tabletitans",

		"http://tabletitans.com/", 
		"http://tabletitans.com/comic/mines-of-madness-page-1",
		test="http://tabletitans.com/comic/whispers-of-dragons-page-142",

		image="section.comic>img",
		next="a|!text:in:next",
	),
	Sarjakuva( 
		"User Friendly", 
		"userfriendly",

		"http://ars.userfriendly.org", 
		"http://ars.userfriendly.org/cartoons/?id=20160515",
		test="http://ars.userfriendly.org/cartoons/?id=20160515",

		image="img|!alt:in:strip",
		next="area|!alt:in:next",
	),
	Sarjakuva(
		"Grog", 
		"grog",

		"http://www.grogcomics.com", 
		"http://www.grogcomics.com/they-breed-like/",
		test="http://grogcomics.com/did-you-jump/",

		image="div.content>div.entry>img",
		next="span.next>a|!rel:in:next",
	),
	Sarjakuva(
		"Vattu", 
		"vattu", 

		"http://www.rice-boy.com/vattu/", 
		"http://www.rice-boy.com/vattu/index.php?c=001",
		test="http://www.rice-boy.com/vattu/index.php?c=742",

		image="#page>img",
		next="a|!text:in:forward|!href:in:c=",
		ending="index.php"
	),
	Sarjakuva(
		"Power Nap", 
		"powernap",

		"http://www.powernapcomic.com/", 
		"http://www.powernapcomic.com/d/20110617.html",
		test="http://www.powernapcomic.com/d/20160502.html",

		image="center>img|!src:in:/pnap",
		next="a|img|!alt:in:next",	
	),
	Sarjakuva(
		"Extra Life", 
		"extralife",

		"http://www.myextralife.com/", 
		"http://www.myextralife.com/comic/06172001/",
		test="http://www.myextralife.com/comic/whoville/",

		image="img.comic",
		next="a.next_comic_link",
	),
	Sarjakuva( 
		"Poorly Drawn Lines", 
		"poorlydrawnlines",

		"http://poorlydrawnlines.com", 
		"http://poorlydrawnlines.com/comic/campus-characters/",
		test="http://poorlydrawnlines.com/comic/kevins-ideas/",

		image="div.comic>img.size-full",
		next="a|!rel:in:next",
	),
	Sarjakuva(
		"Existential Comics", 
		"Existential Comics", 
		
		"http://existentialcomics.com", 
		"http://existentialcomics.com/comic/1",
		test="http://existentialcomics.com/comic/131",

		image="img.comicImg",
		next="a|img|!src:in:nav_next",
	),
	Sarjakuva(
		"The Abominable", 
		"abominable",

		"http://abominable.cc", 
		"http://abominable.cc/post/44164796353/episode-one",
		test="http://abominable.cc/post/104845340635/guest-strip-magnus-jonason",

		image="div.photo>img",
		next="span.next_post>a",
	),
	

	Sarjakuva(
		"Gone With the Blastwave",  
		"blastwave",

		"http://www.blastwave-comic.com/", 
		"http://www.blastwave-comic.com/index.php?p=comic&nro=1",
		test="http://www.blastwave-comic.com/index.php?p=comic&nro=72",

		image="#comic_ruutu>img|!src:in:/comics/",
		next="a|img|!src:in:next",
	),
	Sarjakuva(
		"Stand Still Stay Silent", 
		"standstill",


		"http://www.sssscomic.com/", 
		"http://www.sssscomic.com/comic.php?page=1",
		test="http://www.sssscomic.com/comic.php?page=520",

		parseri="standstill",
	),
	Sarjakuva(
		"Romantically Apocalyptic", 
		"romanticallyapocalyptic",
	
		"http://romanticallyapocalyptic.com", 
		"http://romanticallyapocalyptic.com/0",
		test="http://romanticallyapocalyptic.com/238",

		image="div.comicpanel>center>img",
		next="a|!accesskey:in:n",
	),
	Sarjakuva(
		"Things In Squares", 
		"thingsinsquares",
		
		"http://www.thingsinsquares.com", 
		"http://www.thingsinsquares.com/comics/lame-joke/",
		test="http://www.thingsinsquares.com/comics/san-pedro-cactus/",
		image="div.entry-content>img.size-full",
		next="a|!rel:in:next",
	),
	Sarjakuva( 
		"FoxTrot", 
		"foxtrot",
		
		"http://www.foxtrot.com", 
		"http://www.foxtrot.com/2015/08/16/no-worries/",
		test="http://www.foxtrot.com/2016/05/01/show-off-and-tell/",

		image="div.entry-content>img.size-full",
		next="a|!rel:in:next",
	),
	

	Sarjakuva( 
		"Berds and Nerds", 
		"berdsandnerds",
		#"berdsandnerds",

		"http://berdsandnerds.com", 
		"http://berdsandnerds.com/comic/2013/4/1/comic-1",
		test="http://berdsandnerds.com/comic/2016/5/9/theothermother",

		image="div.sqs-block-content>noscript>img",
		next="nav.pagination>a|!text:in:newer",
	),

	Sarjakuva(
		"Gunshow", 
		"gunshow",

		"http://www.gunshowcomic.com/",
		"http://www.gunshowcomic.com/1",
		test="http://gunshowcomic.com/897",

		interval=0,
		image="#comic>img.strip",
		next="a|img|!src:in:next.gif",
	),

	Sarjakuva(
		"Back", 
		"back",

		"http://backcomic.com/",
		"http://backcomic.com/1",
		test="http://backcomic.com/93",

		image="#comic>img.comic-page",
		next="#next_comic",
	),

	Sarjakuva(
		"Back", 
		"back",

		"http://backcomic.com/",
		"http://backcomic.com/1",
		test="http://backcomic.com/93",

		image="#comic>img.comic-page",
		next="#next_comic",
	),


	Sarjakuva(
		"He is a Good Boy", 
		"hiagb",

		"http://hiagb.com/",
		"http://hiagb.com/1",
		test="http://hiagb.com/122",

		image="#comicImages>img.comic-page",
		next="#next_comic",
	),

	Sarjakuva(
		"HappleTea", #nimi
		"happletea", # lyhenne
		
		"http://www.happletea.com",  # baseurl
		"http://www.happletea.com/comic/fallacies/",
		test="http://www.happletea.com/comic/asking-the-big-questions/",
		image="#comic>img",
		next="a.navi-next",
	),

	Sarjakuva(
		"Skadi", 
		"skadi",
		
		"http://skadicomic.com", 
		"http://skadicomic.com/2008/05/07/ballad-of-skadi-pt-1-2/",
		test="http://skadicomic.com/comic/delay-or-the-end-is-near/",
		image="#comic>img",
		next="a.comic-nav-next",
		interval=0,
		
	),


	Sarjakuva(
		"C-Section", 
		"csection",
		
		"http://www.csectioncomics.com/", 
		"http://www.csectioncomics.com/comics/one-day-in-country",
		test="http://www.csectioncomics.com/comics/back-in-my-day-dad-online-porn",
		image="#comic>img",
		next="a.comic-nav-next",	
	),

# happletea
	Sarjakuva(
		"Berkeley Mews", 
		"berkeleymews",
		
		"http://www.berkeleymews.com/", 
		"http://www.berkeleymews.com/?p=19",
		test="http://www.berkeleymews.com/?p=970",
		image="#comic>img",
		next="a.navi-next",	
	),

	Sarjakuva(
		"Completely Serious Comics", 
		"completelyseriouscomics",
		
		"http://completelyseriouscomics.com/", 
		"http://completelyseriouscomics.com/?p=6",
		test="pienirinkula.com",
		image="#comic>img",
		next="a.navi-next",
		interval=0, # lopetettu
	),

	Sarjakuva(
		"Pictures in Boxes", 
		"picturesinboxes",
		
		"http://www.picturesinboxes.com/", 
		"http://www.picturesinboxes.com/2013/10/26/tetris/",
		test="http://www.picturesinboxes.com/2015/09/16/transformers/",
		image="#comic>img",
		next="a.navi-next",
	),

	Sarjakuva(
		"Channelate", 
		"channelate",
		
		"http://www.channelate.com/", 
		"http://www.channelate.com/2008/02/13/wear-a-clean-shirt/",
		test="http://www.channelate.com/2016/05/13/something-you-need-to-tell-me/",
		image="#comic>img",
		next="a.navi-next",
	),

	Sarjakuva(
		"Amazing Super Powers", 
		"amazingsuperpowers", 
		
		"http://www.amazingsuperpowers.com/", 
		"http://www.amazingsuperpowers.com/2007/09/heredity/",
		test="http://www.amazingsuperpowers.com/2015/06/young-at-heart/",
		image="#comic>img",
		next="a.navi-next",
	),

	Sarjakuva( 
		"Zen Pencils", 
		"zenpencils",
					
		"http://zenpencils.com/", 
		"http://zenpencils.com/comic/1-ralph-waldo-emerson-make-them-cry/",
		test="http://zenpencils.com/comic/rilke/",
		image="#comic>img",
		next="a.navi-next",
	),

	Sarjakuva(
		"The Noob", 
		"noob",
					
		"http://thenoobcomic.com/", 
		"http://thenoobcomic.com/comic/1/",
		test="http://thenoobcomic.com/comic/450/",
		image="#comic>img",
		next="a.navi-next",
	),

	Sarjakuva( 
		"Safely Endangered", 
		"safelyendangered",
					
		"http://www.safelyendangered.com/", 
		"http://www.safelyendangered.com/comic/ignored/",
		test="http://www.safelyendangered.com/comic/stupid/",
		image="#comic>img",
		next="a.navi-next",
	),
	Sarjakuva(
		"Exploding Dinosaur", 
		"explodingdinosaur",
					
		"http://explodingdinosaur.com/", 
		"http://explodingdinosaur.com/comic/seriously-stop-it/",
		test="http://explodingdinosaur.com/comic/hipster-kitchen/",
		image="#comic>img",
		next="a.navi-next",
	),
	Sarjakuva(
		"Veritable Hokum", 
		"veritablehokum",
		
		"http://www.veritablehokum.com/", 
		"http://www.veritablehokum.com/comic/headless-folks-of-the-french-revolution/",
		test="http://www.veritablehokum.com/comic/presidents-washington-buchanan/",
		image="#comic>img",
		next="a.navi-next",
	),

	Sarjakuva(
		"Hijinks Ensue", 
		"hijinksensue",
		
		"http://hijinksensue.com/", 
		"http://hijinksensue.com/comic/who-is-your-daddy-and-what-does-he-do/",
		test="http://hijinksensue.com/comic/roll-right-roll-call/",
		image="#comic>img",
		next="a.navi-next-in",
	
	),


	Sarjakuva(
		"Sharksplode", 
		"sharksplode",
		
		"http://sharksplode.com/", 
		"http://sharksplode.com/comic/is-it-the-word-is-it-really/",
		test="http://sharksplode.com/comic/back-in-the-saddle/",
		image="#comic>img",
		next="a.navi-next",
	
	),

	Sarjakuva(
		"Legacy Control", 
		"legacy-control",
		
		"http://legacy-control.com/", 
		"http://legacy-control.com/comic/advent-boner-3/",
		test="http://legacy-control.com/comic/beardable/",
		image="#comic>img",
		next="a.navi-next",
		
	),
	Sarjakuva(
		"The Adventures of Businesscat", 
		"businesscat",
		"http://www.businesscat.happyjar.com/", 
		"http://www.businesscat.happyjar.com/comic/coffee/",
		
		test="http://www.businesscat.happyjar.com/comic/butterfly/",
		image="#comic>img",
		next="a.navi-next-in",
	),

	Sarjakuva(
		"Hejibits", 
		"hejibits",
		
		"http://www.hejibits.com/", 
		"http://www.hejibits.com/comics/roommate-comics-1/",
		test="http://www.hejibits.com/comics/going-up/",
		image="#comic>img",
		next="a.navi-next",
	),

	Sarjakuva(
		"The Awkward Yeti", 
		"awkwardyeti",
		
		"http://theawkwardyeti.com/", 
		"http://theawkwardyeti.com/comic/0912-reading/",
		test="http://theawkwardyeti.com/comic/big-confusion/",
		image="#comic>img",
		next="a.navi-next",
		
	),

	Sarjakuva(
		"Big Foot Justice", 
		"bigfootjustice",
		
		"http://bigfootjustice.com/", 
		"http://bigfootjustice.com/comic/iscale-2/",
		test="http://bigfootjustice.com/comic/new-suit/",
		image="#comic>img",
		next="a.navi-next",
		
	),
	# END OF HAPPLETEA

	Sarjakuva(
		"VGCats", 
		"vgcats",
		

		"http://www.vgcats.com/comics/", 
		"http://www.vgcats.com/comics/images/",
		test="null",
		#"http://www.vgcats.com/comics/?strip_id=1",
		# test="http://www.vgcats.com/comics/?strip_id=373",

		# image="td>div|!align:in:center>img|!src:in:images/",
		# next="a|img|!src:in:next.gif",
		parseri="dragonarte",
	),
	Sarjakuva(
		"Nerf Now", 
		"nerfnow",

		"http://www.nerfnow.com/", 
		"http://www.nerfnow.com/comic/4",
		test="http://www.nerfnow.com/comic/1813",

		image="#comic>img",
		next="#nav_next>a",
	),

	Sarjakuva(
		"Sinfest", 
		"sinfest",

		"http://www.sinfest.net/", 
		"http://www.sinfest.net/view.php?date=2000-01-17",
		test="http://sinfest.net/view.php?date=2016-05-16",

		image="img|!src:in:btphp/comics/",
		next="a|img|!src:in:images/next",
	),

	Sarjakuva(
		"Camp", 
		"camp",

		"http://campcomic.com/", 
		"http://campcomic.com/comic/dear-mom",
		test="http://campcomic.com/comic/316",

		image="#comic>img",
		next="a.btnNext",
			
	),

	Sarjakuva(
		"Penny Arcade", 
		"pennyarcade",

		"http://www.penny-arcade.com", 
		"http://www.penny-arcade.com/comic/1998/11/18",
		test="https://www.penny-arcade.com/comic/2016/05/13/schismatic",

		image="#comicFrame>img",
		next="a.btnNext|!href:in:comic",
		#download=False,
	),

	Sarjakuva(
		"The Trenches", 
		"trenches",

		"http://trenchescomic.com/", 
		"http://trenchescomic.com/comic/post/9811",
		test="http://trenchescomic.com/comic/post/ghost-in-the-machine",

		image="div.comic>img",
		next="a.btnNext",
		#download=False,
	),

	Sarjakuva(
		"Fredo & Pidjin", 
		"pidjin",

		"http://www.pidjin.net/", 
		"http://www.pidjin.net/2005/05/30/tricks-to-getting-delayed/",
		test="http://www.pidjin.net/2016/03/03/syrian-steve-jobs/",
		image="div.episode>img",
		next="a|!rel:in:next",
	),




	Sarjakuva(
		"Least I could do", 
		"leasticoulddo",

		"http://www.leasticoulddo.com/comic/", 
		"http://www.leasticoulddo.com/comic/20030210/",
		test="http://www.leasticoulddo.com/comic/20160516/",
		image="#comic>img",
		next="#nav-large-next",
			
	),

	Sarjakuva(
		"Questionable Content", 
		"questionablecontent",

		"http://questionablecontent.net/", 
		"http://questionablecontent.net/view.php?comic=1",
		test="http://www.questionablecontent.net/view.php?comic=3221",
		image="#strip",
		next="#comicnav>a|!text:in:next",
	),

	Sarjakuva(
		"Wulffmorgenthaler", 
		"wumo",

		"http://wumo.com/", 
		"http://wumo.com/wumo/2015/09/08",
		test="http://wumo.com/wumo/2016/05/16",

		image="article.strip>div.box-content>img",
		next="a.next",
		
	),

	Sarjakuva(
		"Pepper and Carrot", 
		"pepperandcarrot",
		
		"http://www.peppercarrot.com", 
		"http://peppercarrot.com/en/article234/potion-of-flight",
		test="http://peppercarrot.com/en/article350/episode-14-the-dragon-s-tooth",

		image="img.comicpage",
		next="a|i.fa-chevron-right",
	),

	Sarjakuva( 
		"Catsu The Cat", 
		"catsu",

		"http://www.catsuthecat.com/blogs/comics/", 
		"http://www.catsuthecat.com/blogs/comics/",
		parseri="catsu",
		test="pienirinkula.com"
	),

	Sarjakuva( 
		"Unsounded", 
		"unsounded",

		"http://www.casualvillain.com/Unsounded/comic+index", 
		"http://www.casualvillain.com/Unsounded/comic/ch01/ch01_01.html",
		#"http://www.casualvillain.com/Unsounded/comic/ch05/ch05_16.html",
		#"http://www.casualvillain.com/Unsounded/comic/ch10/ch10_162.html"
		test="pienirinkula.com",
		parseri="unsounded",

	),

	Sarjakuva( 
		"For lack of a better comic", 
		"floabc",

		"http://www.forlackofabettercomic.com", 
		"http://forlackofabettercomic.com/?id=1",
		test="http://forlackofabettercomic.com/?id=277",

		image="#comicimg",
		next="a|#comicimg",	
	),

	Sarjakuva(
		"Love Me Nice", 
		"lovemenice",

		"http://lovemenicecomic.com/comic/", 
		"http://lovemenicecomic.com/comic/001.php",
		test="http://lovemenicecomic.com/comic/215.php",

		image="#comicimg",
		next="a|#comicimg",
	),
# Sarjakuva(
# 	"Johnny Wander Fiction", 
# 	"johnnywander",


# 	"http://www.johnnywander.com/fiction", 
# 	"http://www.johnnywander.com/fiction/girl-with-the-skeleton-hand-1",
# 	test=None,

# 	image="",
# 	next=""

# 	interval=0, # PÄÄTTYNYT
	
# ),

# Sarjakuva(
# 	"Lucky Penny", 
# 	"luckypenny",

# 	"http://www.johnnywander.com/luckypenny", 
# 	"http://www.johnnywander.com/luckypenny/lucky-penny-001", 
# 	test=None,

# 	image="",
# 	next=""

# 	interval=0, # PÄÄTTYNYT ?
# ),
# Sarjakuva( 
# 	"Autobio", 
# 	"autobio",

# 	"http://www.johnnywander.com/comic", 
# 	"http://www.johnnywander.com/comic/i",	
# 	test=None,

# 	image="",
# 	next=""	

# 	interval=0, # PÄÄTTYNYT ?
# ),

Sarjakuva( 
	"Is This What You Wanted", 
	"itwyw",

	"http://www.johnnywander.com/itwyw/", 
	"http://www.johnnywander.com/itwyw/is-this-what-you-wanted",	
	test="http://www.johnnywander.com/comic/is-this-what-you-wanted-25",

	image="#cc-comic",
	next="#cc-comicbody>a"	

),

Sarjakuva(
	"Lets Speak English", 
	"letsspeakenglish", 

	"http://www.marycagle.com", 
	"http://www.marycagle.com/letsspeakenglish/1-shingeki-no-kodomo",
	test="http://www.marycagle.com/letsspeakenglish/121-on-the-catwalk",
	
	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Whomp", 
	"whomp",

	"http://www.whompcomic.com/", 
	"http://www.whompcomic.com/comic/06152010",
	test="http://www.whompcomic.com/comic/mirror-mismatch",
	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"6 Gun Mage", 
	"6gunmage",

	"http://www.6gunmage.com", 
	"http://www.6gunmage.com/comic/6-gun-mage-kickoff",
	test="http://www.6gunmage.com/comic/page-29-12",
	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"A Ghost Story", 
	"ghoststory",

	"http://www.aghoststorycomic.com", 
	"http://www.aghoststorycomic.com/comic/in-the-black-1",
	test="http://www.aghoststorycomic.com/comic/break-comic-1",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Agents of the Realm", 
	"agentsoftherealm",

	"http://www.agentsoftherealm.com/", 
	"http://www.agentsoftherealm.com/aotr/-volume-1-",
	test="http://www.agentsoftherealm.com/aotr/-intermission-iii-3-by-eve-g",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Alice and the Nightmare", 
	"aliceandthenightmare",

	"http://www.aliceandthenightmare.com/", 
	"http://www.aliceandthenightmare.com/comic/chapter-one-cover",
	test="http://www.aliceandthenightmare.com/comic/chapter-3-page-21",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Aquapunk", 
	"aquapunk",

	"http://www.aquapunk.co/", 
	"http://www.aquapunk.co/comic/book1",
	test="http://www.aquapunk.co/comic/4035",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Astral Aves", 
	"astralaves",

	"http://www.astralaves.com/", 
	"http://www.astralaves.com/comic/a-cacophony-of-stars",
	test="http://www.astralaves.com/comic/09-033",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Atomic-robo", 
	"atomicrobo",

	"http://www.atomic-robo.com/", 
	"http://www.atomic-robo.com/atomicrobo/v1ch1-cover",
	test="http://www.atomic-robo.com/atomicrobo/v11ch1-page-21",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Awaken", 
	"awaken",

	"http://www.awakencomic.com/", 
	"http://www.awakencomic.com/comic/comic-cover",
	test="http://www.awakencomic.com/comic/ch4-page-28",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Balderdash", 
	"balderdash",

	"http://www.balderdashcomic.com/", 
	"http://www.balderdashcomic.com/comic/i01",
	test="http://www.balderdashcomic.com/comic/chapter-vi-page-149",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Basinvale", 
	"basinvale",

	"http://www.basinvale.com/", 
	"http://www.basinvale.com/index.php?id=1",
	test="http://www.basinvale.com/index.php?id=129",

	image="#comic",
	next="a.next"	
),

Sarjakuva(
	"Beeserker", 
	"beeserker",

	"http://www.beeserker.com/", 
	"http://www.beeserker.com/comics/the-scienceman/",
	test="http://www.beeserker.com/comics/wallpapers/",

	image="#comic>img",
	next="a.navi-next"	
),


Sarjakuva(
	"Black Grass", 
	"blackgrass",

	"http://blackgrasscomic.com/", 
	"http://www.blackgrasscomic.com/comic/page-1",
	test="http://www.blackgrasscomic.com/comic/page-68",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Blaster Nation", 
	"blasternation",

	"http://www.blasternation.com/", 
	"http://www.blasternation.com/comic/1-one-day-in-the-life-of-matthew-palmer",
	test="http://www.blasternation.com/comic/497-poor-hammy",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Blindsprings", 
	"blindsprings",

	"http://www.blindsprings.com/", 
	"http://www.blindsprings.com/comic/blindsprings-cover-book-one",
	test="http://www.blindsprings.com/comic/whomp-whomp",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Broodhollow", 
	"broodhollow",

	"http://broodhollow.chainsawsuit.com/", 
	"http://broodhollow.chainsawsuit.com/page/2012/10/06/book-1-curious-little-thing/",
	test="http://broodhollow.chainsawsuit.com/page/2016/05/09/among-the-bowers-page-3/",

	image="#comic>img",
	next="a.navi-next"	
),


Sarjakuva(
	"Cassiopeia Quinn", 
	"cassiopeiaquinn",

	"http://www.cassiopeiaquinn.com/", 
	"http://www.cassiopeiaquinn.com/comic/the-prize-cover",
	test="http://www.cassiopeiaquinn.com/comic/the-big-race-page-32",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva(
	"Clique Refresh", 
	"cliquerefresh",

	"http://cliquerefresh.com/", 
	"http://cliquerefresh.com/comic/start-it-up/",
	test="http://cliquerefresh.com/comic/111-the-struggle/",

	image="div.comicImg>img",
	next="#nextcomic"	
),

Sarjakuva(
	"Crazy Sunshine", 
	"crazysunshine",

	"http://www.crazysunshine.com/", 
	"http://www.crazysunshine.com/",
	test=None,

	image="#cc-comic",
	next="#cc-comicbody>a",
	interval=0
),

Sarjakuva(
	"Cut Time", 
	"cuttime",

	"http://www.cuttimecomic.com/", 
	"http://www.cuttimecomic.com/comic/volume-01-first-impressions",
	test="http://www.cuttimecomic.com/comic/chapter-2-page-6",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Daughter of the Lilies", 
	"daughterofthelilies",  

	"http://www.daughterofthelilies.com/", 
	"http://www.daughterofthelilies.com/dotl/part-1-a-girl-with-no-face", 
	test="http://www.daughterofthelilies.com/dotl/503",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),


 Sarjakuva( # ANGULARJS tee custom class. META TAGISTA url
 	"Deathbulge", 
 	"deathbulge", 

 	"http://www.deathbulge.com/", 
 	"http://www.deathbulge.com/comics/1", 
 	test="http://www.deathbulge.com/comics/341",

	#image="#comic>img",
	image="meta|!content:in:images/comics/",
	next="#next-button"	
 ),


Sarjakuva( 
	"Demon Street", 
	"demonstreet",  

	"http://www.demonstreet.co/", 
	"http://www.demonstreet.co/comic/1", 
	test="http://www.demonstreet.co/comic/276",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),


Sarjakuva( 
	"Devil's Candy", 
	"devilscandy",  

	"http://www.devilscandycomic.com/", 
	"http://www.devilscandycomic.com/?comic=prologue-01-2", 
	test="http://www.devilscandycomic.com/?comic=ch04p04",

	image="#comic>img",
	next="a.comic-nav-next"	
),


Sarjakuva( 
	"Dumbing of Age", 
	"dumbingofage",  

	"http://www.dumbingofage.com/", 
	"http://www.dumbingofage.com/2010/comic/book-1/01-move-in-day/home/", 
	test="http://www.dumbingofage.com/2016/comic/book-6/03-when-god-closes-the-door/traumatizing/",

	image="#comic>img",
	next="a.navi-next"	
),


Sarjakuva( 
	"El Goonish Shive", 
	"elgoonishshive",  

	"http://www.egscomics.com/", 
	"http://www.egscomics.com/index.php?id=1", 
	test="http://www.egscomics.com/index.php?id=2188",

	image="#comic",
	next="a.next"	
),


Sarjakuva( 
	"Empowered", 
	"empowered",  

	"http://www.empoweredcomic.com", 
	"http://www.empoweredcomic.com/comic/volume-1-page-1", 
	test="http://www.empoweredcomic.com/comic/volume-1-page-225",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Flight of the Binturong", 
	"flightofthebinturong",  

	"http://www.flightofthebinturong.com/", 
	"http://flightofthebinturong.com/comic/cover/", 
	test="http://flightofthebinturong.com/comic/update-87-awakenings/",

	image="#comic>img",
	next="a.navi-next"	
),


# Sarjakuva( # ihan paska
# 	"Floraverse", 
# 	"floraverse",  

# 	"http://www.floraverse.com/", 
# 	"http://floraverse.com/comic/seeds-a-mini-story/prologue/1-cover/", 
# 	test="http://floraverse.com/comic/oneshots/459-canada-incoming/",

# 	image="img.comic-page-image",
# 	next="div.-next>a"	
# ),


Sarjakuva( 
	"Girl Genius", 
	"girlgenius",  

	"http://www.girlgeniusonline.com/", 
	"http://www.girlgeniusonline.com/comic.php?date=20021104", 
	test="http://www.girlgeniusonline.com/comic.php?date=20160513",

	image="img|!alt:in:comic",
	next="#topnext"	
),


Sarjakuva( 
	"Girlbot", 
	"girlbot",  

	"http://www.intrepidgirlbot.com/", 
	"http://www.intrepidgirlbot.com/2009/03/06/pretty-people-processor/", 
	test="http://www.intrepidgirlbot.com/2015/09/25/dumb-girlbot-comics-stripes/",

	image="img.comic-item",
	next="a.next-comic-link"	
),


Sarjakuva( 
	"Go Get a Roomie", 
	"gogetaroomie",  

	"http://www.gogetaroomie.com/", 
	"http://www.gogetaroomie.com/comic/and-so-it-begins", 
	test="http://www.gogetaroomie.com/comic/happy-family-shopping-yay",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),


Sarjakuva( 
	"Godslave", 
	"godslave",  

	"http://www.godslavecomic.com/", 
	"http://www.godslavecomic.com/comic/page-1", 
	test="http://www.godslavecomic.com/comic/challenging",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),


Sarjakuva( 
	"Guilded Age", 
	"guildedage",  

	"http://www.guildedage.net", 
	"http://guildedage.net/comic/chapter-1-cover/", 
	test="http://guildedage.net/comic/chapter-42-page-8/",

	image="#comic>img",
	next="a.navi-next"	
),


Sarjakuva( 
	"Harpy Gee", 
	"harpygee",  

	"http://www.harpygee.com/", 
	"http://www.harpygee.com/comic/cover", 
	test="http://www.harpygee.com/comic/ch3hivepg090",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),


Sarjakuva( 
	"Headless Bliss", 
	"headlessbliss",  

	"http://www.headlessbliss.com/", 
	"http://www.headlessbliss.com/comic/page-1", 
	test="http://www.headlessbliss.com/comic/page-138",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),


Sarjakuva( 
	"Heart-Shaped Skull", 
	"heartshapedskull",  

	"http://www.heartshapedskull.com/", 
	"http://www.heartshapedskull.com/2002/10/31/working-through-the-negativity-cover/", 
	test="http://www.heartshapedskull.com/2013/11/28/break-your-stupid-heart-page-120/",

	image="#comic>img",
	next="a.navi-next",
	interval=0 # lopetettu
),


Sarjakuva( 
	"Helvetica", 
	"helvetica",  

	"http://helvetica.jnwiedle.com/", 
	"http://helvetica.jnwiedle.com/2011/06/24/and-so-it-begins/", 
	test="http://helvetica.jnwiedle.com/2015/11/29/very-romantic/",

	image="#comic>img",
	next="div.nav-next>a",
),


Sarjakuva( 
	"I Am Arg!", 
	"iamarg",  

	"http://www.iamarg.com/", 
	"http://iamarg.com/2011/05/08/05082011/", 
	test="http://iamarg.com/2016/03/14/03142016/",

	image="#comic>img",
	next="a.navi-next",
),


Sarjakuva( 
	"Jailbird", 
	"jailbird",  

	"http://an.oddlookingbird.com/", 
	"http://an.oddlookingbird.com/comic/page-1", 
	test="http://an.oddlookingbird.com/comic/page-127",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Kiwi Blitz", 
	"kiwiblitz",  

	"http://www.kiwiblitz.com/", 
	"http://www.kiwiblitz.com/comic/welcome-to-kb", 
	test="http://www.kiwiblitz.com/comic/page-463",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Knights Errant", 
	"knightserrant",  

	"http://sparklermonthly.com/series/knights-errant/", 
	"http://sparklermonthly.com/ke/knights-errant-chapter-01-page-001/", 
	test="http://sparklermonthly.com/ke/knights-errant-chapter-04-page-121/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link"	
),

Sarjakuva( 
	"Lost Nightmare", 
	"lostnightmare",  

	"http://www.lostnightmare.com/", 
	"http://www.lostnightmare.com/comic/01-01", 
	test="http://www.lostnightmare.com/comic/06-20",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Love Not Found", 
	"lovenotfound",  

	"http://www.lovenotfound.com/", 
	"http://www.lovenotfound.com/comic/chapter-1-cover", 
	test="http://www.lovenotfound.com/comic/chapter-10-page-07",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Magical How?", 
	"magicalhow",  

	"http://sparklermonthly.com/series/magical-how/", 
	"http://sparklermonthly.com/mh/magical-how-chapter-01-page-001/", 
	test="http://sparklermonthly.com/mh/magical-how-chapter-03-page-051/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link"	
),

Sarjakuva( 
	"Mare Internum", 
	"mareinternum",  

	"http://www.marecomic.com/", 
	"http://www.marecomic.com/comic/intro-page-1/", 
	test="http://www.marecomic.com/comic/ch3-page-24/",

	image="#comic>img",
	next="a.comic-nav-next",	
),

Sarjakuva( 
	"Meaty Yogurt", 
	"meatyyogurt",  

	"http://www.meatyyogurt.com/", 
	"http://rosalarian.com/meatyyogurt/2010/10/01/starting-things-off-with-a-bang-4/", 
	test="http://rosalarian.com/meatyyogurt/2016/04/11/just-love/",

	image="#comic>img",
	next="div.nav-next>a",
),

Sarjakuva( 
	"Metacarpolis", 
	"metacarpolis",  

	"http://www.metacarpolis.com/", 
	"http://www.metacarpolis.com/metacarpolis/chapter-1-page-1", 
	test="http://www.metacarpolis.com/metacarpolis/a-guide-to-the-digits-of-metacarpolis-part-1",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Misfile", 
	"misfile",  

	"http://www.misfile.com/", 
	"http://www.misfile.com/?date=2004-02-22", 
	test="http://www.misfile.com/?date=2016-05-17",

	image=".comic>img",
	next="#comic>a",
),

Sarjakuva( 
	"Monster Pulse", 
	"monserpulse",  

	"http://www.monster-pulse.com/", 
	"http://www.monster-pulse.com/comic/monster-pulse", 
	test="http://www.monster-pulse.com/comic/page-9-chapter-23",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Monsterkind", 
	"monsterkind",  

	"http://monsterkind.enenkay.com/", 
	"http://monsterkind.enenkay.com/comic/first", 
	test="http://monsterkind.enenkay.com/comic/313",

	image="#comic>img",
	next="#comic>a",
),

Sarjakuva( 
	"Namesake", 
	"namesake",  

	"http://www.namesakecomic.com/", 
	"http://namesakecomic.com/comic/the-journey-begins", 
	test="http://namesakecomic.com/comic/warrick-selva-and-fred-cool-things-about-earth",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Never Satisfied", 
	"neversatisfied",  

	"http://www.neversatisfiedcomic.com/", 
	"http://www.neversatisfiedcomic.com/comic/chapter-1-chirp-chirp-chirp", 
	test="http://www.neversatisfiedcomic.com/comic/chapter-3-page-33",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Not Drunk Enough", 
	"notdrunkenough",  

	"http://www.ndecomic.com/", 
	"http://www.ndecomic.com/comic/page-1", 
	test="http://www.ndecomic.com/comic/page-130",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Oh Joy Sex Toy!", 
	"ohjoysextoy",  

	"http://www.ohjoysextoy.com/", 
	"http://www.ohjoysextoy.com/introduction/", 
	test="http://www.ohjoysextoy.com/period-sex/",

	image="#comic>img",
	next="a.navi-next",
),

Sarjakuva( 
	"Parallax", 
	"parallax",  

	"http://www.parallaxcomic.com/", 
	"http://www.parallaxcomic.com/comic/page-01", 
	test="http://www.parallaxcomic.com/comic/page-106",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Paranatural", 
	"paranatural",  

	"http://www.paranatural.net/", 
	"http://www.paranatural.net/comic/chapter-1", 
	test="http://www.paranatural.net/comic/chapter-5-page-117",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Peritale", 
	"peritale",  

	"http://www.peritale.com/", 
	"http://www.peritale.com/comic/promo", 
	test="http://www.peritale.com/comic/p93",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

# Sarjakuva( # ei toimi, lopetettu
# 	"Platinum Black", 
# 	"platinumblack", 
# 	"paintrain", 

# 	"http://www.platinumblackcomic.com", 
# 	"http://platinumblackcomic.com/?comic=chapter-1-cover", 
# 	test=None,

# 	image="#cc-comic",
# 	next="#cc-comicbody>a"	
# ),

Sarjakuva( 
	"Prague Race", 
	"praguerace",  

	"http://www.praguerace.com/", 
	"http://www.praguerace.com/comic/start", 
	test="http://www.praguerace.com/comic/long-into-the-night",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Real Science Adventures", 
	"realscienceadventures",  

	"http://www.realscienceadventures.com", 
	"http://www.realscienceadventures.com/comic/v01ch1-page-cover", 
	test="http://www.realscienceadventures.com/comic/v02ch2-page-2",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Roji", 
	"roji",  

	"http://www.rojicomic.com/", 
	"http://www.rojicomic.com/comic/promo", 
	test="http://www.rojicomic.com/comic/the-hero",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Saint for Rent", 
	"saintforrent",  

	"http://www.saintforrent.com/", 
	"http://www.saintforrent.com/comic/the-cloverhouse-inn", 
	test="http://www.saintforrent.com/comic/7-004",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"SAKANA", 
	"sakana",  

	"http://www.sakana-comic.com/", 
	"http://www.sakana-comic.com/comic/title-page-vol-1", 
	test="http://www.sakana-comic.com/comic/354",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Sam and Fuzzy", 
	"samandfuzzy",  

	"http://www.samandfuzzy.com/", 
	"http://www.samandfuzzy.com/1", 
	test="http://www.samandfuzzy.com/2203",

	image="img.comic-image",
	next="li.next-page>a"	
),

Sarjakuva( 
	"Scenes From a Multiverse", 
	"multiverse",  

	"http://www.amultiverse.com/", 
	"http://amultiverse.com/comic/2010/06/14/parenthood/", 
	test="http://amultiverse.com/comic/2016/05/12/president-plus/",
	#test="http://amultiverse.com/comic/2010/06/17/ladies-choice/",
	image="#comic>img",
	next="a.navi-next",
),

Sarjakuva( 
	"Sfeer Theory", 
	"sfeertheory",  

	"http://www.sfeertheory.com/", 
	"http://www.sfeertheory.com/comic/01-01", 
	test="http://www.sfeertheory.com/comic/03-49",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Shortpacked!", 
	"shortpacked",  

	"http://www.shortpacked.com/", 
	"http://www.shortpacked.com/index.php?id=1", 
	test="http://www.shortpacked.com/index.php?id=2192",

	image="#comic",
	next="#comicbody>a"	
),

Sarjakuva( 
	"Sister Claire", 
	"sisterclaire",  

	"http://www.sisterclaire.com/", 
	"http://www.sisterclaire.com/comic/book-one", 
	test="http://www.sisterclaire.com/comic/book-2-chapter-8-pg-211",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Sister Claire Missing", 
	"sisterclairemissing",  

	"http://www.sisterclaire.com/", 
	"http://www.sisterclaire.com/missing-moments/missing-moment-la-scoperta", 
	test="http://www.sisterclaire.com/missing-moments/missing-moment-acqua-in-aumento-7",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Skullkickers", 
	"skullkickers",  

	"http://comic.skullkickers.com/", 
	"http://comic.skullkickers.com/comic/2012-01-06", 
	test="http://comic.skullkickers.com/comic/march-16-2016",

	image="#cc-comic",
	next="a.next"	
),

Sarjakuva( 
	"Sleepless Domain", 
	"sleeplessdomain",  

	"http://www.sleeplessdomain.com/", 
	"http://www.sleeplessdomain.com/comic/chapter-1-cover", 
	test="http://www.sleeplessdomain.com/comic/chapter-4-page-13",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Slightly Damned", 
	"slightlydamned",  

	"http://www.sdamned.com/", 
	"http://www.sdamned.com/comic/part-one-to-hell-and-back", 
	test="http://www.sdamned.com/comic/747",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"SnarlBear", 
	"snarlbear",  

	"http://www.snarlbear.com/", 
	"http://www.snarlbear.com/index.php?id=1", 
	test="http://www.snarlbear.com/comic/9-6",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Solstoria", 
	"solstoria",  

	"http://www.solstoria.net/", 
	"http://solstoria.net/comic/54/", 
	test="http://solstoria.net/comic/page-181/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva( 
	"Spinnerette", 
	"spinnerette",  

	"http://www.spinnyverse.com/", 
	"http://www.spinnyverse.com/comic/02-09-2010", 
	test="http://www.spinnyverse.com/comic/white-heron-preview-2",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"StarHammer", 
	"starhammer",  

	"http://www.starhammercomic.com/", 
	"http://www.starhammercomic.com/comic/chapter-1-the-shakedown-pg-1-leading-the-charges", 
	test="http://www.starhammercomic.com/comic/chapter-2-two-for-one-page-25-mergers-acquisitions-",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Street Fighter Comics", 
	"streetfighter",  

	"http://www.streetfightercomics.com/", 
	"http://www.streetfightercomics.com/comic/stage-0-page-1", 
	test="http://www.streetfightercomics.com/comic/stage-12-page-21",

	image="#cc-comic",
	next="#cc-comicbody>a",
	interval="0"	
),

Sarjakuva( 
	"Sufficiently Remarkable", 
	"sufficientlyremarkable", 

	"http://www.sufficientlyremarkable.com/", 
	"http://sufficientlyremarkable.com/comic/the-beach", 
	test="http://sufficientlyremarkable.com/comic/dark",

	image="img.comic",
	next="a.nav-next"	
),

Sarjakuva( 
	"Supernormal Step", 
	"supernormalstep",  

	"http://www.supernormalstep.com/", 
	"http://www.supernormalstep.com/archives/8", 
	test="http://www.supernormalstep.com/archives/perspective",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"The Black Brick Road of OZ", 
	"theblackbrickroadofoz",  

	"http://www.blackbrickroadofoz.com", 
	"http://www.blackbrickroadofoz.com/comic/cover", 
	test="http://www.blackbrickroadofoz.com/comic/inefficient-storytelling",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"The Boy Who Fell", 
	"theboywhofell",  

	"http://www.boywhofell.com/", 
	"http://www.boywhofell.com/comic/ch00p01", 
	test="http://www.boywhofell.com/comic/ch3522",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"The End", 
	"end",  

	"http://www.endcomic.com/", 
	"http://www.endcomic.com/comic/book-one-cover/", 
	test="http://www.endcomic.com/comic/ch18-35/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva( 
	"The Glass Scientists", 
	"glassscientists",  

	"http://www.theglassscientists.com/", 
	"http://www.theglassscientists.com/?comic=chapter-i", 
	test="http://www.theglassscientists.com/?comic=page-03-3",

	image="#comic>img",
	next="a.navi-next",	
),

Sarjakuva( 
	"The Last Diplomat", 
	"lastdiplomat",  

	"http://www.thelastdiplomat.com/", 
	"http://www.thelastdiplomat.com/comic/page-001", 
	test="http://www.thelastdiplomat.com/comic/page-102",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"The Lonely Vincent Bellingham", 
	"lonelyvincent",  

	"http://www.lonelyvincent.com/", 
	"http://www.lonelyvincent.com/lonelyvincent/0", 
	test="http://www.lonelyvincent.com/lonelyvincent/82",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"The Mash", 
	"mash",  

	"http://www.mashcomic.com/", 
	"http://www.mashcomic.com/comic/prologue-01-and-02", 
	test="http://www.mashcomic.com/comic/intermission-page-1",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"The Meek", 
	"meek",  

	"http://www.meekcomic.com/", 
	"http://www.meekcomic.com/comic/chapter-1-cover/", 
	test="http://www.meekcomic.com/comic/5-04/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva( 
	"This Is Not Fiction", 
	"thisisnotfiction",  

	"http://www.thisisnotfiction.com/", 
	"http://www.thisisnotfiction.com/comic/ch-01-sydney-morgan", 
	test="http://www.thisisnotfiction.com/comic/ch-23-pg-05",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Todd Allison and the Petunia Violet", 
	"petuniaviolet",  

	"http://petuniaviolet.com", 
	"http://petuniaviolet.com/index.php?id=1", 
	test="http://petuniaviolet.com/index.php?id=604",

	image="#comic",
	next="a.next"	
),

Sarjakuva( 
	"Tove", 
	"tove",  

	"http://www.tovecomic.com/", 
	"http://www.tovecomic.com/comic/chapter-1-page-1", 
	test="http://www.tovecomic.com/comic/chapter-2-page-49",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Trying Human", 
	"tryinghuman",  

	"http://www.tryinghuman.com/", 
	"http://www.tryinghuman.com/comic/prologue--01", 
	test="http://www.tryinghuman.com/comic/chapter-19-738",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Vibe", 
	"vibecomic",  

	"http://www.vibecomic.com/", 
	"http://www.vibecomic.com/vibe/cover-2", 
	test="http://www.vibecomic.com/vibe/226",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

 Sarjakuva( 
 	"Weregeek", 
 	"weregeek",  

 	"http://www.weregeek.com/", 
 	"http://www.weregeek.com/2006/11/27/", 
 	test="http://www.weregeek.com/2016/05/17/",

	image="#comic>img",
	next="a|img|!alt:in:next"	
 ),

Sarjakuva( 
	"Wilde Life", 
	"wildelife",  

	"http://www.wildelifecomic.com/", 
	"http://www.wildelifecomic.com/comic/1", 
	test="http://www.wildelifecomic.com/comic/215",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

Sarjakuva( 
	"Wonderlust", 
	"wonderlust",  

	"http://www.wonderlustcomic.com", 
	"http://www.wonderlustcomic.com/comic/pg-1-2-vamoose", 
	test="http://www.wonderlustcomic.com/comic/pg-20-go",

	image="#cc-comic",
	next="#cc-comicbody>a"	
),

 Sarjakuva(  
 	"You Suck", 
 	"yousuck",  

 	"http://yousuck.slipshine.net/", 
 	"http://yousuck.slipshine.net/go/1-legolas", 
 	test="http://yousuck.slipshine.net/go/249-giving-it-a-shot",

	image="#cc-comic",
	next="#cc-comicbody>a"	
 ),

Sarjakuva( 
	"Zombie Roomie", 
	"zombieroomie",

	"http://www.zombieroomie.com/", 
	"http://www.zombieroomie.com/2009/10/26/issues/", 
	test="http://www.zombieroomie.com/2016/05/16/the-pack-part-6/",

	image="#comic>img",
	next="a.navi-next",	
),


Sarjakuva( 
	"Eerie Cuties", 
	"eeriecuties",  

	"http://www.eeriecuties.com/articles/strips-ec/%28chapter_1%29_it_is_gonna_eat_me%21", 
	"http://www.eeriecuties.com/strips-ec/%28chapter_1%29_it_is_gonna_eat_me%21", 
	test="http://www.eeriecuties.com/strips-ec/siren_brawl_-_pg_10_of_12",

	image="#comic>img",
	next="#cndnextt"	
),

Sarjakuva(
	"Menage a 3", 
	"ma3", 

	"http://www.ma3comic.com/", 
	"http://www.ma3comic.com/strips-ma3/for_new_readers",
	test="http://www.ma3comic.com/strips-ma3/synchronized_swimmers",

	image="#cc>img",
	next="#cndnext",
),

Sarjakuva( 
	"Magick Chicks", 
	"magickchicks",  

	"http://www.magickchicks.com/", 
	"http://www.magickchicks.com/strips-mc/tis_but_a_trifle", 
	test="http://www.magickchicks.com/strips-mc/epilogue",

	image="#comic>img",
	next="#cndnextt",
),

Sarjakuva( 
	"Sandra on the Rocks", 
	"sandraontherocks",  

	"http://www.sandraontherocks.com/", 
	"http://www.sandraontherocks.com/strips-sotr/start_by_running", 
	test="http://www.sandraontherocks.com/strips-sotr/higher_education_will_do_wonders",

	image="#comic>img",
	next="#cndnext",
),

Sarjakuva( 
	"Sticky Dilly Buns", 
	"stickydillybuns",  

	"http://www.stickydillybuns.com/", 
	"http://www.stickydillybuns.com/strips-sdb/awesome_leading_man", 
	test="http://www.stickydillybuns.com/strips-sdb/easter_2016",

	image="#comic>img",
	next="#cndnext",
),

Sarjakuva( 
	"Dangerously Chloe",  
	"dangerouslychloe",

	"http://www.dangerouslychloe.com/", 
	"http://www.dangerouslychloe.com/strips-dc/tighter_fit_than_i_thought", 
	test="http://www.dangerouslychloe.com/articles/strips-dc/chapter_1_-_that_damned_girl",

	image="#comic>img",
	next="#cndnextt",
),

Sarjakuva( 
	"Demon Aid",  
	"demonaid",

	"http://demonaidcomic.com/", 
	"http://demonaidcomic.com/index.php?id=14", 
	test="http://demonaidcomic.com/index.php?id=70",

	image="#comic",
	next="a.next",
	interval=0,
),

Sarjakuva( 
	"Erstwhile",  
	"erstwhile",

	"http://www.erstwhiletales.com/", 
	"http://www.erstwhiletales.com/fcd-00/", 
	test="http://www.erstwhiletales.com/happily-ever-after-09/",

	image="#comic>img",
	next="a.navi-next",
	interval=0,
),

Sarjakuva( 
	"Love is in the Blood",  
	"loveisintheblood",

	"http://www.loveisintheblood.com/", 
	"http://www.loveisintheblood.com/comic/welcome-to-love-is-in-the-blood/", 
	test="http://www.loveisintheblood.com/comic/changes-chapter-06-page-23-0425/",

	image="#comic>img",
	next="a.comic-nav-next",
	interval=0,
),

Sarjakuva( 
	"Love Not Found",  
	"lovenotfound",

	"http://lovenotfound.com/", 
	"http://www.lovenotfound.com/comic/chapter-1-cover", 
	test="http://www.lovenotfound.com/comic/chapter-10-page-07",

	image="#cc-comic",
	next="#cc-comicbody>a",

),

Sarjakuva( 
	"Red String",  
	"redstring",

	"http://redstringcomic.com/", 
	"http://redstringcomic.com/index.php?id=434", 
	test="http://redstringcomic.com/index.php?id=1629",

	image="#comic",
	next="a.next",
	interval=0,
),

Sarjakuva( 
	"Luke McGarry",  
	"lukemcgarry",

	"http://lukemcgarry.com/", 
	"http://lukemcgarry.com/2013/06/oc-weekly-cover-may-31-june-6/", 
	test="http://lukemcgarry.com/2016/02/loptimum-billionaires/",

	image="div.article>img",
	next="a|!rel:in:next",
),

# INTERROBANG
Sarjakuva(
	"Im my own Mascot", 
	"imomascot",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=141",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=1708",

	image="div.comic-content>img",
	next="div.comic-content>a"
),

Sarjakuva(
	"Wookie-ookies", 
	"wookie",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=929",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=987",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0
),
Sarjakuva(
	"Things Which Defy Categorization", 
	"twdc",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=49",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=1690",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0
),
Sarjakuva( 
	"Fair-Haired Adventure Seekers", 
	"adventureseekers",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=930",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=1679",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0
),
Sarjakuva( 
	"It sucks to be Weegie", 
	"weegie",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=941",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=1562",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0
),
Sarjakuva( 
	"WatchBabies", 
	"watchbabies",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=959",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=969",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0
),
Sarjakuva( 
	"Ensign3 Crisis of Infinite Sues", 
	"ensign3",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=989",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=1673",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0
),
Sarjakuva( 
	"Spinks", 
	"spinks",

	"http://www.interrobangstudios.com/", 
	"http://www.interrobangstudios.com/comics-display.php?strip_id=78",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=1502",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0
),
Sarjakuva( 
	"Trigger Star", 
	"triggerstar",

	"http://www.interrobangstudios.com/", 
	"http://www.interrobangstudios.com/comics-display.php?strip_id=60",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=1440",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0
),
Sarjakuva(
	"The Dark Intruder", 
	"darkintruder",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=1",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=505",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0,
),
Sarjakuva(
	"A Girl Named Bob", 
	"girlbob",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=31",
	test="",

	image="div.comic-content>img",
	next="div.comic-content>a"
),
Sarjakuva(
	"This is Visas", 
	"visas",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=357",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=359",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0,
),
Sarjakuva(
	"Heeere's Satan", 
	"heresatan",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=146",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=396",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0
),
Sarjakuva(
	"Punker Darren", 
	"punkerdarren",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=16",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=347",

	image="div.comic-content>img",
	next="div.comic-content>a"
),
Sarjakuva(
	"Space is really big!", 
	"bigspace",

	"http://www.interrobangstudios.com/", 
	"http://interrobangstudios.com/comics-display.php?strip_id=55",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=197",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0,
),
Sarjakuva(
	"He's Gonna Cut Ya", 
	"gonnacutya",

	"http://www.interrobangstudios.com/", 
	"http://www.interrobangstudios.com/comics-display.php?strip_id=52",
	test="http://www.interrobangstudios.com/comics-display.php?strip_id=118",

	image="div.comic-content>img|!src:in:images/comics",
	next="div.comic-content>a",
	interval=0,
),

Sarjakuva(
	"Pickled Comics", 
	"pickled",

	"http://www.pickledcomics.com/", 
	"http://pickledcomics.com/universal-perspective/",
	test="http://pickledcomics.com/ol-jimmy-two-legs/",

	image="div.the-content>img",
	next="span.page-next>a",
),

# Sarjakuva( # failed. paha iframe setti
# 	"Doodle for Food", 
# 	"doodleforfood",

# 	"http://doodleforfood.com/", 
# 	"http://doodleforfood.com/post/42168228343/giraffries-remember-not-to-play-with-your-food",
# 	test="http://doodleforfood.com/post/140977576838",
# 	parseri="TumblrIframe",

# 	image="div.photoset>img",
# 	next="a|img|!src:in:tumblr_static_3mmk30mw8fsw0oggsk4ckg4wg.png",
# ),

Sarjakuva(
	"Cup O'Love", 
	"cupolove",

	"http://dsan.orgymania.net/", 
	"http://dsan.orgymania.net/comic/mya-janet-1",
	test="http://dsan.orgymania.net/comic/dark-roast-pg-6",

	image="#cc-comicbody>img",
	next="a.next",
),

Sarjakuva(
	"Rontti", 
	"rontti",

	"https://rontticomics.com/", 
	"https://rontticomics.com/comic/vauvatreffit-2/",
	test="https://rontticomics.com/comic/vessaetiketti/",

	image="div.comic-content>img",
	next="div.nav-next>a",
),

Sarjakuva(
	"They Can Talk", 
	"theycantalk",

	"http://theycantalk.com/", 
	"http://theycantalk.com/rss",
	test="http://theycantalk.com/rss",

	image="item>description>img",
	next="",
	parseri="rssreader",
),

Sarjakuva(
	"Calm Blue Oceans", 
	"calmblueoceans",

	"http://calmblueoceans.com/", 
	"http://calmblueoceans.com/1/",
	test="http://calmblueoceans.com/91/",

	image="#comic>img",
	next="a.navi-next",
),

Sarjakuva(
	"Girly", 
	"girly",

	"http://girlyyy.com/", 
	"http://girlyyy.com/go/1",
	test="http://girlyyy.com/go/762",

	image="img|!src:in:comics/girly",
	next="a|!text:in:next",
	interval=0,
),

Sarjakuva(
	"Boxer Hockey", 
	"boxerhockey",

	"http://boxerhockeycomic.tumblr.com/", 
	"http://boxerhockeycomic.tumblr.com/post/97715070395/comprising-of-the-first-four-years-of-boxer",
	test="http://boxerhockeycomic.tumblr.com/post/97994629605",

	image="article.post>figure.photo-hires-item>img",
	next="a|!text:in:next",
),


Sarjakuva(
	"Buttersafe", 
	"buttersafe",

	"http://buttersafe.com/", 
	"http://buttersafe.com/2007/04/03/breakfast-sad-turtle/",
	test="http://buttersafe.com/2016/05/12/a-delivery-from-the-stork/",

	image="#comic>img",
	next="a|!rel:in:next",
),

Sarjakuva(
	"The Cummoner", 
	"cummoner",

	"http://www.totempole666.com/", 
	"http://www.totempole666.com/comic/first-time-for-everything-00-cover/",
	test="http://www.totempole666.com/comic/swallowing-dark-14/",

	image="#comic>img",
	next="a.navi-next",
),


Sarjakuva(
	"Two Kinds", 
	"twokinds",

	"http://twokinds.keenspot.com/", 
	"http://twokinds.keenspot.com/archive.php?p=1",
	test="http://twokinds.keenspot.com/archive.php?p=915",

	image="div.comic>img",
	next="#cg_next",
),

Sarjakuva(
	"The Monster Under the Bed", 
	"monsterunderthebed",

	"http://themonsterunderthebed.net/", 
	"http://themonsterunderthebed.net/?comic=test-post",
	test="http://themonsterunderthebed.net/?comic=80-a-dark-mirror",

	image="#comic>img",
	next="a.comic-nav-next",
),


Sarjakuva(
	"Delve", 
	"delve",

	"http://thisis.delvecomic.com/NewWP/", 
	"http://thisis.delvecomic.com/NewWP/comic/in-too-deep/",
	test="http://thisis.delvecomic.com/NewWP/comic/division-and-conquest/",

	image="#comic>img",
	next="a.comic-nav-next",
),


Sarjakuva(
	"Not a Villain", 
	"notavillain",

	"http://navcomic.com/", 
	"http://navcomic.com/not-a-villain/v1-001/",
	test="http://navcomic.com/not-a-villain/page-488/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),


Sarjakuva(
	"Replay", 
	"replay",

	"http://replaycomic.com/", 
	"http://replaycomic.com/comic/red-desert/",
	test="http://replaycomic.com/comic/important-memory-4/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Sandra and Woo", 
	"sandraandwoo",

	"http://www.sandraandwoo.com/", 
	"http://www.sandraandwoo.com/2008/10/19/a-sly-raccoon/",
	test="http://www.sandraandwoo.com/2016/05/09/0784-rude-awakening-page-1/",

	image="#comic>img",
	next="div.nav-next>a",
),


Sarjakuva(
	"Mr Lovenstein", 
	"mrlovenstein",

	"http://www.mrlovenstein.com/", 
	"http://www.mrlovenstein.com/comic/1",
	test="http://www.mrlovenstein.com/comic/775",

	image="#comic_main_image",
	next="a|img|!src:in:nav_right.png",
),


Sarjakuva(
	"The Gentlemans Armchair", 
	"thegentlemansarmchair",

	"http://thegentlemansarmchair.com/", 
	"http://thegentlemansarmchair.com/comic/dora-the-explorer/",
	test="http://thegentlemansarmchair.com/comic/rocks/",

	image="#comic>img",
	next="a.comic-nav-next",
),


Sarjakuva(
	"Grrl Power", 
	"grrlpower",

	"http://grrlpowercomic.com/", 
	"http://grrlpowercomic.com/archives/48",
	test="http://grrlpowercomic.com/archives/2110",

	image="#comic>img",
	next="a.navi-next",
),

Sarjakuva(
	"Goblins", 
	"goblins",

	"http://www.goblinscomic.org/", 
	"http://www.goblinscomic.org/06252005/",
	test="http://www.goblinscomic.org/01062012/",

	image="#comic>img",
	next="div.nav-next>a",
),


Sarjakuva(
	"The Great Isle of Prentil", 
	"prentil",

	"http://prentil.com/", 
	"http://prentil.com/?comic=bk1-ch1-pg1",
	test="http://prentil.com/?comic=bk1-ch4-pg19",

	image="#comic>img",
	next="a.comic-nav-next",
),


Sarjakuva(
	"Off World: The Crease", 
	"crease",

	"http://thecrease.thecomicseries.com/", 
	"http://thecrease.thecomicseries.com/comics/1",
	test="http://thecrease.thecomicseries.com/comics/325",

	image="#comic>img",
	next="a|!rel:in:next",
),


Sarjakuva(
	"Spying with Lana", 
	"spyingwithlana",

	"http://spyingwithlana.com/", 
	"http://spyingwithlana.com/comic/mxcover/",
	test="http://spyingwithlana.com/comic/ell17/",

	image="#comic>img",
	next="a.comic-nav-next",
),


Sarjakuva(
	"Puck", 
	"puck",

	"baseurl", 
	"http://www.puckcomics.com/?comic=puck-1",
	test="http://www.puckcomics.com/?comic=puck-335",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Will Save World for Gold", 
	"wswfg",

	"http://willsaveworldforgold.com/", 
	"http://willsaveworldforgold.com/?p=18",
	test="http://willsaveworldforgold.com/?p=1952",

	image="div.comicpane>img",
	next="a.navi-next",
),

Sarjakuva(
	"Vultures", 
	"alias",

	"http://vulturesblog.com/", 
	"http://vulturesblog.com/comic/one/",
	test="http://vulturesblog.com/comic/forty-four/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Gaia", 
	"gaia",

	"http://www.sandraandwoo.com/", 
	"http://www.sandraandwoo.com/gaia/2011/11/01/cover/",
	test="http://www.sandraandwoo.com/gaia/2016/05/16/monster-009/",

	image="#comic>img",
	next="div.nav-next>a",
),

Sarjakuva(
	"Sins Fugue", 
	"sinsfugue",

	"http://sincomics.com/", 
	"http://sincomics.com/index.php?1209",
	test="http://sincomics.com/index.php?1703",

	image="img|!src:in:comic/sins",
	next="a|img|!src:in:foward.jpg",
),

Sarjakuva(
	"Wapsi Square", 
	"wapsisquare",

	"http://wapsisquare.com/", 
	"http://wapsisquare.com/comic/09092001/",
	test="http://wapsisquare.com/comic/mama-bear/",

	image="#comic>img",
	next="a.comic-nav-next",
),



Sarjakuva(
	"Stick in the Mud", 
	"stickinthemud",

	"http://www.konradokonski.com/SITM/", 
	"http://www.konradokonski.com/SITM/comic/title-0001/",
	test="http://www.konradokonski.com/SITM/comic/sitm-345/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Bear Nuts", 
	"bearnuts",

	"http://www.bearnutscomic.com/", 
	"http://www.bearnutscomic.com/2008/08/17/01-bear-nuts/",
	test="http://www.bearnutscomic.com/2016/05/02/524-bear-nuts/",

	image="#comic>img",
	next="a|!text:in:next",
),

Sarjakuva(
	"Flipside", 
	"flipside",

	"http://flipside.keenspot.com/", 
	"http://flipside.keenspot.com/comic.php?i=1",
	test="http://flipside.keenspot.com/comic.php?i=2871",

	image="#flip_comicpage>img.ksc",
	next="a|!rel:in:next",
),

Sarjakuva(
	"The Dreamland Chronicles", 
	"thedreamlandchronicles",

	"http://www.thedreamlandchronicles.com/", 
	"http://www.thedreamlandchronicles.com/comic/welcome-to-the-dreamland-chronicles/",
	test="http://www.thedreamlandchronicles.com/comic/page-1836/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Mecoforie Continent", 
	"mecoforiecontinent",

	"http://mecoforie.com/", 
	"http://mecoforie.com/index.php?chapter=0&page=0",
	test="http://mecoforie.com/index.php?chapter=3&page=43",

	image="img.comicimg",
	next="a|!title:in:next",
),

Sarjakuva(
	"Demon of the Underground", 
	"demonoftheunderground",

	"http://www.bob-artist.com/demon/", 
	"http://www.bob-artist.com/demon/?id=1",
	test="http://www.bob-artist.com/demon/?id=195",

	image="#comicimg",
	next="a|!text:in:next",
),

Sarjakuva(
	"Schlock Mercenary", 
	"schlockmercenary",

	"http://www.schlockmercenary.com/", 
	"http://www.schlockmercenary.com/2000-06-12",
	test="http://www.schlockmercenary.com/2016-05-26",

	image="div.strip-images>img",
	next="a.next-strip",
),

Sarjakuva(
	"Gunnerkrigg Court", 
	"gunnerkriggcourt",

	"http://www.gunnerkrigg.com/", 
	"http://www.gunnerkrigg.com/?p=1",
	test="http://www.gunnerkrigg.com/?p=1672",

	image="img.comic_image",
	next="a|img|!src:in:next",
),

Sarjakuva(
	"Snow by Night", 
	"snowbynight",

	"http://www.snowbynight.com/", 
	"http://www.snowbynight.com/pages/ch1/pg1.php",
	test="http://www.snowbynight.com/pages/ch12/v7.php",
	parseri="snowbynight",

	image="div.comic_group>img",
	next="a.comic-nav_forward-page",
),

Sarjakuva(
	"Shotgun Shuffle", 
	"shotgunshuffle",

	"http://shotgunshuffle.com/", 
	"http://shotgunshuffle.com/comic/pilot/",
	test="http://shotgunshuffle.com/comic/who-are-you/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Housepets", 
	"housepets",

	"http://www.housepetscomic.com/", 
	"http://www.housepetscomic.com/2008/06/02/when-boredom-strikes/",
	test="http://www.housepetscomic.com/2016/05/20/seek-and-hide/",

	image="#comic>img",
	next="a.navi-next",
),

Sarjakuva(
	"Savestate", 
	"savestate",

	"http://www.savestatecomic.com/", 
	"http://www.savestatecomic.com/2014/02/pokemon-bank/",
	test="http://www.savestatecomic.com/2016/05/beach-toys/",

	image="div.comicpane>img",
	next="a.navi-next",
),

Sarjakuva(
	"Runewriters", 
	"runewriters",

	"http://runewriters.com/", 
	"http://runewriters.com/index.php?c=7",
	test="http://runewriters.com/index.php?c=176",

	image="#comic>img",
	next="a|!rel:in:next",
),

Sarjakuva(
	"JHall Pokemon", 
	"jhallpokemon",

	"http://jhallcomics.com/", 
	"http://jhallcomics.com/Pokemon/7312",
	test="http://jhallcomics.com/Pokemon/7935",

	image="#comic-container>img",
	next="a|img|!alt:in:forward",
),

Sarjakuva(
	"JHall Bloop", 
	"jhallbloop",

	"http://jhallcomics.com/", 
	"http://jhallcomics.com/Bloop/7204",
	test="http://jhallcomics.com/Bloop/7933",

	image="#comic-container>img",
	next="a|img|!alt:in:forward",
),

Sarjakuva(
	"JHall Unsorted", 
	"jhallunsorted",

	"http://jhallcomics.com/", 
	"http://jhallcomics.com/Unsorted/7216",
	test="http://jhallcomics.com/Unsorted/7956",

	image="#comic-container>img",
	next="a|img|!alt:in:forward",
),

Sarjakuva(
	"Derelict", 
	"derelict",

	"http://derelictcomic.com/", 
	"http://derelictcomic.com/?strip_id=0",
	test="http://derelictcomic.com/?strip_id=251",

	image="span.rss-content>img",
	next="a|img|!alt:in:next",
),

Sarjakuva(
	"Miss Melee", 
	"missmelee",

	"http://miss-melee.com/", 
	"http://miss-melee.com/comic/1-0/",
	test="http://miss-melee.com/comic/2-10/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Fey Winds", 
	"feywinds",

	"http://www.feywinds.com/", 
	"http://www.feywinds.com/feywinds/fw001/",
	test="http://www.feywinds.com/feywinds/test-doodle/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Exiern", 
	"exiern",

	"http://www.exiern.com/", 
	"http://www.exiern.com/2005/09/06/so-far/",
	test="http://www.exiern.com/2016/05/10/cleaning-up/",

	image="#comic>img",
	next="a.navi-next",
),

Sarjakuva(
	"Spindrift", 
	"spindrift",

	"http://www.spindrift-comic.com/", 
	"http://www.spindrift-comic.com/comic/00/0",
	test="http://www.spindrift-comic.com/comic/02/97",

	image="#comic-image",
	next="li.c-nav-6>a",
),

Sarjakuva(
	"How to be a Werewolf", 
	"howtobeawerewolf",

	"http://www.howtobeawerewolf.com/", 
	"http://www.howtobeawerewolf.com/comic/coming-february-3rd/",
	test="http://www.howtobeawerewolf.com/comic/hands/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"3 Minute Max", 
	"3minutemax",

	"http://www.3mm-crisisstrike.com/", 
	"http://www.3mm-crisisstrike.com/3mmcomic/activation/",
	test="http://www.3mm-crisisstrike.com/3mmcomic/hard-target-page-four/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Out of My Element", 
	"outofmyelement",

	"http://www.oomecomic.com/", 
	"http://www.oomecomic.com/comic/ch1-cover/",
	test="http://www.oomecomic.com/comic/ch8-14/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Dream Scar", 
	"dreamscar",

	"http://www.dream-scar.net/", 
	"http://www.dream-scar.net/?id=1",
	test="http://www.dream-scar.net/?id=285",

	image="#comic",
	next="#page_nav_next",
),

Sarjakuva(
	"Giant Girl Adventures", 
	"giantgirl",

	"http://www.giantgirladventures.com/", 
	"http://www.giantgirladventures.com/comics/iss1-cover",
	test="http://www.giantgirladventures.com/comics/iss15pg10",

	image="#comic>img",
	next="a.next",
),

Sarjakuva( #js helpottais
	"Scurry", 
	"scurry",

	"http://www.scurrycomic.com/", 
	"http://www.scurrycomic.com/scurry-comic/2016/1/17/comic-01-00",
	test="http://www.scurrycomic.com/scurry-comic/2016/5/23/scurry-pg37",

	image="noscript>img",
	next="a.archive-item-link",
),

Sarjakuva(
	"Shattered Starlight", 
	"shatteredstarlight",

	"http://www.shatteredstarlight.com/", 
	"http://www.shatteredstarlight.com/shattered-starlight/coming-soon/",
	test="http://www.shatteredstarlight.com/shattered-starlight/page-13/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Precocious", 
	"precocious",

	"http://www.precociouscomic.com/", 
	"http://www.precociouscomic.com/archive/comic/2009/03/09",
	test="http://www.precociouscomic.com/archive/comic/2016/05/27",

	image="div.comicContent>img|!src:in:comics/",
	next="a|img|!src:in:next_arrow",
),

Sarjakuva(
	"Freefall", 
	"freefall",

	"http://freefall.purrsia.com/", 
	"http://freefall.purrsia.com/ff100/fv00001.htm",
	test="http://freefall.purrsia.com/ff2900/fc02812.htm",

	image="img",
	next="a|!text:in:next",
),

Sarjakuva(
	"Blade Bunny", 
	"bladebunny",

	"http://www.bladebunny.com/", 
	"http://www.bladebunny.com/comic/bunny-blade-cover-final/",
	test="http://www.bladebunny.com/comic/just-kiss-2/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Quantum Vibe", 
	"quantumvibe",

	"http://www.quantumvibe.com/", 
	"http://www.quantumvibe.com/strip?page=1",
	test="http://www.quantumvibe.com/strip?page=1350",

	image="img|!alt:in:strip",
	next="a|div|img|!src:in:nextstrip",
),

Sarjakuva(
	"Amya", 
	"amya",

	"http://www.amyachronicles.com/", 
	"http://www.amyachronicles.com/archives/comic/09292009",
	test="http://www.amyachronicles.com/archives/comic/guest-art-by-autumn-dickens",

	image="#comic>img",
	next="a.comic-nav-next",
),



Sarjakuva(
	"No Need for Bushido", 
	"noneedforbushido",

	"http://nn4b.com/", 
	"http://nn4b.com/comic/1",
	test="http://nn4b.com/comic/653",

	image="#comic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Earthsong", 
	"earthsong",

	"http://earthsongsaga.com/", 
	"http://earthsongsaga.com/vol1/ch1cover.php",
	test="http://earthsongsaga.com/vol5/104.php",

	image="#comic>img",
	next="#next>a",
),

Sarjakuva(
	"Blade Under Mask", 
	"bladeundermask",

	"http://bladeundermask.com/", 
	"http://bladeundermask.com/comic/en/",
	test="http://bladeundermask.com/comic/en/",

	image="img.img-responsive",
	next="a|!text:in:>",

	parseri="dragonarte",
),

Sarjakuva(
	"Hero on Hero", 
	"heroonhero",

	"http://www.neorice.com/", 
	"http://www.neorice.com/hoh_1",
	test="http://www.neorice.com/hoh_625",

	image="#comic>img",
	next="a|img|!alt:in:next",
),

Sarjakuva(
	"164 days", 
	"164days",

	"http://164days.co.uk/", 
	"http://164days.co.uk/comic/prologue/08012011/",
	test="http://164days.co.uk/comic/filler/thanks-for-reading/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Supervillainous", 
	"supervillainous",

	"http://supervillainous.spiderforest.com/", 
	"http://supervillainous.spiderforest.com/comic/comic-1-work-and-family/",
	test="http://supervillainous.spiderforest.com/comic/ya-think-ya-know-a-guy/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Reality Quest", 
	"realityquest",

	"http://rq.skyrocketcreation.com/", 
	"http://rq.skyrocketcreation.com/comic/001-the-misadventures-begin/",
	test="http://rq.skyrocketcreation.com/comic/114-children-part-15/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Yesterday Bound", 
	"yesterdaybound",

	"http://yesterdaybound.webcomic.ws/", 
	"http://yesterdaybound.webcomic.ws/comics/1",
	test="http://yesterdaybound.webcomic.ws/comics/129",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"A Redtails Dream", 
	"redtailsdream",

	"http://www.minnasundberg.fi/comic/", 
	"http://www.minnasundberg.fi/comic/page00.php",
	test="http://www.minnasundberg.fi/comic/page553.php",

	image="#page>img",
	next="a|img|!src:in:anext",
	interval=0,
),

Sarjakuva(
	"Ryugou", 
	"ryugou",

	"bahttp://ryugou.swashbuckledcomics.com/seurl", 
	"http://ryugou.swashbuckledcomics.com/comic/ryugou-chapter-1-cover/",
	test="http://ryugou.swashbuckledcomics.com/comic/7three/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Widdershins", 
	"widdershins",

	"http://www.widdershinscomic.com/", 
	"http://www.widdershinscomic.com/wdshn/sleight-of-hand-cover/",
	test="http://www.widdershinscomic.com/wdshn/may-17th-2016/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Salamanstra", 
	"salamanstra",

	"http://salamanstra.keenspot.com/", 
	"http://salamanstra.keenspot.com/d/20140315.html",
	test="http://salamanstra.keenspot.com/d/20160523.html",

	image="img.ksc",
	next="a|!rel:in:next",
),



Sarjakuva(
	"Blonde Sunrise", 
	"blondesunrise",

	"http://www.blondesunrise.com/", 
	"http://www.blondesunrise.com/comic.php?page=1",
	test="http://www.blondesunrise.com/comic.php?page=406",

	image="img|!src:in:comic_imgs",
	next="a|img|!src:in:next",
),

Sarjakuva(
	"The Book of Lies", 
	"bookoflies",

	"http://bookofliescomic.webcomic.ws/", 
	"http://bookofliescomic.webcomic.ws/comics/1",
	test="http://bookofliescomic.webcomic.ws/comics/248",

	image="#comicimagewrap>img",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Its New Day", 
	"itsnewday",

	"http://itsnewday.thecomicseries.com/", 
	"http://itsnewday.thecomicseries.com/comics/1/",
	test="http://itsnewday.thecomicseries.com/comics/89/",

	image="#comicimagewrap>img",
	next="a|!rel:in:next",
),

Sarjakuva(
	"The Beast Legion", 
	"beastlegion",

	"http://www.thebeastlegion.com/", 
	"http://www.thebeastlegion.com/comic/chapter-1-darkness-rising/",
	test="http://www.thebeastlegion.com/comic/issue-12-extra-page-3-the-shield/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Suihira", 
	"suihira",

	"http://www.suihira.com/", 
	"http://www.suihira.com/comics/2052554/1-acuere-page-1/",
	test="http://www.suihira.com/comics/2286645/3-ferus-page-17/",

	image="#comic_image",
	next="a|img|!alt:in:next",
),

Sarjakuva(
	"Modest Medusa", 
	"modestmedusa",

	"http://modestmedusa.com/", 
	"http://modestmedusa.com/comic/christmas-eve-3/",
	test="http://modestmedusa.com/comic/overwatch-medusa/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Frivolesque", 
	"frivolesque",

	"http://frivolesque.com/", 
	"http://frivolesque.com/archives/comic/frivolesque",
	test="http://frivolesque.com/archives/comic/160-invitation",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"General Protection Fault", 
	"generalprotectionfault",

	"http://www.gpf-comics.com/", 
	"http://www.gpf-comics.com/archive/2016/05/23",
	test="http://www.gpf-comics.com/archive/2016/05/23",

	image="div.content>img|!src:in:/comics/",
	next="span.nav_link_forward>a",
),

Sarjakuva(
	"Ramen Empire", 
	"ramenempire",

	"http://ramen-empire.com/", 
	"http://ramen-empire.com/strip/afterglow_cover/",
	test="http://ramen-empire.com/strip/phoenix-down-1/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Rune Hunters", 
	"runehunters",

	"http://www.runehunters.com/", 
	"http://www.runehunters.com/2008/05/10/rune-hunters-ch-1-cover/",
	test="http://www.runehunters.com/2016/05/08/rune-hunters-chapter-12-page-8/",

	image="#comic>img",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Middleways", 
	"middleways",

	"http://www.middleways.net/", 
	"http://www.middleways.net/comic/page-1/",
	test="http://www.middleways.net/comic/chapter-10/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Autumn Bay", 
	"autumnbay",

	"http://autumnbaycomics.com/", 
	"http://autumnbaycomics.com/comics/1",
	test="http://autumnbaycomics.com/comics/106/",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"League of Super Redundant Heroes", 
	"superredundant",

	"http://superredundant.com/", 
	"http://superredundant.com/?comic=meet-the-gang",
	test="http://superredundant.com/?comic=549-judgement",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Doc Rat", 
	"docrat",

	"http://www.docrat.com.au/", 
	"http://www.docrat.com.au/comic/begin-with-eye-contact/",
	test="http://www.docrat.com.au/comic/eland-gag/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Eternal Knights", 
	"eternalknights",

	"http://eternalknights.thecomicseries.com/", 
	"http://eternalknights.thecomicseries.com/comics/1/",
	test="http://eternalknights.thecomicseries.com/comics/128/",

	image="#authornotes>div.commentcontent>center>img",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Mega Tokyo", 
	"megatokyo",

	"http://megatokyo.com/", 
	"http://megatokyo.com/strip/1",
	test="http://megatokyo.com/strip/1445",

	image="#strip-bl>img",
	next="li.next>a",
),


Sarjakuva(
	"M.F.K", 
	"mfk",

	"http://www.mfkcomic.com/", 
	"http://www.mfkcomic.com/comic/chapter-1-page-1-2/",
	test="http://www.mfkcomic.com/comic/chapter-4-page-15/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Planet Chaser", 
	"planetchaser",

	"http://planetchaser.thecomicseries.com/", 
	"http://planetchaser.thecomicseries.com/comics/1",
	test="http://planetchaser.thecomicseries.com/comics/312/",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Unknown Lands", 
	"unknownlands",

	"http://unknownlands.thecomicseries.com/", 
	"http://unknownlands.thecomicseries.com/comics/1/",
	test="http://unknownlands.thecomicseries.com/comics/94/",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"The Underdogs", 
	"underdogs",

	"http://underdogscomic.com/", 
	"http://underdogscomic.com/udcomic/issue-1/underdogs-issue-1-page-1/",
	test="http://underdogscomic.com/udcomic/issue-3/underdogs-issue-3-page-10/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Endtown", 
	"endtown",

	"http://www.gocomics.com/", 
	"http://www.gocomics.com/endtown/2009/01/19",
	test="http://www.gocomics.com/endtown/2016/05/20",

	image="img.strip",
	next="ul.feature-nav>a.next",
),

Sarjakuva(
	"B.C", 
	"bc",

	"http://www.gocomics.com/", 
	"http://www.gocomics.com/bc/2002/01/01",
	test="http://www.gocomics.com/bc/2016/05/27",

	image="img.strip",
	next="ul.feature-nav>a.next",
),



Sarjakuva(
	"Uber Quest", 
	"uberquest",

	"http://uberquest.katbox.net/", 
	"http://uberquest.katbox.net/comic/an-uber-start/",
	test="http://uberquest.katbox.net/comic/149-these-old-bones/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"White Noise", 
	"whitenoise",

	"http://whitenoisecomic.com/", 
	"http://whitenoisecomic.com/comic/book-one/",
	test="http://whitenoisecomic.com/comic/page-43-chapter-10/",

	image="#comic>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Las Lindas", 
	"laslindas",

	"http://laslindas.katbox.net/", 
	"http://laslindas.katbox.net/comic/day-one/",
	test="http://laslindas.katbox.net/comic/homecoming-4/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"False Start", 
	"falsestart",

	"http://falsestart.katbox.net/", 
	"http://falsestart.katbox.net/comic/issue-1-cover/",
	test="http://falsestart.katbox.net/comic/issue-2-page-9/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Desert Fox", 
	"desertfox",

	"http://desertfox.katbox.net/", 
	"http://desertfox.katbox.net/comic/origins-1/",
	test="http://desertfox.katbox.net/comic/page-2/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Itsy Bitsy Adventures", 
	"itsybitsyadventures",

	"http://iba.katbox.net/", 
	"http://iba.katbox.net/comic/fight-the-machine/",
	test="http://iba.katbox.net/comic/page-52/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Peter and Whitney", 
	"peterandwhitney",

	"http://peterandwhitney.katbox.net/", 
	"http://peterandwhitney.katbox.net/comic/comic-1-graduation-day/",
	test="http://peterandwhitney.katbox.net/comic/comic-1-graduation-day/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Peter and Company", 
	"peterandcompany",

	"http://peterandcompany.katbox.net/", 
	"http://peterandcompany.katbox.net/comic/strip-1/",
	test="http://peterandcompany.katbox.net/comic/comic-246-jake-the-jerk/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Addictive Science", 
	"addictive science",

	"http://addictivescience.katbox.net/", 
	"http://addictivescience.katbox.net/comic/page-1/",
	test="http://addictivescience.katbox.net/comic/the-concquerors-7/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Our World", 
	"ourworld",

	"http://ourworld.katbox.net/", 
	"http://ourworld.katbox.net/comic/title-page/",
	test="http://ourworld.katbox.net/comic/night-watch/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),


Sarjakuva(
	"Mousechievous", 
	"mousechievous",

	"http://mousechievous.katbox.net/", 
	"http://mousechievous.katbox.net/comic/01-vacation/",
	test="http://mousechievous.katbox.net/comic/01-vacation/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),


Sarjakuva(
	"The Draconia Chronicles", 
	"dragoniachronicles",

	"http://draconia.katbox.net/", 
	"http://draconia.katbox.net/comic/chapter-1-page-1/",
	test="http://draconia.katbox.net/comic/page-387/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),


Sarjakuva(
	"Practise Makes Perfect", 
	"practisemakesperfect",

	"http://pmp.katbox.net/", 
	"http://pmp.katbox.net/comic/001-procrastination/",
	test="http://pmp.katbox.net/comic/001-procrastination/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),


Sarjakuva(
	"Paprika", 
	"paprika",

	"http://paprika.katbox.net/", 
	"http://paprika.katbox.net/comic/001-revolution/",
	test="http://paprika.katbox.net/comic/054-tina-online/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),


Sarjakuva(
	"Caribbean Blue", 
	"caribbeanblue",

	"http://cblue.katbox.net/", 
	"http://cblue.katbox.net/comic/caribbean-blue/",
	test="http://cblue.katbox.net/comic/002-steve-ii/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
	interval=0,
),


Sarjakuva(
	"iMew", 
	"imew",

	"http://imew.katbox.net/", 
	"http://imew.katbox.net/comic/imew/",
	test="http://imew.katbox.net/comic/46-cornered/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
	interval=0,
),


Sarjakuva(
	"Project Zero 6", 
	"projectzero6",

	"http://projectzero.katbox.net/", 
	"http://projectzero.katbox.net/comic/project-zero-cover/",
	test="http://projectzero.katbox.net/comic/i-want-out/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Knuckle Up", 
	"knuckleup",

	"http://knuckleup.katbox.net/", 
	"http://knuckleup.katbox.net/comic/knuckleup-prologue1/",
	test="http://knuckleup.katbox.net/comic/happy-new-years-2016/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Rascals", 
	"rasals",

	"http://rascals.katbox.net/", 
	"http://rascals.katbox.net/comic/rascals-cover/",
	test="http://rascals.katbox.net/comic/340-the-rebound/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Artificial Incident", 
	"artificialincident",

	"http://ai.katbox.net/", 
	"http://ai.katbox.net/comic/issue-one-life-changing/",
	test="http://ai.katbox.net/comic/prologue-2/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Yosh!", 
	"yosh",

	"http://yosh.katbox.net/", 
	"http://yosh.katbox.net/comic/introduction/",
	test="http://yosh.katbox.net/comic/plan-a-failed/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"DMFA", 
	"dmfa",

	"http://dmfa.katbox.net/", 
	"http://dmfa.katbox.net/comic/1-the-story-begins/",
	test="http://dmfa.katbox.net/comic/1663-dodged-a-blt-there/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Anthronauts", 
	"anthronauts",

	"http://anthronauts.katbox.net/", 
	"http://anthronauts.katbox.net/ar/comic/rational-thought/",
	test="http://anthronauts.katbox.net/ar/comic/final-boss-soap/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
	interval=0
),

Sarjakuva(
	"Tine of the South", 
	"tinaofthesouth",

	"http://tinaofthesouth.katbox.net/", 
	"http://tinaofthesouth.katbox.net/comic/wanted-alive-3-chins-joe-001/",
	test="http://tinaofthesouth.katbox.net/comic/the-pride-of-the-huntress-11/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"The Eye", 
	"eye",

	"http://theeye.katbox.net/", 
	"http://theeye.katbox.net/comic/boxes-and-memories/",
	test="http://theeye.katbox.net/comic/ben-the-meatshield/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Blue Milk Special", 
	"bluemilkspecial",

	"http://www.bluemilkspecial.com/", 
	"http://www.bluemilkspecial.com/comic/in-the-beginning/",
	test="http://www.bluemilkspecial.com/comic/furry-friends/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Silver", 
	"silver",

	"http://sil-ver.thecomicseries.com/", 
	"http://sil-ver.thecomicseries.com/comics/1",
	test="http://sil-ver.thecomicseries.com/comics/194",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Alvery Nerveaux's Secret Case Files", 
	"alverynerveaux",

	"http://alverynerveaux.thecomicseries.com/", 
	"http://alverynerveaux.thecomicseries.com/comics/1/",
	test="http://alverynerveaux.thecomicseries.com/comics/19/",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Mindless Designs", 
	"mindlessdesigns",

	"http://mindlessdesigns.com/", 
	"http://mindlessdesigns.com/comic/magnor/cover-1-3/",
	test="http://mindlessdesigns.com/comic/magnor/magnor-page-23/",

	image="#comic>img",
	next="a.navi-next-in",
),

Sarjakuva(
	"The Devils Panties", 
	"devilspanties",

	"http://thedevilspanties.com/", 
	"http://thedevilspanties.com/archives/300",
	test="http://thedevilspanties.com/archives/11332",

	image="#comic>img",
	next="a.navi-next",
),

Sarjakuva(
	"Bicycle Boy", 
	"bicycleboy",

	"http://bicycleboy.thecomicseries.com/", 
	"http://bicycleboy.thecomicseries.com/comics/first/",
	test="http://bicycleboy.thecomicseries.com/comics/167/",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Live Nude Ghouls", 
	"livenudeghouls",

	"http://livenudeghouls.com/", 
	"http://livenudeghouls.com/post/66544858920/welcome-to-the-premiere-of-live-nude-ghouls-it",
	test="http://livenudeghouls.com/post/143842112134/live-nude-ghouls-54-if-you-are-a-new-viewer-and",

	image="article>figure.photo-item>img",
	next="a|!text:in:next",
),

Sarjakuva(
	"Everblue", 
	"everblue",

	"http://www.everblue-comic.com/", 
	"http://www.everblue-comic.com/comic?sort=1",
	test="http://www.everblue-comic.com/comic?sort=248",

	image="img|!itemprop:in:image",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Soul to Call", 
	"soultocall",

	"http://soultocall.com/", 
	"http://soultocall.com/?id=1",
	test="http://soultocall.com/?id=270",

	image="#comicimg",
	next="a|img|!src:in:nexta",
),

Sarjakuva(
	"Accursed Dragon", 
	"accurseddragon",

	"http://www.accurseddragon.com/", 
	"http://www.accurseddragon.com/index.php?date=2008-10-06",
	test="http://www.accurseddragon.com/index.php?date=2016-04-13",

	image="#comic-image>img",
	next="li.nextlink>a",
),

Sarjakuva(
	"Three Panel Soul", 
	"threepanelsoul",

	"http://www.threepanelsoul.com/", 
	"http://www.threepanelsoul.com/comic/a-test-comic",
	test="http://www.threepanelsoul.com/comic/authenticity",

	image="#cc-comic",
	next="a.next",
),

Sarjakuva(
	"Between Failures", 
	"betweenfailures",

	"http://betweenfailures.com/", 
	"http://betweenfailures.com/comics1/every-story-has-to-start-somewhere",
	test="http://betweenfailures.com/comics1/1539-special-infected",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Iron Violet", 
	"ironviolet",

	"http://ironvioletcomic.com/", 
	"http://ironvioletcomic.com/?comic=iron-violet-issue-1-cover",
	test="http://ironvioletcomic.com/?comic=issue-5-page-5",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Evon", 
	"evon",

	"http://evoncomics.com/", 
	"http://evoncomics.com/?comic=chapter-1",
	test="http://evoncomics.com/?comic=volume-four-chapter-18-page-694",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Tistow", 
	"tistow",

	"http://tistow.uk/comic/", 
	"http://tistow.uk/comic/page0.php",
	test="http://tistow.uk/comic/page65.php",

	image="#comicspread>img",
	next="a.next",
),

Sarjakuva(
	"G-Girl", 
	"ggirl",

	"http://www.heroicmultiverse.com/ggirl/webcomic/", 
	"http://www.heroicmultiverse.com/ggirl/webcomic/index.php?pn=1",
	test="http://www.heroicmultiverse.com/ggirl/webcomic/index.php?pn=170",

	image="#centerfull>img|!src:in:img/",
	next="a|img|!src:in:arrowright",
),

Sarjakuva(
	"Wastelanders", 
	"wastelanders",

	"http://wastelanders.webcomic.ws/", 
	"http://wastelanders.webcomic.ws/comics/first/",
	test="http://wastelanders.webcomic.ws/comics/313/",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Waffles and Pancakes", 
	"wafflesandpancakes",

	"http://wandpcomic.com/", 
	"http://wandpcomic.com/index.php/comic/1/",
	test="http://wandpcomic.com/index.php/comic/30-if-i-were-a-god/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"PhD", 
	"phd",

	"http://phdcomics.com/comics/", 
	"http://phdcomics.com/comics/archive.php?comicid=1",
	test="http://phdcomics.com/comics/archive.php?comicid=1881",

	image="#comic",
	next="a|img|!src:in:next_button",
),

Sarjakuva(
	"Nightlight", 
	"nightlight",

	"http://nightlight.thecomicseries.com/", 
	"http://nightlight.thecomicseries.com/comics/1/",
	test="http://nightlight.thecomicseries.com/comics/21/",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Normal", 
	"normal",

	"http://normalcomic.thecomicseries.com/", 
	"http://normalcomic.thecomicseries.com/comics/1/",
	test="http://normalcomic.thecomicseries.com/comics/43/",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Sombulus", 
	"sombulus",

	"http://www.sombulus.com/", 
	"http://www.sombulus.com/comic/1",
	test="http://www.sombulus.com/comic/617",

	image="#page>img|!alt:in:comic",
	next="a.next",
),

Sarjakuva(
	"My Life With Fel", 
	"mylifewithfel",

	"http://www.mylifewithfel.com/", 
	"http://www.mylifewithfel.com/comics/1047001/comic-cover/",
	test="http://www.mylifewithfel.com/comics/2283444/301/",

	image="#comic_image",
	next="li.next>a",
),

Sarjakuva(
	"Over Eyes", 
	"overeyes",

	"http://overeyes.rude-owl.pl/", 
	"http://overeyes.rude-owl.pl/comic/waking-up/",
	test="http://overeyes.rude-owl.pl/comic/two-madness/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Dork Tower", 
	"dorktower",

	"http://www.dorktower.com/", 
	"http://www.dorktower.com/1997/01/01/shadis-magazine-strip-1/",
	test="http://www.dorktower.com/2016/05/12/life-changing-magic-dork-tower-12-05-16/",

	image="#content>div.entry-content>img",
	next="p.comic-nav>a|!text:in:next",
),

Sarjakuva(
	"Savage Sword of Sharona", 
	"savageswordofsharona",

	"http://savageswordofsharona.com/", 
	"http://savageswordofsharona.com/comic/qfdcover/",
	test="http://savageswordofsharona.com/comic/tog14/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Bruno Harm", 
	"brunoharm",

	"http://brunoharm.thecomicseries.com/", 
	"http://brunoharm.thecomicseries.com/comics/1/",
	test="http://brunoharm.thecomicseries.com/comics/55/",

	image="#comicimage",
	next="#next",
),

Sarjakuva(
	"Terra", 
	"terra",

	"http://terra-comic.com/", 
	"http://terra-comic.com/wordpress/archives/comic/prologue",
	test="http://terra-comic.com/wordpress/archives/comic/page-340",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Shadowbinders", 
	"shadowbinders",

	"http://shadowbinders.com/", 
	"http://shadowbinders.com/comic/shadowbinders-chapter-1/",
	test="http://shadowbinders.com/comic/shadowbinders-419-chapter-12-page-10/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Love Debut", 
	"lovedebut",

	"http://lovedebutcomic.com/", 
	"http://lovedebutcomic.com/read/cover/",
	test="http://lovedebutcomic.com/read/page-135/",

	image="div.webcomic-image>img",
	next="a.next-webcomic-link",
),

Sarjakuva(
	"Two Guys and a Guy", 
	"twogag",

	"http://www.twogag.com/", 
	"http://www.twogag.com/archives/4",
	test="http://www.twogag.com/archives/3683",

	image="#comic>img",
	next="a.navi-next",
),

Sarjakuva(
	"The Black Enchantress", 
	"blackenchantress",

	"http://www.heroicmultiverse.com/blackenchantress/webcomic/", 
	"http://www.heroicmultiverse.com/blackenchantress/webcomic/index.php?pn=1",
	test="http://www.heroicmultiverse.com/blackenchantress/webcomic/index.php?pn=71",

	image="#centerfull>img|!src:in:img/",
	next="a|img|!src:in:arrowright",
),

Sarjakuva(
	"Murcielaga She-Bat", 
	"shebat",

	"http://www.heroicmultiverse.com/shebat/webcomic/", 
	"http://www.heroicmultiverse.com/shebat/webcomic/index.php?pn=1",
	test="http://www.heroicmultiverse.com/shebat/webcomic/index.php?pn=260",

	image="#centerfull>img|!src:in:img/",
	next="a|img|!src:in:arrowright",
),

Sarjakuva(
	"The League of Champions", 
	"leagueofchampions",

	"http://www.heroicmultiverse.com/league/webcomic/", 
	"http://www.heroicmultiverse.com/league/webcomic/index.php?pn=1",
	test="http://www.heroicmultiverse.com/league/webcomic/index.php?pn=160",

	image="#centerfull>img|!src:in:img/",
	next="a|img|!src:in:arrowright",
),

Sarjakuva(
	"Flare", 
	"flare",

	"http://www.heroicmultiverse.com/flare/webcomic/", 
	"http://www.heroicmultiverse.com/flare/webcomic/index.php?pn=1",
	test="http://www.heroicmultiverse.com/flare/webcomic/index.php?pn=720",

	image="#centerfull>img|!src:in:img/",
	next="a|img|!src:in:arrowright",
),

Sarjakuva(
	"Fine Sometimes Rain", 
	"finesometimesrain",

	"http://finesometimesrain.genkigirl.com/", 
	"http://genkigirl.com/finesometimesrain/?comic=fine-sometimes-rain-chapter-01-cover",
	test="http://genkigirl.com/finesometimesrain/?comic=fine-sometimes-rain-chapter-07-p15",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"The Secrets of the Afterlife", 
	"secretsoftheafterlife",

	"http://thesecretsoftheafterlife.webcomic.ws/", 
	"http://thesecretsoftheafterlife.webcomic.ws/comics/2",
	test="http://thesecretsoftheafterlife.webcomic.ws/comics/55/",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Black and Blue", 
	"blackandblue",

	"http://www.blackandbluecomic.com/", 
	"http://www.blackandbluecomic.com/comic/page-01/",
	test="http://www.blackandbluecomic.com/comic/page-177/",

	image="#content>article.comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Charby the Vampirate", 
	"charbythevampirate",

	"http://www.charbythevampirate.com/", 
	"http://www.charbythevampirate.com/comic/1",
	test="http://www.charbythevampirate.com/comic/1070",

	image="#content>article>div.content>img|!src:in:/comics/",
	next="a.next",
),

Sarjakuva(
	"Here There Be Monsters", 
	"heretherebemonsters",

	"http://www.heretherebemonsters.us/", 
	"http://www.heretherebemonsters.us/comic/1",
	test="http://www.heretherebemonsters.us/comic/28",

	image="#content>article>div.content>img|!src:in:/comics/",
	next="a.next",
),


Sarjakuva(
	"Station V3", 
	"stationv3",

	"http://www.stationv3.com/", 
	"http://www.stationv3.com/d2/20150628.html",
	test="http://www.stationv3.com/d2/20160525.html",

	image="#middle>img|!src:in:comics",
	next="a|img|!src:in:next",
),

Sarjakuva(
	"Armless Amy", 
	"armlessamy",

	"http://armlessamy.thecomicseries.com/", 
	"http://armlessamy.thecomicseries.com/comics/first/",
	test="http://armlessamy.thecomicseries.com/comics/325/",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Ashes", 
	"ashes",

	"http://ashescomic.webcomic.ws/", 
	"http://ashescomic.webcomic.ws/comics/first/",
	test="http://ashescomic.webcomic.ws/comics/229/",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Chirault", 
	"chirault",

	"http://chirault.sevensmith.net/", 
	"http://chirault.sevensmith.net/?comic_id=0",
	test="http://chirault.sevensmith.net/?comic_id=1080-13",

	image="img|!src:in:comics",
	next="a|img|!alt:in:next",
),

Sarjakuva(
	"M9 Girls", 
	"m9girls",

	"http://m9girls.com/webcomic/en/", 
	"http://m9girls.com/webcomic/en/2011/09/07/m9-girls-cover/",
	test="http://m9girls.com/webcomic/en/2016/04/22/fall-into-darkness/",

	image="#comic>img",
	next="a.navi-next-in",
),

Sarjakuva(
	"Monster Soup", 
	"monstersoup",

	"http://monstersoupcomic.com/", 
	"http://monstersoupcomic.com/?comic=chapter-1-cover",
	test="http://monstersoupcomic.com/?comic=page-32-the-visitors",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Twitlight Trust", 
	"twilighttrust",

	"http://twilighttrust.thecomicseries.com/", 
	"http://twilighttrust.thecomicseries.com/comics/1",
	test="http://twilighttrust.thecomicseries.com/comics/548/",

	image="#comicimage",
	next="a|!rel:in:next",
),

Sarjakuva(
	"Electric Bunny", 
	"electricbunny",

	"http://electricbunnycomics.com/", 
	"http://electricbunnycomics.com/View/Comic/1/My+first+day",
	test="http://electricbunnycomics.com/View/Comic/161/Seduca+Medusa",

	image="div.comic_container>img",
	next="div.comic_navbar>a|img|!alt:in:next",
),

Sarjakuva(
	"C-Cassandra", 
	"c-cassandra",

	"http://c-cassandra.tumblr.com/", 
	"http://c-cassandra.tumblr.com/post/90510288035/exploring-different-cartoon-illustration-styles",
	test="http://c-cassandra.tumblr.com/post/146923200625",

	image="#content>div.post>img",
	next="div.new>a",
),

Sarjakuva(
	"Uber Steffen", 
	"ubersteffen",

	"http://www.ubersteffen.com/", 
	"http://www.ubersteffen.com/comic/useng1/",
	test="http://www.ubersteffen.com/comic/beautifools/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Gone Into Rapture", 
	"goneintorapture",

	"http://goneintorapture.com/", 
	"http://goneintorapture.com/post/77402242022",
	test="http://goneintorapture.com/post/144750855591",

	image="article.post>figure.photo-hires-item>img",
	next="a.next-button",
),

Sarjakuva(
	"Respawn", 
	"respawn",

	"http://respawncomic.com/", 
	"http://respawncomic.com/comic/c0001/",
	test="http://respawncomic.com/comic/c0072/",

	image="div.jetpack-image-container>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Soggy Cardboard", 
	"soggycardboard",

	"http://www.soggycardboard.com/", 
	"http://www.soggycardboard.com/?comic=001-new-friends-1",
	test="http://www.soggycardboard.com/?comic=084-fuck-you-mrs-lana",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	u"Inspector Dangers Crime-Quiz", 
	u"inspectordangers",

	u"http://www.gocomics.com/", 
	u"http://www.gocomics.com/inspector-dangers-crime-quiz/2011/08/01",
	test="http://www.gocomics.com/inspector-dangers-crime-quiz/2016/06/27",

	image="img.strip",
	next="ul.feature-nav>a.next",
),

Sarjakuva(
	"Sarahs Scribbles", 
	"sarahsscribbles",

	"http://www.gocomics.com/", 
	"http://www.gocomics.com/sarahs-scribbles/2014/01/02",
	test="http://www.gocomics.com/sarahs-scribbles/2016/07/03",

	image="img.strip",
	next="ul.feature-nav>a.next",
),

Sarjakuva(
	"In the Bleachers", 
	"inthebleachers",

	"http://www.gocomics.com/", 
	"http://www.gocomics.com/inthebleachers/2016/07/10",
	test="http://www.gocomics.com/inthebleachers/2016/07/10",

	image="img.strip",
	next="ul.feature-nav>a.next",
),


Sarjakuva(
	"Books of Adam", 
	"booksofadam",

	"http://booksofadam.tumblr.com/", 
	"http://booksofadam.tumblr.com/rss",
	#test="testurl",

	#image="imagetree",
	#next="nextlinktree",
	parseri="rssreader"
),

Sarjakuva(
	"clearlymissherd", 
	"clearlymissherd",

	"http://clearlymissherd.com/", 
	"http://clearlymissherd.com/mother-knows-best/",
	test="http://clearlymissherd.com/thatll-teach-you-human/",

	image="div.webcomic-img>img",
	next="nav.webcomics>a|img|!alt:in:next",
),

Sarjakuva(
	"Our Super Adventure", 
	"oursuperadventure",

	"http://www.oursuperadventure.com/", 
	"http://www.oursuperadventure.com/comic/2013-03-02/",
	test="http://www.oursuperadventure.com/comic/20th-june-2016/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Fanboys", 
	"fanboys",

	"http://fanboys-online.com/", 
	"http://fanboys-online.com/index.php?id=483",
	test="http://fanboys-online.com/index.php?id=547",

	image="#comicbody>img",
	next="div.nav>a.next",
),

Sarjakuva(
	"Mary Death", 
	"marydeath",

	"http://www.marydeathcomics.com/", 
	"http://www.marydeathcomics.com/archives/comic/01172013",
	test="http://www.marydeathcomics.com/archives/comic/solitude",

	image="#comic>img",
	next="a.navi-next",
),

Sarjakuva(
	"Bartenerds", 
	"bartenerds",

	"http://www.bartenerds.com/archive/", 
	"http://www.bartenerds.com/archive/10-01-2012.html",
	test="http://www.bartenerds.com/archive/07-29-2016.html",

	image="#comic>img",
	next="#forw>a",
),

Sarjakuva(
	"Walking from Work", 
	"walkingfromwork",

	"http://walkingfromwork.com/", 
	"http://walkingfromwork.com/archives/comic/champ-3",
	test="http://walkingfromwork.com/archives/comic/shower",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"Tales of Absurdity", 
	"talesofabsurdity",

	"http://talesofabsurdity.com/", 
	"http://talesofabsurdity.com/comic/the-magic-well/",
	test="http://talesofabsurdity.com/comic/scarcity/",

	image="#comic>img",
	next="a.comic-nav-next",
),

Sarjakuva(
	"XY Gaming", 
	"xygaming",

	"http://www.xygaming.com/", 
	"http://www.xygaming.com/comic/1",
	test="http://www.xygaming.com/comic/47",

	image="div.container>div.p-0>img",
	next="a|button|i.fa-chevron-right",
),

Sarjakuva(
	"Optipess", 
	"optipess",

	"http://www.optipess.com/2008/", 
	"http://www.optipess.com/2008/12/01/jason-friend-of-the-butterflies/",
	test="http://www.optipess.com/2017/02/14/crush-counter/",

	image="#comic>img",
	next="a.navi-next",
),

Sarjakuva(
	"How Baby", 
	"howbaby",

	"http://howbabycomic.com/", 
	"http://howbabycomic.com/comic/how-baby-1-the-first-day/",
	test="http://howbabycomic.com/comic/hb184/",

	image="#comic>img",
	next="a.navi-next",
),

Sarjakuva(
	"Theism", 
	"theism",

	"http://www.theism-comics.com/", 
	"http://www.theism-comics.com/main/different-economic-approaches-to-market-stagnation/",
	test="http://www.theism-comics.com/main/the-spinning-news/",

	image=".webcomic-image>img",
	next="a.next-webcomic-link",
),


Sarjakuva(
	"Could be Worse", 
	"couldbeworse",

	"http://couldbeworse-comic.com/", 
	"http://couldbeworse-comic.com/055.html",
	test="http://couldbeworse-comic.com/425.html",

	image="#mainComic>img",
	next="a|img|!alt:in:next",
),

Sarjakuva(
	"Stupid Fox", 
	"stupidfox",

	"http://stupidfox.net/", 
	"http://stupidfox.net/hello",
	test="http://stupidfox.net/168-home-sweet-home",

	image="div.comicmid>img",
	next="div.comicright>a|span.spriteNext",
),


# Sarjakuva(
# 	"Red panels", 
# 	"redpanels",

# 	"http://www.hj-story.com/", 
# 	"http://redpanels.com/1/",
# 	test="http://redpanels.com/360/",

# 	image="#comicImg",
# 	next="a.arrowLink|div|text:=:❯",
# ),

# Sarjakuva(
# 	"nimi", 
# 	"alias",

# 	"baseurl", 
# 	"firsturl",
# 	test="testurl",

# 	image="imagetree",
# 	next="nextlinktree",
# ),


# Sarjakuva(
# 	"nimi", 
# 	"alias",

# 	"baseurl", 
# 	"firsturl",
# 	test="testurl",

# 	image="imagetree",
# 	next="nextlinktree",
# ),

]
count = db.session.query(Sarjakuva).count()
for i in content:
	found = db.session.query(Sarjakuva).filter(Sarjakuva.lyhenne == i.lyhenne).first()
	if not found:
		count += 1
		db.session.add(i)
		db.session.flush()
		Print(i.id, i.nimi)
		
		

db.session.commit()


#http://www.pixietrixcomix.com/
#http://www.strawberrycomics.com/

#http://garfieldminusgarfield.net/post/26270938
#http://www.marriedtothesea.com/index.php?date=021206



#testaa redstring
# strong female

# Sarjakuva(
# 	"nimi", 
# 	"alias",

# 	"baseurl", 
# 	"firsturl",
# 	test="testurl",

# 	image="imagetree",
# 	next="nextlinktree",
# ),




# Sarjakuva( #testaa myöhemmin
# 	"Erfworld", 
# 	"erfworld",

# 	"http://www.erfworld.com/", 
# 	"http://archives.erfworld.com/Book 1/1",
# 	test="http://archives.erfworld.com/Book+3/159",

# 	image="div.comic_content>img",
# 	next="a|i.fa-forward",
# ),

# Sarjakuva( # oma luokka
# 	"Carciphona", 
# 	"carciphona",

# 	"http://carciphona.com/", 
# 	"http://carciphona.com/view.php?page=cover&chapter=1",
# 	test="http://carciphona.com/view.php?page=162&chapter=14",

# 	image="imagetree",
# 	next="#nextarea",
# ),

# Sarjakuva( next perseesta
# 	"Dream Keepers", 
# 	"dreamkeepers",

# 	"http://www.dreamkeeperscomic.com/", 
# 	"http://www.dreamkeeperscomic.com/GNSaga.php?pg=1",
# 	test="http://www.dreamkeeperscomic.com/GNSaga.php?pg=316",

# 	image="img|!src:in:agapages",
# 	next="a|img|!src:in:arrowright",
# ),


# Sarjakuva( #javascript
# 	"Wargyrl", 
# 	"wargyrl",

# 	"http://wargyrl.webcomic.ws/comics/", 
# 	"http://wargyrl.webcomic.ws/comics/1/",
# 	test="http://wargyrl.webcomic.ws/comics/53/",

# 	image="#comicimage",
# 	next="a|!rel:in:next",
# ),