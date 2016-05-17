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
	# 	tags="#comic>img",
	# 	next="a.comic-nav-next",
	# 	weekday="0",
	# ),

	Sarjakuva(
		"Evil Inc.", 
		"evilinc",
		"paintrain",

		"http://evil-inc.com/", 
		"http://evil-inc.com/comic/santa-villain-poem-1/",
		test="http://evil-inc.com/comic/goo-monster/",

		tags="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		"Last Place", 
		"lastplace",

		"http://lastplacecomics.com/", 
		"http://lastplacecomics.com/comic/wide-range-of-super-powers/",
		test="http://lastplacecomics.com/comic/final-fantasy-high-school/",

		tags="#comic>img",
		next="a.comic-nav-next",
		interval=0,
	),

	Sarjakuva(
		"Fowl Language", 
		"fowllanguage",
		"paintrain",
		
		"http://www.fowllanguagecomics.com/", 
		"http://www.fowllanguagecomics.com/comic/part-of-the-process/",
		test="http://www.fowllanguagecomics.com/comic/bread-crust/",

		tags="#comic>img",
		next="a.comic-nav-next",

	),

	Sarjakuva(
		"Looking For Group", 
		"lfg", 

		"http://www.lfg.co/", 
		"http://www.lfg.co/page/1/",
		test="http://www.lfg.co/page/981/",

		tags="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		"Non-Player Character", 
		"npc", 
	
		"http://www.lfg.co/", 
		"http://www.lfg.co/npc/tale/1-1/",
		test="http://www.lfg.co/npc/tale/21-9/",

		tags="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		"Tiny Dick Adventures", 
		"tinydickadventures", 
	
		"http://www.lfg.co/", 
		"http://www.lfg.co/tda/strip/1/",
		test="http://www.lfg.co/tda/strip/114/",

		tags="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		"The Fox Sisters", 
		"foxsisters",
				
		"http://www.thefoxsister.com/", 
		"http://www.thefoxsister.com/index.php?id=1",
		test="http://thefoxsister.com/index.php?id=126",

		tags="#comicimg",
		next="a.comic-nav-next",
	),

	Sarjakuva(
		"The Odd 1s Out", 
		"theodd1sout",
		
		"http://theodd1sout.com/", 
		"http://theodd1sout.com/comic/god-its-awful/",
		test="http://theodd1sout.com/comic/my-child/",

		tags="#comic>img",
		next="a.comic-nav-next",
	),

	Sarjakuva( 
		"Cheer Up, Emo Kid", 
		"cheerup",
		
		"http://www.cheerupemokid.com", 
		"http://www.cheerupemokid.com/comic/truth",
		test="http://www.cheerupemokid.com/comic/permit",

		tags="#comic>img",
		next="a.next",
		#"http://www.cheerupemokid.com/comic/frank",	
	),

	Sarjakuva(
		"Manly Guys Doing Manly Things", 
		"machismo",


		"http://thepunchlineismachismo.com/", 
		"http://thepunchlineismachismo.com/archives/comic/02222010",
		test="http://thepunchlineismachismo.com/archives/comic/2755",
		tags="#comic>img",
		next="a.comic-nav-next"
	),

	Sarjakuva( 
		"Commit Strip", 
		"commitstrip",

		"http://www.commitstrip.com/", 
		"http://www.commitstrip.com/en/2012/02/22/interview/",
		test="http://www.commitstrip.com/en/2016/05/12/coder-superpower/",

		tags="div.entry-content>img.size-full",
		next="a|!rel:in:next",	
	),

	Sarjakuva(
		"Girls with Slingshots", 
		"girlswithslingshots",

		"http://www.girlswithslingshots.com", 
		"http://www.girlswithslingshots.com/comic/gws-chaser-1",
		test="http://www.girlswithslingshots.com/comic/gws-chaser-307",

		tags="#cc-comic",
		next="a.next",
	),

	Sarjakuva( 
		"Strong Female Protagonist", 
		"strongfemaleprotagonist", 
		
		"http://strongfemaleprotagonist.com/", 
		"http://strongfemaleprotagonist.com/issue-1/page-0/",
		test="http://strongfemaleprotagonist.com/issue-6/page-44-5/",
		tags="article.post>img.size-full",
		next="a|!rel:in:next",
	),
	Sarjakuva( 
		"Nerd Rage", 
		"nerdrage",

		"http://nerdragecomic.com/", 
		"http://nerdragecomic.com/index.php?date=2010-09-28",
		test="http://nerdragecomic.com/index.php?date=2016-04-22",

		tags="img|!src:in:strips",
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

		tags="img.comic-image",
		next="a.nextLink",
		
	),
	Sarjakuva(
		"Awkward Zombie", 
		"awkwardzombie",

		"http://www.awkwardzombie.com/", 
		"http://www.awkwardzombie.com/index.php?page=0&comic=092006",
		test="http://www.awkwardzombie.com/index.php?page=0&comic=041816",

		tags="#comic>img",
		next="a|img|!alt:in:next comic",
	),

	Sarjakuva( 
		"Player vs. Player", 
		"pvponline",

		"http://www.pvponline.com/", 
		"http://www.pvponline.com/comic/2015/06/01/birds-of-a-feather1",
		test="http://pvponline.com/comic/2016/05/12/the-one-time",

		tags="section.comic-art>img",
		next="div.comic-nav>a.left|!text:in:next",
	),
	Sarjakuva( 
		"Table Titans", 
		"tabletitans",

		"http://tabletitans.com/", 
		"http://tabletitans.com/comic/mines-of-madness-page-1",
		test="http://tabletitans.com/comic/whispers-of-dragons-page-142",

		tags="section.comic>img",
		next="a|!text:in:next",
	),
	Sarjakuva( 
		"User Friendly", 
		"userfriendly",

		"http://ars.userfriendly.org", 
		"http://ars.userfriendly.org/cartoons/?id=20160515",
		test="http://ars.userfriendly.org/cartoons/?id=20160515",

		tags="img|!alt:in:strip",
		next="area|!alt:in:next",
	),
	Sarjakuva(
		"Grog", 
		"grog",

		"http://www.grogcomics.com", 
		"http://www.grogcomics.com/they-breed-like/",
		test="http://grogcomics.com/did-you-jump/",

		tags="div.content>div.entry>img",
		next="span.next>a|!rel:in:next",
	),
	Sarjakuva(
		"Vattu", 
		"vattu", 

		"http://www.rice-boy.com/vattu/", 
		"http://www.rice-boy.com/vattu/index.php?c=001",
		test="http://www.rice-boy.com/vattu/index.php?c=742",

		tags="#page>img",
		next="a|!text:in:forward|!href:in:c=",
		ending="index.php"
	),
	Sarjakuva(
		"Power Nap", 
		"powernap",

		"http://www.powernapcomic.com/", 
		"http://www.powernapcomic.com/d/20110617.html",
		test="http://www.powernapcomic.com/d/20160502.html",

		tags="center>img|!src:in:/pnap",
		next="a|img|!alt:in:next",	
	),
	Sarjakuva(
		"Extra Life", 
		"extralife",

		"http://www.myextralife.com/", 
		"http://www.myextralife.com/comic/06172001/",
		test="http://www.myextralife.com/comic/whoville/",

		tags="img.comic",
		next="a.next_comic_link",
	),
	Sarjakuva( 
		"Poorly Drawn Lines", 
		"poorlydrawnlines",

		"http://poorlydrawnlines.com", 
		"http://poorlydrawnlines.com/comic/campus-characters/",
		test="http://poorlydrawnlines.com/comic/kevins-ideas/",

		tags="div.comic>img.size-full",
		next="a|!rel:in:next",
	),
	Sarjakuva(
		"Existential Comics", 
		"Existential Comics", 
		
		"http://existentialcomics.com", 
		"http://existentialcomics.com/comic/1",
		test="http://existentialcomics.com/comic/131",

		tags="img.comicImg",
		next="a|img|!src:in:nav_next",
	),
	Sarjakuva(
		"The Abominable", 
		"abominable",

		"http://abominable.cc", 
		"http://abominable.cc/post/44164796353/episode-one",
		test="http://abominable.cc/post/104845340635/guest-strip-magnus-jonason",

		tags="div.photo>img",
		next="span.next_post>a",
	),
	Sarjakuva(
		"Menage a 3", 
		"ma3", 

		"http://www.ma3comic.com/", 
		"http://www.ma3comic.com/strips-ma3/for_new_readers",
		test="http://www.ma3comic.com/strips-ma3/synchronized_swimmers",

		tags="#cc>img",
		next="#cndnext",
	),

	Sarjakuva(
		"Gone With the Blastwave",  
		"blastwave",

		"http://www.blastwave-comic.com/", 
		"http://www.blastwave-comic.com/index.php?p=comic&nro=1",
		test="http://www.blastwave-comic.com/index.php?p=comic&nro=72",

		tags="#comic_ruutu>img|!src:in:/comics/",
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
		"romanticallyapocalyptic",
		"http://romanticallyapocalyptic.com", 
		"http://romanticallyapocalyptic.com/0",
		test="http://romanticallyapocalyptic.com/238",

		tags="div.comicpanel>center>img",
		next="a|!accesskey:in:n",
	),
	Sarjakuva(
		"Things In Squares", 
		"thingsinsquares",
		
		"http://www.thingsinsquares.com", 
		"http://www.thingsinsquares.com/comics/lame-joke/",
		test="http://www.thingsinsquares.com/comics/san-pedro-cactus/",
		tags="div.entry-content>img.size-full",
		next="a|!rel:in:next",
	),
	Sarjakuva( 
		"FoxTrot", 
		"foxtrot",
		
		"http://www.foxtrot.com", 
		"http://www.foxtrot.com/2015/08/16/no-worries/",
		test="http://www.foxtrot.com/2016/05/01/show-off-and-tell/",

		tags="div.entry-content>img.size-full",
		next="a|!rel:in:next",
	),
	

	Sarjakuva( 
		"Berds and Nerds", 
		"berdsandnerds",
		#"berdsandnerds",

		"http://berdsandnerds.com", 
		"http://berdsandnerds.com/thearchive/",
		test="http://berdsandnerds.com/comic/2016/5/9/theothermother",

		tags="div.sqs-block-content>noscript>img",
		next="div.intrinsic>a|!href:in:/comic/",
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