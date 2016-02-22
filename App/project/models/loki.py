# -*- coding: utf-8 -*-
from project import db, app
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Loki(db.Model):

	__tablename__ = "loki"

	id = db.Column(db.Integer, primary_key=True)
	sarjakuva_id = db.Column(db.Integer, ForeignKey('sarjakuva.id'), nullable=True)
	site = db.Column(db.UnicodeText)
	url = db.Column(db.UnicodeText)
	viesti = db.Column(db.UnicodeText)
	error = db.Column(db.UnicodeText)

	date_created = db.Column(db.DateTime, default=datetime.datetime.now)

	def __init__(self, sarjakuva_id, site, viesti, error=None, url=None):
		self.sarjakuva_id = sarjakuva_id
		self.site = site
		self.url = url
		self.viesti = viesti
		self.error = error

	def __repr__(self):	
		return self.toJson()

	def toJson(self):
		ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		ret["date_created"] = self.date_created.strftime("%Y-%m-%d %H:%M:%S")
		#ret["last_parse"] = str(self.last_parse)
		return ret



	
