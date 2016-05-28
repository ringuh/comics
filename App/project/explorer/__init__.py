# -*- coding: utf-8 -*-
from flask import flash, redirect, render_template, request, url_for, Blueprint, jsonify
from project import db, app
from flask.ext.login import current_user, login_required, login_user, logout_user
from sqlalchemy import desc, func, and_, or_, case, distinct
from project.models import Sarjakuva as SK, Strippi, Likes, Loki, User, Brute_force,\
Sarjakuva_user as SKU
import datetime, math
explorer_blueprint = Blueprint('explorer', __name__, 
					template_folder='templates',
					static_url_path='/explorer/static',
					static_folder='static' )

def Comic(f):
	from functools import wraps
	@wraps(f)
	def decorated_function(*args, **kwargs):
		n = db.session.query(SK).filter(
				func.lower(SK.lyhenne) == func.lower(kwargs["comic"])
			).first()
		if n is None:
			flash("Tuntematon sarjakuva")
			return redirect(url_for("explorer.index"))
		kwargs["comic"] = n
		return f(*args, **kwargs)
	return decorated_function

def Strip(f):
	from functools import wraps
	@wraps(f)
	def decorated_function(*args, **kwargs):
		n = None
		if kwargs["strip"] > 0:
			print("HEI IM HERE")
			n = db.session.query(Strippi).filter(
					Strippi.sarjakuva_id == kwargs["comic"].id
				).order_by(Strippi.id).offset(kwargs["strip"]-1).first()
			if n is None:
				print("IS NONE")
				n = db.session.query(Strippi).filter(
					Strippi.sarjakuva_id == kwargs["comic"].id
				).order_by(Strippi.id).first()
		if n is None:
			flash("Strippi puuttuu")
			return redirect(url_for("explorer.comic", comic=kwargs["comic"].nimi))
		kwargs["strip"] = n
		return f(*args, **kwargs)
	return decorated_function




#def index():
#	return pvm(None)

	
@explorer_blueprint.route('/')
@explorer_blueprint.route('/d/<pvm>/')
def index(pvm=None):
	try:
		now = datetime.datetime.strptime(pvm, "%Y-%m-%d")
	except Exception as e:
		now = datetime.datetime.now()
	if current_user.get_id() == None:
		return render_template("portal.html",
			dates=None, stripit=None, user=current_user)
	today = datetime.datetime(now.year, now.month, now.day)
	
	yesterday = today - datetime.timedelta(days=1)
	tomorrow = today + datetime.timedelta(days=1)
	dates = dict(	yesterday=yesterday.strftime("%Y-%m-%d"),
					day=today.strftime("%Y-%m-%d"),
					tomorrow=tomorrow.strftime("%Y-%m-%d"),
					next_day=datetime.datetime.now() > tomorrow
				)
	karsitut = current_user.getKarsitut()

	stripit = db.session.query(Strippi).filter(
				Strippi.date_created >= today, 
				Strippi.date_created < tomorrow,
				~Strippi.sarjakuva_id.in_(karsitut) 
			).order_by(
				#Strippi.sarjakuva_id,
				Strippi.date_created
			).limit(300).all()

	return render_template("portal.html",
		dates=dates, stripit=stripit, user=current_user)

@explorer_blueprint.route('/list/')
@login_required
def list():
	n = db.session.query(SK).filter(
			~SK.id.in_(current_user.getKarsitut())).order_by(SK.id).all()
	return render_template("list.html", comics=n, user=current_user)


@explorer_blueprint.route('/<comic>/')
@login_required
@Comic
def comic(comic):
	return redirect(url_for("explorer.comic_strip", comic=comic.lyhenne, strip=1))

@explorer_blueprint.route('/<comic>/<int:strip>/')
@Comic
@Strip
def comic_strip(comic, strip):
	if current_user.Progress(comic.id)+1 == strip.Order():
		current_user.Progress(comic.id, strip.id)

	return render_template("strip.html", comic=comic, strip=strip, user=current_user)

@explorer_blueprint.route('/<comic>/id/<id>/')
@Comic
def strip_by_id(comic, id):
	n = db.session.query(Strippi).get(id)

	if n:
		return redirect(url_for("explorer.comic_strip", comic=n.sarjakuva.lyhenne, strip=n.Order()))
	return redirect(url_for("explorer.comic_strip", comic=comic.lyhenne, strip=1))

@explorer_blueprint.route('/log/')
@login_required
def comic_log():
	return render_template("loki.html", user=current_user)



