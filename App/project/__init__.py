# -*- coding: utf-8 -*-
from flask import Flask, request, g, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user
from flask.ext.triangle import Triangle

app = Flask(__name__)
app.config.from_object('config.BaseConfig')

db = SQLAlchemy(app)
Triangle(app)
login_manager = LoginManager()
login_manager.init_app(app)

#from project.users.views import user_blueprint
#app.register_blueprint(user_blueprint)

from project.explorer import explorer_blueprint
app.register_blueprint(explorer_blueprint)


login_manager.login_view = 'explorer.index'

@app.before_request
def before_request():
	"jotain ennen requestia"

@login_manager.user_loader
def load_user(id):
    from project.models import User
    return User.query.get(int(id))


@app.errorhandler(500)
def page_not_found(e):
    return "Sorry. There was some kind of error on our server. :(", 500

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry. No such page on our server. :(", 404


def Print(a, b=None, c=None, d=None, e=None, f=None, g=None, h=None, i=None, j=None, k=None):
	import unicodedata
	""" Normalise (normalize) unicode data in Python to remove umlauts, accents etc. """

	ret = None
	for i in [a,b,c,d,e,f,g,h,i,j,k]:
		if i:
			merkit = unicode(i) 
			
			normal = unicodedata.normalize('NFKD', merkit).encode('ASCII', 'ignore')
			if ret is None:
				ret = normal
			else:
				ret = u"{}, {}".format(ret, normal)
	print ret


def Log(sarjakuva_id, site, viesti, error=None, url=None, sessio=db.session):
	from project.models import Loki
	if error:
		error = unicode(error)
	sessio.add(Loki(sarjakuva_id, site, viesti, error, url))
	Print(sarjakuva_id, site, viesti, error, url)

	sessio.commit()