# -*- coding: utf-8 -*-
from project import db, app
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

class Likes(db.Model):

	__tablename__ = "likes"

	id = db.Column(db.Integer, primary_key=True)
	strippi_id = db.Column(db.Integer, ForeignKey('strippi.id'), nullable=True)
	user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=True)
	vote = db.Column(db.Boolean, default=True)
	date_created = db.Column(db.DateTime, default=datetime.datetime.now)

	def __init__(self, strippi_id, user_id, vote):
		self.strippi_id = strippi_id
		self.user_id = user_id
		self.vote = vote

	def __repr__(self):	
		return self.toJson()

	def toJson(self):
		ret = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		ret["date_created"] = self.date_created.strftime("%Y-%m-%d %H:%M:%S")
		#ret["last_parse"] = str(self.last_parse)
		return ret



	
