#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

if "sarjis" in sys.argv:
	from project.taustaprosessit.sarjis_parseri import run
	run()


if "sort" in sys.argv:
	from project. taustaprosessit.sortter import run
	run()
print(sys.argv)



if "reindex" in sys.argv:
	import datetime
	from project import db
	from project.models import Sarjakuva, Strippi
	tmp = sys.argv[2].split("-")


	
	n = db.session.query(Sarjakuva).filter(
		Sarjakuva.id >= int(tmp[0]),
		Sarjakuva.id <= int(tmp[-1])
	).all()

	for i in n:
		count = i.stripit.count()
		for strippi in i.stripit.order_by("id").all():
			count -= 1
			strippi.date_created = strippi.date_created - datetime.timedelta(days=count)

	db.session.commit()