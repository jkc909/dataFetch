from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class create_session():
	def __init__(self):
		self.Engine = create_engine('mysql+pymysql://root:qwerty1!@127.0.0.1/dataFetch')
		self.Sessionmaker = sessionmaker(bind=self.Engine)

	def return_session(self):
		session = self.Sessionmaker()
		return session