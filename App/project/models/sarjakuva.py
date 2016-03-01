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
	
	tags = db.Column(db.UnicodeText)
	next_tags = db.Column(db.UnicodeText)

	interval = db.Column(db.Integer, default=12) # tunteja
	weekday = db.Column(db.UnicodeText, default=u"0,1,2,3,4,5,6")
	next_parse = db.Column(db.DateTime, default=datetime.datetime.now)
	last_parse = db.Column(db.DateTime, default=None)
	download = db.Column(db.Boolean, default=True)
	filetype = db.Column(db.UnicodeText)
	date_created = db.Column(db.DateTime, default=datetime.datetime.now)
	#joukkue_id = db.Column(db.Integer, ForeignKey('joukkue.id'), nullable=True)
	
	#parents = relationship("User_has_child", foreign_keys="User_has_child.child_id", lazy="dynamic", backref="child")
	#fh_players = relationship("Fh_pelaaja_seuranta", lazy="dynamic", backref="user")

	# relationships
	stripit = relationship("Strippi", lazy="dynamic", cascade='all,delete-orphan', backref="sarjakuva")
	lokit = relationship("Loki", lazy="dynamic", cascade='all,delete-orphan', backref="sarjakuva")


	def __init__(self, nimi, lyhenne, parseri, url, last_url, 
					tags=None, next_tags=None, filetype=None, weekday=None, interval=12, download=True ):
		self.nimi = nimi
		self.lyhenne = lyhenne
		self.parseri = parseri
		self.url = url
		self.last_url = last_url
		self.tags = tags
		self.next_tags = next_tags
		self.filetype = filetype
		#self.more = more
		self.interval = interval
		self.weekday = weekday
		self.download = download


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




