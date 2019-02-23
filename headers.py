import random
from ORM.tables.tblHeaders import *

def getHeader(session, retId):
	# randId = random.randint(1,7)
	randId = 1
	hedId = session.query(Headers.hedHeader,Headers.hedId).\
				filter(Headers.hedId == randId).\
				first()
	headers = hedId
	session.close()
	return (headers)


