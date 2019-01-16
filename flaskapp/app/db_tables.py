from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
# from dbBase import Base

# db = SQLAlchemy(app)
# from tblUrls import Urls
from app import db

from sqlalchemy import create_engine

class Urls(db.Model):
	__tablename__ = 'tblUrls'

	urlId = Column(Integer, autoincrement = True, primary_key = True)
	urlUrl = Column(String(255), primary_key = True, unique=True)
	urlRetId = Column(Integer, ForeignKey('tblRetailer.retId'))
	urlBadUrl = Column(Boolean)
	urlBadUrlReason = Column(Integer)
	urlBadUrlLastDate = Column(DateTime)
	urlBadUrlHistory = Column(Integer)
	urlDateInserted = Column(DateTime, default=func.now())
	urlDateModified = Column(DateTime)
	urlPriority = Column(SmallInteger)
	urlNotes = Column(String(255))
	qrl = relationship('UrlQueue')
	sta = relationship('Static')
	crl = relationship('CrawlResult')

	def __init__(self, urlUrl, urlRetId):
		self.urlUrl = urlUrl
		self.urlRetId = urlRetId
		# self.urlDateModified = datetime.now().replace(microsecond=0)

class Retailer(db.Model):
	__tablename__ = 'tblRetailer'

	retId = Column(Integer, \
					autoincrement = True, \
					primary_key = True)
	retName = Column(String(255), \
					primary_key = True, \
					unique=True)
	qrl = relationship('UrlQueue')
	url = relationship('Urls')
	sta = relationship('Static')
	dyn = relationship('Dynamic')
	crl = relationship('CrawlResult')
	cap = relationship('Captcha')

class UrlQueue(db.Model):
	__tablename__ = 'tblUrlQueue'

	qrlId = Column(Integer, autoincrement = True, primary_key = True)
	qrlUrlId = Column(Integer, ForeignKey('tblUrls.urlId'), primary_key = True, unique=True)
	qrlRetId = Column(Integer, ForeignKey('tblRetailer.retId'))
	qrlLastAck = Column(DateTime)
	qrlAck = Column(Boolean)
	qrlPriority = Column(SmallInteger)


