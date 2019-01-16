from app import app
from app import db
# from app.tables import *
from app.tables.tblRetailer import Retailer
from app.tables.tblUrls import Urls
from app.tables.tblUrlQueue import UrlQueue
from app.tables.tblStatic import Static
from app.tables.tblDynamic import Dynamic
from app.tables.tblCrawlResult import CrawlResult
from app.tables.tblCaptcha import Captcha



class urlUpsert():
	def __init__(self, url):
		results = db.session.query(Urls).filter(Urls.urlUrl == url).all()
		try:
			urlId = results[0].urlId
			try:
				qrlId = db.session.query(UrlQueue).filter(UrlQueue.qrlUrlId == urlId).all()[0].qrlId
				update_qrl = db.update(UrlQueue).where(UrlQueue.qrlId == qrlId).values(qrlAck=0)
				db.session.execute(update_qrl)
				db.session.commit()
			except Exception as e:
				insert_qrl = UrlQueue(qrlUrlId = urlId, qrlAck=0, qrlRetId = 1)
				db.session.add(insert_qrl)
				db.session.commit()

		except:
			insert_url = Urls(urlUrl = url, urlRetId = 1)
			db.session.add(insert_url)
			db.session.commit()
			db.session.refresh(insert_url)
			urlId = insert_url.urlId
			db.session.flush()
			insert_qrl = UrlQueue(qrlUrlId = urlId, qrlAck=0, qrlRetId = 1)
			db.session.add(insert_qrl)
			db.session.commit()
		db.session.flush()
		# return(type(results))