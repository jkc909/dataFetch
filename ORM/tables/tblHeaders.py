
from sqlalchemy import Column, Integer, DateTime, SmallInteger, JSON, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
from dbBase import Base

class Headers(Base):
	__tablename__ = 'tblHeaders'

	hedId = Column(Integer, autoincrement = True, \
							primary_key = True)
	hedHeader = Column(JSON)
	hedScore = Column(Integer)
	hedDateAdded = Column(DateTime, default = func.now)
	crl = relationship('CrawlResult')

	def __init__(self, header, score = 0):
		pass
		# self.urlDateModified = datetime.now().replace(microsecond=0)