@explorer_blueprint.route('/options/')
@login_required
def options():
	n = db.session.query(SK).order_by(SK.id).all()
	comics = [i.toJson() for i in n]

	users = None
	if current_user.admin:
		users = db.session.query(User).all()

	return render_template("options.html", comics=comics, users=users, user=current_user)

@explorer_blueprint.route('/favourites/')
@explorer_blueprint.route('/favourites/<int:user_id>/')
def favourites(user_id=None):
	from project.models import User as U, Likes as L, Strippi as ST
	from sqlalchemy import case
	
	target = None
	if user_id: target = db.session.query(U).get(user_id)
	targets = db.session.query(U).order_by("id").all()
	
	limit = app.config["PAGE_LIMIT"]
	try: page = int(request.args["page"])-1
	except: page = 0
	

	offset = page * limit

	count = 0
	
	if user_id:
		count = db.session.query(L).filter(L.user_id == user_id,# L.vote == True
			).count()
		n = db.session.query(L).filter(
				L.user_id == user_id, #L.vote == True
			).order_by(L.vote.desc(), L.strippi_id.desc()).offset(offset).limit(limit).all()
		
		stripit = [i.strippi for i in n]
	else:
		count = db.session.query(distinct(L.strippi_id)).count()
		
		n = db.session.query(
				L.strippi_id.label("id"),
				func.sum(
					case([(L.vote == True, 1), (L.vote == False, -1)], else_=0)
				).label("count")
			).group_by(L.strippi_id).order_by(desc("count"), L.strippi_id).offset(offset).limit(limit).all()
		
		st_ids = [i.id for i in n if i.count != 0]
		m = db.session.query(ST).filter(ST.id.in_(st_ids)).all()

		stripit = []
		for i in n:
			for j in m:
				if i.id == j.id:
					stripit.insert(0, j)
					break



	
	return render_template("favourites.html", 
			stripit=stripit, 
			user=current_user, 
			target=target, 
			page=page,
			pages=math.ceil(count/limit),
			targets=targets)

@explorer_blueprint.route('/options/change_pass/', methods=["POST"])
@login_required
def change_pass():
	json = request.get_json(True)
	msg = None
	#print json
	msg = "Ei tehty mitään"
	try:
		u = db.session.query(User).get(json["id"])
		if u.id == current_user.id and "old_pass" in json and u.verify_pass(json["old_pass"]):
			u.set_password(json["new_pass"])
			db.session.commit()
			msg = "Vaihdettiin salasana"
		else:
			msg = "Virheellinen salasana"
			if current_user.admin:
				try:
					u = db.session.query(User).get(json["id"])
					u.set_password(json["new_pass"])
					db.session.commit()
					msg = "Salasanaksi asetettiin "+json["new_pass"]

				except Exception as e:
					msg = "Salasanan asetus epäonnistui"

	except Exception as e:
		msg = "Salasanan asetus epäonnistui"

	return jsonify(msg=msg)

@explorer_blueprint.route('/options/my_comics/', methods=["POST"])
@login_required
def my_comics():
	json = request.get_json(True)
	msg = None
	#print json
	if "id" in json and "visibility" in json:
		n = db.session.query(SKU).filter(
				SKU.sarjakuva_id == json["id"],
				SKU.user_id == current_user.id ).first()
		if n is None:
			db.session.add(SKU(json["id"], current_user.id, json["visibility"]))
			
		else:
			n.visibility = json["visibility"]
		db.session.commit()
		msg = "Tallennettiin"

	tmp = db.session.query(SK).order_by(SK.nimi).all()
	all_comics = [i.toJson() for i in tmp]
	comics = []
	for i in tmp:
		comics.append(i.StatusJson(current_user.id))

	return jsonify(comics=comics, msg=msg, all_comics=all_comics)

@explorer_blueprint.route('/options/users/', methods=["POST"])
@login_required
def users():
	json = request.get_json(True)
	msg = None
	#print json

	if not current_user.admin:
		return "error", 400

	tmp = db.session.query(User).order_by(User.id).all()
	users = [i.toJson() for i in tmp]

	return jsonify(users=users, msg=msg)

@explorer_blueprint.route('/options/users/take_over/', methods=["POST"])
@login_required
def take_over():
	json = request.get_json(True)
	msg = None

	if not current_user.admin:
		return "error", 400
	try:
		tmp = db.session.query(User).get(json["id"])
		logout_user()
		login_user(tmp)			
	except Exception as e:
		msg = "Epäonnistui"
	
	

	return jsonify(msg=msg)

