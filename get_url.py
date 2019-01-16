from ORM.tables.tblUrls import *

def get_url(session, urlId_retId):
	url = session.query(Urls.urlUrl).\
					filter(Urls.urlRetId == urlId_retId[1],\
							Urls.urlId == urlId_retId[0]).\
							first()
	return_value = url[0]
	session.close()
	return return_value