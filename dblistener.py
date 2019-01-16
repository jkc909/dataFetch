from sqlalchemy import update
from sqlalchemy.orm import sessionmaker
from time import sleep
from datetime import datetime
from ORM.tables.tblUrlQueue import *
from sqlalchemy.orm.exc import NoResultFound

class event_listener():

	def __init__(self, session):
		self.session = session

	def return_value(self):
		while True:
				try:
					find_qrlId = self.session.query\
									(UrlQueue).\
									filter(UrlQueue.qrlAck == 0).\
									with_for_update().\
									first()

					find_qrlId.qrlAck = True
					find_qrlId.qrlLastAck = (datetime.now().replace(microsecond=0))

					self.session.add(find_qrlId)
					self.session.commit()
					result = (find_qrlId.qrlUrlId, find_qrlId.qrlRetId)
					self.session.close()
					return result
				except Exception as e:
					print(e)
					self.session.close()
					sleep(1)
					continue