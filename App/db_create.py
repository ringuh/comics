# -*- coding: utf-8 -*-
from project import app, db, Print
import random, datetime, sys, os
from project.models import *
from project.luokat import *

if "create" in sys.argv:
	db.drop_all()
	db.create_all()
	db.session.flush()
	db.session.commit()
	u = User(u"ringuh", u"zerg", True)
	db.session.add(u)

	db.session.add(User(u"vieras", u"vieras"))

	polku = os.path.join(app.config["SARJAKUVA_FOLDER"], "x")
	dir = os.path.dirname(polku) 
	try: os.stat(dir)
	except: os.mkdir(dir)

# sarjikset
content = [
	Sarjakuva(
		u"Oglaf", #nimi
		u"oglaf", # lyhenne
		u"oglaf", # parseri
		
		u"http://oglaf.com", # baseurl
		u"http://oglaf.com/cumsprite/",

		u"Trydy Cooper, Doub Bayne", # author
		12, # vähintään interval verran väliä per haku
		u"6", # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),

	Sarjakuva(
		u"Fingerpori", #nimi
		u"fingerpori", # lyhenne
		u"fingerpori", # parseri
		
		u"http://www.hs.fi/fingerpori", # baseurl
		u"http://www.hs.fi/fingerpori/s1349775187323",

		u"Pertti Jarla", # author
		12, # vähintään interval verran väliä per haku
		u"0,1,2,3,4,5,6", # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),
	Sarjakuva(
		u"Wiivi ja Wagner", #nimi
		u"wiivijawagned", # lyhenne
		u"fingerpori", # parseri
		
		u"http://www.hs.fi/viivijawagner", # baseurl
		u"http://www.hs.fi/viivijawagner/s1349773144978",

		u"Juba Tuomola", # author
		12, # vähintään interval verran väliä per haku
		u"0,1,2,3,4,5,6", # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),

	Sarjakuva(
		u"Karlsson", 
		u"karlsson",
		u"fingerpori",

		u"http://www.hs.fi/karlsson", 
		u"http://www.hs.fi/karlsson/s1305951536460" 	
	),


	
	# tumblr
	Sarjakuva(
		u"Rosianna Rabbit", #nimi
		u"rosiannarabbit", # lyhenne
		u"rosiannarabbit", # parseri
		
		u"http://rosiannarabbit.com", # baseurl
		u"http://rosiannarabbit.com/post/131180644576",

		u"Alex Dempsey", # author
		12, # vähintään interval verran väliä per haku
		u"0,1,2,3,4,5,6", # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),

	Sarjakuva(
		u"Justice League 8", 
		u"justiceleague8", 
		u"rosiannarabbit",
		
		u"http://jl8comic.tumblr.com", 
		u"http://jl8comic.tumblr.com/post/13372482444/jl8-1-by-yale-stewart-based-on-characters-in-dc",
	),

	Sarjakuva(
		u"Dire Circumstances", 
		u"dire",
		u"rosiannarabbit",

		u"http://fruitscs.tumblr.com", 
		u"http://fruitscs.tumblr.com/post/117225884584",
	),

	Sarjakuva(
		u"nellucnhoj", 
		u"nellucnhoj", 
		u"rosiannarabbit",

		u"http://nellucnhoj.com", 
		u"http://nellucnhoj.com/post/72259187580/back-in-2010-i-decided-to-punish-myself-by-doing",
	),

	# end of tumblr

	Sarjakuva(
		u"Dorkly", #nimi
		u"dorkly", # lyhenne
		u"dorkly", # parseri
		
		u"http://www.dorkly.com/comics", # baseurl
		u"http://www.dorkly.com/comics/page:96", # 96

		None, # author
		12, # vähintään interval verran väliä per haku
		u"0,1,2,3,4,5,6", # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),

	Sarjakuva(
		u"The Order of the Stick", #nimi
		u"oots", # lyhenne
		u"oots", # parseri
		
		u"http://www.giantitp.com", # baseurl
		u"http://www.giantitp.com/comics/oots0001.html", # 96

		u"Rich Burlew", # author
		12, # vähintään interval verran väliä per haku
		u"0,1,2,3,4,5,6", # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),

	# toonhole
	Sarjakuva(
		u"Toonhole", #nimi
		u"toonhole", # lyhenne
		u"toonhole", # parseri
		
		u"http://toonhole.com", # baseurl
		u"http://toonhole.com/2010/01/smart-questions-get-smart-answers/", # 96

		u"Toonhole Chris", # author
		12, # vähintään interval verran väliä per haku
		u"0,2,4", # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),

	Sarjakuva(
		u"xkcd", 
		u"xkcd", 
		u"toonhole",
		
		u"http://xkcd.com", 
		u"http://xkcd.com/1500/",
	),

	Sarjakuva(
		u"Nedroid", 
		u"nedroid", 
		u"toonhole",

		u"http://nedroid.com", 
		u"http://nedroid.com/2015/04/gobs/",
	),

	# END OF TOONHOLE


	Sarjakuva(
		u"Scandinavia and the World", #nimi
		u"satw", # lyhenne
		u"satw", # parseri
		
		u"http://satwcomic.com", # baseurl
		u"http://satwcomic.com/sweden-denmark-and-norway", # 96

		None, # author
		12, # vähintään interval verran väliä per haku
		None, # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),

	Sarjakuva(
		u"Ctrl+Alt+Del", #nimi
		u"cad", # lyhenne
		u"cad", # parseri
		
		u"http://www.cad-comic.com", # baseurl
		u"http://www.cad-comic.com/cad/20021023", # 

		u"Tim Buckley", # author
		12, # vähintään interval verran väliä per haku
		None, # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),

	Sarjakuva(
		u"Cyanide and Happiness", #nimi
		u"explosm", # lyhenne
		u"explosm", # parseri
		
		u"http://explosm.net", # baseurl
		u"http://explosm.net/comics/15", # 

		u"Kris Wilson", # author
		12, # vähintään interval verran väliä per haku
		None, # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),

	Sarjakuva(
		u"Dragonarte", #nimi
		u"dragonarte", # lyhenne
		u"dragonarte", # parseri
		
		u"http://dragonarte.com.br",  # baseurl
		u"http://dragonarte.com.br/admin/tirinhas/",

		None, # author
		12, # vähintään interval verran väliä per haku
		None, # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),

	Sarjakuva(
		u"Completely Normal People", 
		u"completelynormal",
		u"dragonarte",

		u"http://completelynormalpeople.com", 
		u"http://completelynormalpeople.com/images/toons/",
	),

	Sarjakuva(
		u"Avas Demon", 
		u"avasdemon",
		u"avasdemon",

		u"http://www.avasdemon.com/", 
		u"http://www.avasdemon.com/chapters.php",
		u"Michelle Czajkowski", 	
		None,
		None,
		None, 	
	),

	# PAINTRAIN
	Sarjakuva(
		u"Paintrain", #nimi
		u"paintrain", # lyhenne
		u"paintrain", # parseri
		
		u"http://paintraincomic.com",  # baseurl
		u"http://paintraincomic.com/comic/romance/",

		u"KC Green", # author
		12, # vähintään interval verran väliä per haku
		None, # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),

	Sarjakuva(
		u"Merkworks", 
		u"merkworks",
		u"paintrain",

		u"http://mercworks.net/", 
		u"http://mercworks.net/comicland/a-comic/",

		u"Dave Mercier", 		
	),

	Sarjakuva(
		u"Evil Inc.", 
		u"evilinc",
		u"paintrain",

		u"http://evil-inc.com/", 
		u"http://evil-inc.com/comic/santa-villain-poem-1/",

		u"Brad J. Guigar", 		
	),

	Sarjakuva(
			u"Last Place", 
			u"lastplace",
			u"paintrain",

			u"http://lastplacecomics.com/", 
			u"http://lastplacecomics.com/comic/wide-range-of-super-powers/",

		),

	Sarjakuva(
		u"Fowl Language", 
		u"fowllanguage",
		u"paintrain",
		
		u"http://www.fowllanguagecomics.com/", 
		u"http://www.fowllanguagecomics.com/comic/part-of-the-process/",

		u"Brian Gordon", 
		),

	Sarjakuva(
			u"Looking For Group", 
			u"lfg", 
			u"paintrain",
			
			u"http://www.lfg.co/", 
			u"http://www.lfg.co/page/1/",
		),

	Sarjakuva(
			u"Non-Player Character", 
			u"npc", 
			u"paintrain",
			
			u"http://www.lfg.co/", 
			u"http://www.lfg.co/npc/tale/1-1/",
		),

	Sarjakuva(
			u"Tiny Dick Adventures", 
			u"tinydickadventures", 
			u"paintrain",
			
			u"http://www.lfg.co/", 
			u"http://www.lfg.co/tda/strip/1/",
		),

		Sarjakuva(
			u"The Fox Sisters", 
			u"foxsisters",
			u"paintrain",
			
			u"http://www.thefoxsister.com/", 
			u"http://www.thefoxsister.com/index.php?id=1",
		),

	Sarjakuva(
			u"The Odd 1s Out", 
			u"theodd1sout",
			u"paintrain",

			u"http://theodd1sout.com/", 
			u"http://theodd1sout.com/comic/god-its-awful/",
		),

	Sarjakuva( 
		u"Cheer Up, Emo Kid", 
		u"cheerup",
		u"paintrain",

		u"http://www.cheerupemokid.com", 
		u"http://www.cheerupemokid.com/comic/truth",		
	),

	# END OF PAINTRAIN

	Sarjakuva(
		u"Gunshow", 
		u"gunshow",
		u"gunshow",

		u"http://www.gunshowcomic.com/",
		u"http://www.gunshowcomic.com/1",

		u"KC Green", 		
	),

	Sarjakuva(
		u"HappleTea", #nimi
		u"happletea", # lyhenne
		u"happletea", # parseri
		
		u"http://www.happletea.com",  # baseurl
		u"http://www.happletea.com/comic/fallacies/",

		u"Scott Maynard", # author
		12, # vähintään interval verran väliä per haku
		None, # haetaan korkeintaan näinä viikonpäivinä
		False, # more
	),
	
	Sarjakuva(
		u"Skadi", 
		u"skadi",
		u"happletea",

		u"http://skadicomic.com", 
		u"http://skadicomic.com/2008/05/07/ballad-of-skadi-pt-1-2/",

		u"Katie Rice, Luke Cormican", 
	),

	# Sarjakuva(
	# 	u"Tales of Valoran", 
	# 	u"valoran",
	# 	u"happletea",

	# 	u"http://www.talesofvaloran.com/", 
	# 	u"http://www.talesofvaloran.com/?p=21",

	# 	u"lendokhar", 
	# ),

	Sarjakuva(
		u"C-Section", 
		u"csection",
		u"happletea",

		u"http://www.csectioncomics.com/", 
		u"http://www.csectioncomics.com/comics/one-day-in-country",

		u"Idan Schneider", 		
	),

# happletea
	Sarjakuva(
		u"Berkeley Mews", 
		u"berkeleymews",
		u"happletea",

		u"http://www.berkeleymews.com/", 
		u"http://www.berkeleymews.com/?p=19",

		u"benzaehringer at gmail.com", 		
	),

	Sarjakuva(
		u"Completely Serious Comics", 
		u"completelyseriouscomics",
		u"happletea",

		u"http://completelyseriouscomics.com/", 
		u"http://completelyseriouscomics.com/?p=6",

		u"completelyseriouscomics", 		
	),

	Sarjakuva(
		u"Pictures in Boxes", 
		u"picturesinboxes",
		u"happletea",

		u"http://www.picturesinboxes.com/", 
		u"http://www.picturesinboxes.com/2013/10/26/tetris/",

		u"picturesinboxes", 		
	),

	Sarjakuva(
		u"Channelate", 
		u"channelate",
		u"happletea",

		u"http://www.channelate.com/", 
		u"http://www.channelate.com/2008/02/13/wear-a-clean-shirt/",

		u"Ryan Hudson", 
	),

	Sarjakuva(
			u"Amazing Super Powers", 
			u"amazingsuperpowers", 
			u"happletea",

			u"http://www.amazingsuperpowers.com/", 
			u"http://www.amazingsuperpowers.com/2007/09/heredity/",

			u"Wes & Tony", 
		),

	Sarjakuva( 
			u"Zen Pencils", 
			u"zenpencils",
			u"happletea",
			
			u"http://zenpencils.com/", 
			u"http://zenpencils.com/comic/1-ralph-waldo-emerson-make-them-cry/",
		),

	Sarjakuva(
			u"The Noob", 
			u"noob",
			u"happletea",
			
			u"http://thenoobcomic.com/", 
			u"http://thenoobcomic.com/comic/1/",

			u"Gianna", 
		),

	Sarjakuva( 
			u"Safely Endangered", 
			u"safelyendangered",
			u"happletea",
			
			u"http://www.safelyendangered.com/", 
			u"http://www.safelyendangered.com/comic/ignored/",

			u"Chris", 
		),
	Sarjakuva(
			u"Exploding Dinosaur", 
			u"explodingdinosaur",
			u"happletea",
			
			u"http://explodingdinosaur.com/", 
			u"http://explodingdinosaur.com/comic/seriously-stop-it/",

			u"Josh Walthall", 
		),
	Sarjakuva(
		u"Veritable Hokum", 
		u"veritablehokum",
		u"happletea",

		u"http://www.veritablehokum.com/", 
		u"http://www.veritablehokum.com/comic/headless-folks-of-the-french-revolution/",

		u"Korwin Briggs", 
	),

	Sarjakuva(
		u"Hijinks Ensue", 
		u"hijinksensue",
		u"happletea",

		u"http://hijinksensue.com/", 
		u"http://hijinksensue.com/comic/who-is-your-daddy-and-what-does-he-do/",
	
	),


	Sarjakuva(
		u"Sharksplode", 
		u"sharksplode",
		u"happletea",

		u"http://sharksplode.com/", 
		u"http://sharksplode.com/comic/is-it-the-word-is-it-really/",
	
	),

	Sarjakuva(
		u"Legacy Control", 
		u"legacy-control",
		u"happletea",

		u"http://legacy-control.com/", 
		u"http://legacy-control.com/comic/advent-boner-3/",
		
	),
	Sarjakuva(
		u"The Adventures of Businesscat", 
		u"businesscat",
		u"happletea",

		u"http://www.businesscat.happyjar.com/", 
		u"http://www.businesscat.happyjar.com/comic/coffee/",
		
	),

	Sarjakuva(
		u"Hejibits", 
		u"hejibits",
		u"happletea",

		u"http://www.hejibits.com/", 
		u"http://www.hejibits.com/comics/roommate-comics-1/",
	),

	Sarjakuva(
		u"The Awkward Yeti", 
		u"awkwardyeti",
		u"happletea",

		u"http://theawkwardyeti.com/", 
		u"http://theawkwardyeti.com/comic/0912-reading/",

		u"Nick Seluk", 
		
	),

	Sarjakuva(
		u"Big Foot Justice", 
		u"bigfootjustice",
		u"happletea",

		u"http://bigfootjustice.com/", 
		u"http://bigfootjustice.com/comic/iscale-2/",

		u"Mike Salcedo", 
		
	),

# end happletea
	Sarjakuva(
		u"VGCats", 
		u"vgcats",
		u"vgcats",

		u"http://www.vgcats.com/comics/", 
		u"http://www.vgcats.com/comics/?strip_id=1",
		u"Scott Ramsoomair", 
	),

	Sarjakuva(
		u"Nerf Now", 
		u"nerfnow",
		u"nerfnow",

		u"http://www.nerfnow.com/", 
		u"http://www.nerfnow.com/comic/4",
		u"Josué Pereira", 		
	),
	Sarjakuva(
		u"Sinfest", 
		u"sinfest",
		u"sinfest",

		u"http://www.sinfest.net/", 
		u"http://www.sinfest.net/view.php?date=2000-01-17",

		u"Tatsuya Ishida",
	),

	Sarjakuva(
		u"Camp", 
		u"camp",
		u"camp",

		u"http://campcomic.com/", 
		u"http://campcomic.com/comic/dear-mom",
		
	),

	Sarjakuva(
		u"Penny Arcade", 
		u"pennyarcade",
		u"pennyarcade",

		u"http://www.penny-arcade.com", 
		u"http://www.penny-arcade.com/comic/1998/11/18",
		u"Mike Krahulik & Jerry Holkins", 
		None,
		None,
		None,
		False # ei tallenneta
	),

	Sarjakuva(
		u"Fredo & Pidjin", 
		u"pidjin",
		u"pidjin",

		u"http://www.pidjin.net/", 
		u"http://www.pidjin.net/2005/05/30/tricks-to-getting-delayed/",		
	),

	Sarjakuva(
		u"Garfield", 
		u"garfield",
		u"garfield",

		u"http://garfield.com/comic", 
		u"http://garfield.com/comic/2012-06-01",
	),

	Sarjakuva(
		u"U.S. Acres", 
		u"usacres",
		u"garfield",

		u"http://garfield.com/us-acres", 
		u"http://garfield.com/us-acres/2012-06-01",
	),
	Sarjakuva(
		u"Least I could do", 
		u"leasticoulddo",
		u"leasticoulddo",

		u"http://www.leasticoulddo.com/comic/", 
		u"http://www.leasticoulddo.com/comic/20030210/",
		
	),

	Sarjakuva(
		u"Questionable Content", 
		u"questionablecontent",
		u"questionablecontent",

		u"http://questionablecontent.net", 
		u"http://questionablecontent.net/view.php?comic=1",
	),

	Sarjakuva(
		u"Wulffmorgenthaler", 
		u"wumo",
		u"wumo",

		u"http://wumo.com", 
		u"http://wumo.com/wumo/2015/09/08",
		u"Wumo", 		
	),
	#GO COMICS
	Sarjakuva(
		u"Calvin and Hobbes", 
		u"calvinandhobbes",
		u"gocomics",

		u"http://www.gocomics.com/calvinandhobbes/", 
		u"http://www.gocomics.com/calvinandhobbes/2014/06/13",

		u"Bill Watterson", 
	),

	Sarjakuva(
		u"The Flying MCCoys", 
		u"mccoys",
		u"gocomics",

		u"http://www.gocomics.com/theflyingmccoys/", 
		u"http://www.gocomics.com/theflyingmccoys/2012/06/01",

		u"Glenn and Gary McCoy", 
	),
	Sarjakuva(
		u"Pearls Before Swine", 
		u"pearls",
		u"gocomics",

		u"http://www.gocomics.com/pearlsbeforeswine/", 
		u"http://www.gocomics.com/pearlsbeforeswine/2012/06/01",

		u"Stephan Pastis", 
	),
	Sarjakuva(
		u"9 Chickweed Lane", 
		u"9chickweedlane",
		u"gocomics",

		u"http://www.gocomics.com/9chickweedlane", 
		u"http://www.gocomics.com/9chickweedlane/2012/06/01",

		u"Brooke McEldowney", 
	),

	Sarjakuva(
		u"Jim Benton", 
		u"jimbenton",
		u"gocomics",

		u"http://www.gocomics.com/jim-benton-cartoons/", 
		u"http://www.gocomics.com/jim-benton-cartoons/2014/10/27",

		u"Jim Benton", 		
	),
	Sarjakuva(
		u"Over the Hedge", 
		u"overthehedge", 
		u"gocomics",

		u"http://www.gocomics.com/overthehedge/", 
		u"http://www.gocomics.com/overthehedge/2015/07/30",
		u"T Lewis and Michael Fry", 
	),
	Sarjakuva(
		u"Sunny Street",
		u"sunnystreet" 
		u"gocomics",
		
		u"http://www.gocomics.com/sunny-street/", 
		u"http://www.gocomics.com/sunny-street/2013/06/03",
		u"Max Garcia and Sandra Barthauer", 
	),


	#END OF GO COMICS
	#
	# HIWEWORKS
	Sarjakuva(
		u"Johnny Wander Fiction", 
		u"johnnywander",
		u"hiveworks",

		u"http://www.johnnywander.com/fiction", 
		u"http://www.johnnywander.com/fiction/girl-with-the-skeleton-hand-1",
		None,
		0		
	),

	Sarjakuva(
		u"Lucky Penny", 
		u"luckypenny",
		u"hiveworks",

		u"http://www.johnnywander.com/luckypenny", 
		u"http://www.johnnywander.com/luckypenny/lucky-penny-001", 
		None,
		0
		
	),
	Sarjakuva( 
		u"Autobio", 
		u"autobio",
		u"hiveworks",

		u"http://www.johnnywander.com/comic", 
		u"http://www.johnnywander.com/comic/i",
		None,
		0
		
	),

	Sarjakuva(
		u"Lets Speak English", 
		u"letsspeakenglish", 
		u"hiveworks",
		
		u"http://www.marycagle.com", 
		u"http://www.marycagle.com/letsspeakenglish/1-shingeki-no-kodomo",
		u"Mary Cagle", 
	),
	Sarjakuva( 
		u"The Rock Cocks", 
		u"rockcocks", 
		u"hiveworks",
		
		u"http://www.therockcocks.com", 
		u"http://www.therockcocks.com/comic/page-1-nsfw-track-1-start",
	),

	Sarjakuva(
		u"Whomp", 
		u"whomp",
		u"hiveworks",

		u"http://www.whompcomic.com/", 
		u"http://www.whompcomic.com/comic/06152010",
	),


	# END OF HIWEWORKS
	# 
	
	Sarjakuva( 
		u"For lack of a better comic", 
		u"floabc",
		u"floabc",

		u"http://www.forlackofabettercomic.com", 
		u"http://forlackofabettercomic.com/?id=1",		
	),

	Sarjakuva(
		u"Love Me Nice", 
		u"lovemenice",
		u"floabc",

		u"http://lovemenicecomic.com/comic", 
		u"http://lovemenicecomic.com/comic/001.php",
		u"Amanda Lafrenais", 		
	),

	Sarjakuva(
		u"Hamlet's Danish", 
		u"hamlet",
		u"hamlet",

		u"http://clayyount.com/hamlets-danish", 
		u"http://clayyount.com/hamlets-danish-comic/2014/4/7/one-question",
		u"Clay Yount", 		
	),
	
	Sarjakuva(
		u"Manly Guys Doing Manly Things", 
		u"machismo",
		u"paintrain",

		u"http://thepunchlineismachismo.com/", 
		u"http://thepunchlineismachismo.com/archives/comic/02222010",		
	),
	# INTERROBANG
		Sarjakuva( #29,
		u"Im my own Mascot", 
		u"imomascot",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=9", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=141",		
	),
	Sarjakuva( #29,
		u"Wookie-ookies", 
		u"wookie",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=18", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=929",
	),
	Sarjakuva( #29,
		u"Things Which Defy Categorization", 
		u"twdc",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=17", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=49",
	),
	Sarjakuva( #29,
		u"Fair-Haired Adventure Seekers", 
		u"adventureseekers",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=6", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=930",
	),
	Sarjakuva( #29,
		u"It sucks to be Weegie", 
		u"weegie",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=11", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=941",
	),
	Sarjakuva( #29,
		u"WatchBabies", 
		u"watchbabies",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=7", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=959",
	),
	Sarjakuva( #29,
		u"Ensign3 Crisis of Infinite Sues", 
		u"ensign3",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=10", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=989",
	),
	Sarjakuva( #29,
		u"Spinks", 
		u"spinks",
		u"interrobang",

		u"http://www.spinkspink.com/", 
		u"http://www.spinkspink.com/index.php?strip_id=78",
	),
	Sarjakuva( #29,
		u"Trigger Star", 
		u"triggerstar",
		u"interrobang",

		u"http://www.triggerstar.com/", 
		u"http://www.triggerstar.com/index.php?strip_id=60",
	),
	Sarjakuva( #29,
		u"The Dark Intruder", 
		u"darkintruder",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=1", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=1",
	),
	Sarjakuva( #29,
		u"A Girl Named Bob", 
		u"girlbob",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=3", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=31",
	),
	Sarjakuva( #29,
		u"This is Visas", 
		u"visas",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=13", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=357",
	),
	Sarjakuva( #29,
		u"Heeere's Satan", 
		u"heresatan",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=15", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=146",
	),
	Sarjakuva( #29,
		u"Punker Darren", 
		u"punkerdarren",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=2", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=16",
	),
	Sarjakuva( #29,
		u"Space is really big!", 
		u"bigspace",
		u"interrobang",

		u"http://www.interrobangstudios.com/comics-display.php?comic_id=12", 
		u"http://interrobangstudios.com/comics-display.php?strip_id=55",
	),
	

	# END OF INTERROBANG
	# 
	
	Sarjakuva( 
		u"Dilbert", 
		u"dilbert",
		u"dilbert",

		u"http://dilbert.com", 
		u"http://dilbert.com/strip/2015-01-11",
		u"Scott Adams", 
	),

	Sarjakuva( 
		u"The Perry Bible Fellowship", 
		u"perrybible",
		u"perrybible",

		u"http://pbfcomics.com", 
		u"http://pbfcomics.com/1/",
		
	),

	Sarjakuva( 
		u"Rational Comics", 
		u"rational",
		u"rational",

		u"http://www.rationalcomics.com", 
		u"http://www.rationalcomics.com/001-mountain-moving-man/",
		u"Joshua Sim", 		
	),

	Sarjakuva( 
		u"Loading Artist", 
		u"loadingartist",
		u"loadingartist",

		u"http://www.loadingartist.com", 
		u"http://www.loadingartist.com/comic/born/",
				
	),

	Sarjakuva( 
		u"Saturday Morning Breakfast Cereal", 
		u"smbc",
		u"smbc",

		u"http://www.smbc-comics.com", 
		u"http://www.smbc-comics.com/index.php?id=3768",		
	),

	Sarjakuva(
		u"Girls with Slingshots", 
		u"girlswithslingshots",
		u"smbc",

		u"http://www.girlswithslingshots.com", 
		u"http://www.girlswithslingshots.com/comic/gws-chaser-1",
	),


	Sarjakuva(
		u"Its the Tie", 
		u"itsthetie",
		u"itsthetie",

		u"http://itsthetie.com/", 
		u"http://itsthetie.com/?comic=no-world-for-a-squirrel-4",		
	),

	Sarjakuva( 
		u"Commit Strip", 
		u"commitstrip",
		u"itsthetie",

		u"http://www.commitstrip.com/", 
		u"http://www.commitstrip.com/en/2012/02/22/interview/",		
	),

	Sarjakuva( 
		u"Strong Female Protagonist", 
		u"strongfemaleprotagonist", 
		u"itsthetie",
		
		u"http://strongfemaleprotagonist.com/", 
		u"http://strongfemaleprotagonist.com/issue-1/page-0/",
	),

	Sarjakuva( 
		u"Nerd Rage", 
		u"nerdrage",
		u"nerdrage",

		u"http://nerdragecomic.com", 
		u"http://nerdragecomic.com/index.php?date=2010-09-28",
		
	),


	Sarjakuva(
		u"Tubey Toons", 
		u"tubeytoons",
		u"tubeytoons",

		u"http://tubeytoons.com", 
		u"http://tubeytoons.com/comic/stay-put",		
	),

	Sarjakuva( 
		u"Dark Legacy", 
		u"darklegacy", 
		u"darklegacy",
	
		u"http://www.darklegacycomics.com", 
		u"http://www.darklegacycomics.com/1",
		
	),

	Sarjakuva(
		u"Awkward Zombie", 
		u"awkwardzombie",
		u"nerdrage",

		u"http://www.awkwardzombie.com", 
		u"http://www.awkwardzombie.com/index.php?page=0&comic=092006",	
	),

	Sarjakuva( 
		u"Player vs. Player", 
		u"pvponline",
		u"pvponline",

		u"http://www.pvponline.com", 
		u"http://www.pvponline.com/comic/2015/06/01/birds-of-a-feather1",
		
	),

	Sarjakuva( 
		u"User Friendly", 
		u"userfriendly",
		u"userfriendly",
		u"http://ars.userfriendly.org", 
		u"http://ars.userfriendly.org/cartoons/?id=20150731",

	),

	Sarjakuva( #60,
		u"Grog", 
		u"grog",
		u"grog",

		u"http://www.grogcomics.com", 
		u"http://www.grogcomics.com/they-breed-like/",
	),


	Sarjakuva(
		u"Vattu", 
		u"vattu", 
		u"vattu",

		u"http://www.rice-boy.com/vattu", 
		u"http://www.rice-boy.com/vattu/index.php?c=001",
	),

	Sarjakuva(
		u"Power Nap", 
		u"powernap",
		u"powernap",

		u"http://www.powernapcomic.com/", 
		u"http://www.powernapcomic.com/d/20110617.html",		
	),

	Sarjakuva(
		u"Extra Life", 
		u"extralife",
		u"extralife",

		u"http://www.myextralife.com", 
		u"http://www.myextralife.com/comic/06172001/",		
	),

	Sarjakuva( 
		u"Poorly Drawn Lines", 
		u"poorlydrawnlines",
		u"poorlydrawnlines",

		u"http://poorlydrawnlines.com", 
		u"http://poorlydrawnlines.com/comic/campus-characters/",
	),


	Sarjakuva(
		u"Existential Comics", 
		u"Existential Comics", 
		u"existential",
		u"http://existentialcomics.com", 
		u"http://existentialcomics.com/comic/1",
	),

	Sarjakuva(
		u"The Abominable", 
		u"abominable",
		u"abominable",

		u"http://abominable.cc", 
		u"http://abominable.cc/post/44164796353/episode-one",
	),

	Sarjakuva(
		u"Menage a 3", 
		u"ma3", 
		u"ma3",
		u"http://www.ma3comic.com/", 
		u"http://www.ma3comic.com/strips-ma3/for_new_readers",
	),

	Sarjakuva(
		u"Gone With the Blastwave",  
		u"blastwave",
		u"blastwave",

		u"http://www.blastwave-comic.com", 
		u"http://www.blastwave-comic.com/index.php?p=comic&nro=1",
	),

	Sarjakuva(
		u"Stand Still Stay Silent", 
		u"standstill",
		u"standstill",

		u"http://www.sssscomic.com", 
		u"http://www.sssscomic.com/comic.php?page=1",
		u"Minna Sundberg", 
	),

	Sarjakuva(
		u"Romantically Apocalyptic", 
		u"romanticallyapocalyptic",
		u"romanticallyapocalyptic",
		u"http://romanticallyapocalyptic.com", 
		u"http://romanticallyapocalyptic.com/0",
	),

	Sarjakuva( 
		u"Down the Upward Spiral", 
		u"downtheupwardspiral",
		u"downtheupwardspiral",
		u"http://www.downtheupwardspiral.com", 
		u"http://www.downtheupwardspiral.com/gallery.html",
		),
	Sarjakuva(
		u"Things In Squares", 
		u"thingsinsquares",
		u"thingsinsquares",
		u"http://www.thingsinsquares.com", 
		u"http://www.thingsinsquares.com/comics/lame-joke/",
	),

	Sarjakuva( 
		u"FoxTrot", 
		u"foxtrot",
		u"thingsinsquares",
		u"http://www.foxtrot.com", 
		u"http://www.foxtrot.com/2015/08/16/no-worries/",
	),

	Sarjakuva( 
		u"Berds and Nerds", 
		u"berdsandnerds",
		u"berdsandnerds",

		u"http://berdsandnerds.com", 
		u"http://berdsandnerds.com/thearchive/",
	),

	Sarjakuva(
		u"Pepper and Carrot", 
		u"pepperandcarrot",
		u"pepperandcarrot",

		u"http://www.peppercarrot.com", 
		u"http://www.peppercarrot.com/en/static6/sources",
	),

	Sarjakuva( 
		u"Catsu The Cat", 
		u"catsu",
		u"catsu",

		u"http://www.catsuthecat.com/blogs/comics/", 
		u"http://www.catsuthecat.com/blogs/comics/",
	),

	Sarjakuva( 
		u"Unsounded", 
		u"unsounded",
		u"unsounded",

		u"http://www.casualvillain.com/Unsounded/comic+index", 
		u"http://www.casualvillain.com/Unsounded/comic/ch01/ch01_01.html",
		#u"http://www.casualvillain.com/Unsounded/comic/ch05/ch05_16.html",
		#u"http://www.casualvillain.com/Unsounded/comic/ch10/ch10_162.html"
	),

]

for i in content:
	found = db.session.query(Sarjakuva).filter(Sarjakuva.lyhenne == i.lyhenne).first()
	if not found:
		Print(i.nimi)
		db.session.add(i)

db.session.commit()
