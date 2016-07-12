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
	url = db.Column(db.UnicodeText)
	last_url = db.Column(db.UnicodeText)
	count = db.Column(db.Integer, default=1)
	
	image = db.Column(db.UnicodeText)
	next = db.Column(db.UnicodeText)

	nsfw = db.Column(db.Boolean)
	short = db.Column(db.Boolean)

	tags = db.Column(db.UnicodeText)

	interval = db.Column(db.Integer, default=12) # tunteja
	minimum_interval = db.Column(db.Integer, default=0) # minimiväli EDELLISESTÄ YRITYKSESTÄ
	weekday = db.Column(db.UnicodeText, default="0,1,2,3,4,5,6")
	download = db.Column(db.Boolean, default=True)
	filetype = db.Column(db.UnicodeText)
	ending = db.Column(db.UnicodeText)
	last_parse = db.Column(db.DateTime, default=None)
	last_attempt = db.Column(db.DateTime, default=None)
	date_created = db.Column(db.DateTime, default=datetime.datetime.now)


	#joukkue_id = db.Column(db.Integer, ForeignKey('joukkue.id'), nullable=True)
	
	#parents = relationship("User_has_child", foreign_keys="User_has_child.child_id", lazy="dynamic", backref="child")
	#fh_players = relationship("Fh_pelaaja_seuranta", lazy="dynamic", backref="user")

	# relationships
	stripit = relationship("Strippi", lazy="dynamic", cascade='all,delete-orphan', backref="sarjakuva")
	lokit = relationship("Loki", lazy="dynamic", cascade='all,delete-orphan', backref="sarjakuva")


	def __init__(self, nimi, lyhenne, url, last_url, parseri=None,
					image=None, next=None, ext=None, weekday=None, 
					interval=12, 
					download=True,
					test=None,
					ending=None ):
		self.nimi = nimi
		self.lyhenne = lyhenne
		self.parseri = parseri
		self.url = url
		self.last_url = last_url
		self.image = image
		self.next = next
		self.filetype = ext
		#self.more = more
		self.interval = interval
		self.weekday = weekday
		self.download = download
		self.ending = ending

		import sys
		if "test" in sys.argv and test:
			self.last_url = test




	def __repr__(self):	
		return self.nimi

	def toJson(self):
		ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		try: ret["date_created"] = self.date_created.strftime("%Y-%m-%d %H:%M:%S")
		except: ret["date_created"] = None
		try: ret["last_parse"] = self.last_parse.strftime("%Y-%m-%d %H:%M:%S")
		except: ret["last_parse"] = None
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




