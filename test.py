from ORM.tables.tblCrawlResult import *
from ORM.tables.tblDynamic import *
from ORM.tables.tblHeaders import *
from ORM.tables.tblPLCrawlResult import *
from ORM.tables.tblRetailer import *
from ORM.tables.tblStatic import *
from ORM.tables.tblUrlQueue import *
from ORM.tables.tblUrls import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from sqlalchemy.ext.declarative import declarative_base
db = declarative_base()


Engine = create_engine('mysql+pymysql://root:qwerty1!@127.0.0.1/dataFetch')
Sessionmaker = sessionmaker(bind=Engine)


session = Sessionmaker()

urlId = 8

static_data = session.query(Static, Dynamic).join(Dynamic, Dynamic.dynStaId == Static.staId).filter(Static.staUrlId == urlId).all()[0][1].__dict__
print(static_data)
