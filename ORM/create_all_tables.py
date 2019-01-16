from sqlalchemy import *

from tables.tblCrawlResult import *
from tables.tblDynamic import *
from tables.tblHeaders import *
from tables.tblPLCrawlResult import *
from tables.tblRetailer import *
from tables.tblStatic import *
from tables.tblUrlQueue import *
from tables.tblUrls import *

from sqlalchemy.schema import CreateSchema

from dbBase import Base




Engine = create_engine('mysql+pymysql://root:qwerty1!@127.0.0.1')

metadata = MetaData(bind=Engine)

Engine.execute(CreateSchema('fetch_test'))

Engine = create_engine('mysql+pymysql://root:qwerty1!@127.0.0.1/fetch_test')

Base.metadata.create_all(Engine)

print(metadata)
print(Engine)
# print(Urls)