from sqlalchemy import Column, Integer, String, ForeignKey
from app import db

class Captcha(db.Model):
	__tablename__ = 'tblCaptcha'

	capId = Column(Integer, autoincrement = True, \
							primary_key = True)
	capRetId = Column(Integer, \
						ForeignKey('tblRetailer.retId'))
	capCrlId = Column(Integer, ForeignKey('tblCrawlResult.crlId'))
	capCaptcha = Column(String(255))
	

	def __init__(self, \
				retId, \
				crlId, \
				captcha):
		self.capRetId = retId
		self.capCrlId = crlId
		self.capCaptcha = captcha

