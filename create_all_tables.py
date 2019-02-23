from sqlalchemy import *

from ORM.tables.tblRetailer import *
from ORM.tables.tblCrawlResult import *
from ORM.tables.tblDynamic import *
from ORM.tables.tblHeaders import *
from ORM.tables.tblPLCrawlResult import *
from ORM.tables.tblStatic import *
from ORM.tables.tblUrlQueue import *
from ORM.tables.tblUrls import *
from ORM.tables.tblMatches import *
from ORM.tables.tblCaptcha import *

from sqlalchemy.schema import CreateSchema
from sqlalchemy.orm import sessionmaker



from dbBase import Base

# from engine_session import create_engine

# Engine = create_engine('mysql+pymysql://root:qwerty1!@127.0.0.1')
# # Engine = create_engine('postgres://127.0.0.1')

# metadata = MetaData(bind=Engine)

# Engine.execute(CreateSchema('fetch_refresh'))


Engine = create_engine('mysql+pymysql://root:qwerty1!@127.0.0.1/fetch_refresh')

# # Engine = create_engine('postgres://127.0.0.1/match-maker_test')

# Base.metadata.create_all(Engine)

# session = engine_session().create_engine()

Sessionmaker = sessionmaker(bind=Engine)

session = Sessionmaker()

add_amazon = Retailer('Amazon')
add_sweetwater = Retailer('Sweetwater')

add_crawl_type1 = PLCrawlResult('Success')
add_crawl_type2 = PLCrawlResult('Blocked')
add_crawl_type3 = PLCrawlResult('Data Error')


header = Headers({'DNT': '1', 'Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'})

# session.add(add_amazon)
# session.add(add_sweetwater)

session.add(add_crawl_type1)
session.add(add_crawl_type2)
session.add(add_crawl_type3)
session.add(header)

session.commit()

session.flush()


# print(metadata)
# print(Engine)
# print(Urls)