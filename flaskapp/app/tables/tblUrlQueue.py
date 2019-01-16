
from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db


class UrlQueue(db.Model):
	__tablename__ = 'tblUrlQueue'

	qrlId = Column(Integer, autoincrement = True, primary_key = True)
	qrlUrlId = Column(Integer, ForeignKey('tblUrls.urlId'), primary_key = True, unique=True)
	qrlRetId = Column(Integer, ForeignKey('tblRetailer.retId'))
	qrlLastAck = Column(DateTime)
	qrlAck = Column(Boolean)
	qrlPriority = Column(SmallInteger)

	def __init__(self, qrlUrlId, qrlRetId, qrlAck):
		self.qrlUrlId = qrlUrlId
		self.qrlRetId = qrlRetId
		self.qrlLastAck = datetime.now().replace(microsecond=0)
		self.qrlAck = qrlAck


