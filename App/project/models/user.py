# -*- coding: utf-8 -*-
from project import db
from sqlalchemy import ForeignKey, or_
from sqlalchemy.orm import relationship
from flask import jsonify, flash
import datetime


class User(db.Model):

	__tablename__ = "user"

	id = db.Column(db.Integer, primary_key=True)
	account = db.Column(db.UnicodeText, nullable=False)
	password = db.Column(db.UnicodeText, nullable=False)
	admin = db.Column(db.Boolean, default=False, nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.datetime.now)
	last_login_date = db.Column(db.DateTime)
	last_login_ip= db.Column(db.UnicodeText)

	sarjakuvat = relationship("Sarjakuva_user", lazy="dynamic", cascade='all,delete-orphan', backref="user")
	likes = relationship("Likes", lazy="dynamic", cascade='all,delete-orphan', backref="user")




	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return str(self.id)  # python 2
		except NameError:
			return str(self.id)  # python 3		

	def __init__(self, account, passwd=None, admin=False):
		from passlib.apps import custom_app_context as pwd_context
		self.account = account
		self.set_password(passwd)
		self.admin = admin

	def toJson(self):
		ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		if self.date_created is not None:
			ret["date_created"] = self.date_created.strftime("%Y-%m-%d %H:%M:%S")
		if self.last_login_date is not None:
			ret["last_login_date"] = self.last_login_date.strftime("%Y-%m-%d %H:%M:%S")
		ret.pop("password", None)

		return ret

	def set_password(self, password=None):
		from passlib.apps import custom_app_context as pwd_context
		if password is None:
			password = self.generate_password()
		self.password = str(pwd_context.encrypt(password))
		return password

	def generate_password(self):
		import string
		from random import SystemRandom
		rnd = SystemRandom() # use SystemRandom to get real random numbers
		chars = string.letters + string.digits
		length = 20
		return "".join(rnd.choice(chars) for _ in range(length))

	def verify_pass(self, password):
		from passlib.apps import custom_app_context as pwd_context
		return pwd_context.verify(password.strip(), self.password )


	def getKarsitut(self):
		from project.models import Sarjakuva_user as SKU
		karsitut = db.session.query(SKU.sarjakuva_id).filter(
					SKU.user_id == self.id,
					SKU.visibility == False ).all()
		if len(karsitut) == 0:
			karsitut = [-1]

		return karsitut



	def Progress(self, sarjakuva_id, strip_id=None):
		from project.models import User_progress as UP

		n = db.session.query(UP).filter(UP.sarjakuva_id == sarjakuva_id, UP.user_id == self.id).first()
		if n is None:
			n = UP(sarjakuva_id, current_user.id, strip_id)
			db.session.add(n)
			db.session.commit()

		if strip_id:
			n.strippi_id = strip_id
			db.session.commit()
		
		return n.strippi.Order()