# from dbConnect import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class UrlQueue(Base):
	__tablename__ = 'tblUrlQueue'

	qrlId = Column(Integer, autoincrement = True, primary_key = True)
	qrlUrl = Column(String(255), primary_key = True)
	qrlRetid = Column(Integer) # NOT NULL
	qrlBadUrl = Column(Boolean) #DEFAULT 0
	qrlBadUrlReason = Column(Integer)
	qrlBadUrlDate = Column(DateTime)
	qrlDateInserted = Column(DateTime) # DEFAULT Now(),
	qrlDateModified = Column(DateTime) # ON UPDATE Now(),
	qrlLastAck = Column(DateTime)
	qrlAck = Column(Boolean)
	qrlPriority = Column(SmallInteger) # NOT NULL DEFAULT 0,
	qrlNotes = Column(String(255))

	def __init__(self, qrlUrl, qrlRetid, qrlAck = 1, qrlPriority = 0):
		self.qrlUrl = qrlUrl
		self.qrlRetid = qrlRetid
		self.qrlPriority = qrlPriority
		self.qrlBadUrl = 0
		self.qrlDateInserted = datetime.now().replace(microsecond=0)
		self.qrlAck = qrlAck


# print(UrlQueue.__table__)

# CREATE TABLE IF NOT EXISTS dataFetch.tblUrlQueue (
#     qrlId INT AUTO_INCREMENT,
#     qrlUrl VARCHAR(255) NOT NULL,
#     qrlRetid INT NOT NULL,
#     qrlBadUrl BIT DEFAULT 0,
#     qrlBadUrlReason INT,
#     qrlBadUrlDate DATETIME,
#     qrlDateInserted DATETIME DEFAULT Now(),
#     qrlDateModified DATETIME ON UPDATE Now(),
#     qrlLastAck DATETIME,
#     qrlAck BIT,
#     qrlPriority TINYINT NOT NULL DEFAULT 0,
#     qrlNotes TEXT,
#     PRIMARY KEY (qrlId, qrlUrl)
# )  ENGINE=INNODB;


