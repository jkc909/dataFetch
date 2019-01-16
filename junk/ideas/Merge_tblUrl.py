

class Merge_tblUrl():

	def __init__(self, dic):
		self.url = dic.urlUrl
		self.retId = dic.urlRetId 
		self.dic = dic


	def Upsert(self):
		try:
			ID = Merge_tblUrl.CheckPK(self, self.url, self.retId)
			Merge_tblUrl.Update_tblUrl(self.dic, ID)
		except:
			Merge_tblUrl.Insert_tblUrl(self.dic)

	def CheckPK(self, url, retId):
		try:
			ID = session.query(Urls).filter(Urls.urlUrl == url, Urls.urlRetId == retId).first().urlId
			print(ID)
			return ID
		except NoResultFound:
			return

	def Insert_tblUrl(dic):
		dic.urlDateInserted = datetime.now().replace(microsecond=0)
		dic.urlDateModified = datetime.now().replace(microsecond=0)
		dic.urlBadUrl = 0
		dic.urlBadUrlHistory = 0
		dic.urlPriority = 1
		print('heldfdfasfasdlo')
		session.add(dic)
		session.commit()

	def Update_tblUrl(dic, UurlId):
		pass
		# x = update(Urls.__table__).\
		# 		where(Urls.urlId == UurlId).\
		# 		values(urlBadUrl=1)
		# print(x.execution_options())
		# Engine.execute(x)
		# session.flush()