from project import db
from project.models import Sarjakuva as SK, Strippi as ST
from sqlalchemy import func, distinct

sub = db.session.query(distinct(ST.sarjakuva_id)).subquery()

n = db.session.query(SK).filter(~SK.id.in_(sub)).all()

for i in n:
	print(i.id, i.nimi)