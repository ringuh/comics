# -*- coding: utf-8 -*-
from project import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

class IgnoreUrl(db.Model):

	__tablename__ = "IgnoreUrl"

	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.UnicodeText)
	
	date_created = db.Column(db.DateTime, default=datetime.datetime.now)


	def __init__(self, url):
		self.url = url		

	
	