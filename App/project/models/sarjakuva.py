# -*- coding: utf-8 -*-
from project import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Sarjakuva(db.Model):

	__tablename__ = "sarjakuva"

	id = db.Column(db.Integer, primary_key=True)
	nimi = db.Column(db.UnicodeText)
	parseri = db.Column(db.UnicodeText)
	lyhenne = db.Column(db.UnicodeText, nullable=False)
	author = db.Column(db.UnicodeText)
	url = db.Column(db.UnicodeText)
	last_url = db.Column(db.UnicodeText)
	more = db.Column(db.Boolean, default=False)
	interval = db.Column(db.Integer, default=12) # tunteja
	weekday = db.Column(db.UnicodeText, default=u"0,1,2,3,4,5,6")
	next_parse = db.Column(db.DateTime, default=datetime.datetime.now)
	last_parse = db.Column(db.DateTime, default=None)
	download = db.Column(db.Boolean, default=True)
	date_created = db.Column(db.DateTime, default=datetime.datetime.now)
	#joukkue_id = db.Column(db.Integer, ForeignKey('joukkue.id'), nullable=True)
	
	#parents = relationship("User_has_child", foreign_keys="User_has_child.child_id", lazy="dynamic", backref="child")
	#fh_players = relationship("Fh_pelaaja_seuranta", lazy="dynamic", backref="user")

	# relationships
	stripit = relationship("Strippi", lazy="dynamic", backref="sarjakuva")


	def __init__(self, nimi, lyhenne, parseri, url, last_url, author=None, interval=12, weekday=None, more=False ):
		self.nimi = nimi
		self.lyhenne = lyhenne
		self.parseri = parseri
		self.url = url
		self.last_url = last_url
		self.author = author
		self.more = more
		self.interval = interval
		self.weekday = weekday


	def __repr__(self):	
		return self.nimi

	def toJson(self):
		ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		ret["date_created"] = str(self.date_created)
		ret["last_parse"] = str(self.last_parse)
		return ret

	def Max(self):
		from project.models import Strippi
		count = db.session.query(Strippi).filter(
			Strippi.sarjakuva_id == self.id).count()

		return count

	def Last(self):
		from project.models import Strippi
		ret = None
		ret = db.session.query(Strippi).filter(
			Strippi.sarjakuva_id == self.id).order_by(
					Strippi.id.desc()).first()
		return ret

	def UserStatus(self, id):
		from project.models import Sarjakuva_user as SKU
		ret = True

		n = db.session.query(SKU).filter(
				SKU.sarjakuva_id == self.id,
				SKU.user_id == id ).first()
		if n is not None:
			ret = n.visibility

		return ret

	def StatusJson(self, id):
		ret = self.toJson()
		ret["visibility"] = self.UserStatus(id)

		return ret