@explorer_blueprint.route('/options/users/register/', methods=["POST"])
@login_required
def register():
	json = request.get_json(True)
	msg = None
	#print json

	if not current_user.admin:
		return "error", 400
	try:
		db.session.add(User(json["account"].strip().lower(), json["password"].strip()))
		db.session.commit()
	except Exception as e:
		msg = "Epäonnistui"
	
	

	return jsonify(msg=msg)


@explorer_blueprint.route('/login/', methods=["POST"])
def login():
	from project.models import User
	from project import Log
	json = request.get_json(True)
	try:
		account = json["account"].strip().lower()
		passwd = json["password"].strip()
		ip = request.environ['REMOTE_ADDR']
		
		
		db.session.commit()
		n = Brute_force(ip)
		
		if n.count() > 15:
			flash("IP väliaikaisesti estetty. Koita myöhemmin uudestaan.")
			Log("Kirjautuminen estetty", "{}//{}".format(account, len(passwd)), ip)
		
		user = User.query.filter(func.lower(User.account)==func.lower(account)).first()
		if user is not None and user.verify_pass(passwd):
				print((user.account))
				login_user(user, True) # kirjataan käyttäjä current_useriksi
				
				if user.last_login_date is not None and user.account != "vieras":
					flash("Last login {} from ip {}"\
						.format(user.last_login_date, user.last_login_ip ))
				user.last_login_date = datetime.datetime.now()
				user.last_login_ip = ip
				
				Log(None, None, "Kirjautuminen success", "{}//{}".format(account, len(passwd)), 
					ip)
				db.session.commit()
				flash("Kirjauduit sisään")
		else:
			flash("Virheellinen kirjautuminen nro: {}".format(n.count()+1))
			db.session.add(n)
			db.session.commit()

	except Exception as e:
		flash("{}".format(e.message))
		return "0"
	
	return "1"
	

@explorer_blueprint.route('/logout/')
@login_required
def logout():
	logout_user()
	flash("Kirjauduit ulos")

	return redirect(url_for("explorer.index"))


@explorer_blueprint.route('/add/', methods=["POST", "GET"])
@login_required
def add():
	from project.models import Sarjakuva as SK
	if not current_user.admin:
		return "loser";

	if request.method == "GET":
		sarjikset = db.session.query(SK).order_by(desc(SK.id)).all()
		return render_template("add.html", user=current_user, sarjikset=sarjikset)
	else:
		json = request.get_json(True)

		tmp = json["text"].strip()
		tmp = tmp.split("\n")

		add = []
		for i in tmp:
			i = i.strip();
			if i[0] == "u":
				i = i[1:]

			if i[-1] == ",":
				i = i[:-1]

			i = i.strip('"')

			if not i[0] in [")"] and i != "" and not "Sarjakuva" in i:
				add.append(i)
		
		#print add
		if len(add) == 6:
			db.session.add(SK(add[0], add[1], add[2], add[3], add[4], add[5]))
			db.session.commit()
			
		return jsonify(ret=add)


@explorer_blueprint.route('/vote_strip/', methods=["POST"])
@login_required
def vote_strip():
	json = request.get_json(True)
	msg = None

	vote = None
	like = db.session.query(Likes).filter(
				Likes.strippi_id == json["id"],
				Likes.user_id == current_user.id
			).first()


	if "vote" in json:
		if like is None:
			like = Likes(json["id"], current_user.id, json["vote"])
			db.session.add(like)
			db.session.flush()
		else:
			like.vote = json["vote"]

		db.session.commit()

	if like:
		vote = like.vote

	return jsonify(vote=vote)


@explorer_blueprint.route('/options/loki_filter/', methods=["POST"])
@login_required
def loki_filter():
	from project.models import Loki
	json = request.get_json(True)
	msg = None

	sql = db.session.query(Loki)
	try:
		if json["sarjakuva_id"] > 0:
			sql = sql.filter(Loki.sarjakuva_id == json["sarjakuva_id"])
	except: pass
	n = sql.order_by(Loki.id.desc()).limit(1000).all()



	loki = [i.toJson() for i in n]



	return jsonify(loki=loki)

@explorer_blueprint.route('/<comic>/<int:strip>/save_progress/', methods=["POST"])
@Comic
@Strip
@login_required
def save_progress(comic, strip):
	from project.models import User_progress as UP
	msg = None
	json = request.get_json(True)

	current_user.Progress(comic.id, strip.id)

	return jsonify(msg="Tallennettiin progressiksi strippi nro {}".format(strip.Order()))