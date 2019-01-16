from app import app
from app import db
# from app.tables import *
from app.tables.tblUrls import Urls
from app.tables.tblUrlQueue import UrlQueue
from app.tables.tblStatic import Static
from app.tables.tblDynamic import Dynamic
from app.tables.tblCrawlResult import CrawlResult
from app.tables.tblCaptcha import Captcha

from sqlalchemy.inspection import inspect

from flask_table import Table, Col



class getData():
	def __init__(self, url):
		self.results = db.session.query(Urls).filter(Urls.urlUrl == url).all()
		self.get_the_data()


	def get_the_data(self):
		try:
			urlId = self.results[0].urlId
			try:
				self.get_data = db.session.query(Static, Dynamic).join(Dynamic, Dynamic.dynStaId == Static.staId).filter(Static.staUrlId == urlId).first()
				self.return_data = [t.__dict__ for t in self.get_data]
				print(return_data)
				return self.return_data
			except:
				pass
		except:
			pass


# test = getData('https://www.amazon.com/dp/B005M02VNW')
# print(test)


		# 		update_qrl = db.update(UrlQueue).where(UrlQueue.qrlId == qrlId).values(qrlAck=0)
		# 		db.session.execute(update_qrl)
		# 		db.session.commit()
		# 	except Exception as e:
		# 		insert_qrl = UrlQueue(qrlUrl = url, qrlUrlId = urlId, qrlAck=0, qrlRetId = 1)
		# 		db.session.add(insert_qrl)
		# 		db.session.commit()

		# except:
		# 	insert_url = Urls(urlUrl = url, urlRetId = 1)
		# 	db.session.add(insert_url)
		# 	db.session.commit()
		# 	db.session.refresh(insert_url)
		# 	urlId = insert_url.urlId
		# 	db.session.flush()
		# 	insert_qrl = UrlQueue(qrlUrl = url, qrlUrlId = urlId, qrlAck=0, qrlRetId = 1)
		# 	db.session.add(insert_qrl)
		# 	db.session.commit()
		# db.session.flush()
		# # return(type(results))