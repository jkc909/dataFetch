from fuzzywuzzy import fuzz

from sqlalchemy import *

from ORM.tables.tblCrawlResult import *
from ORM.tables.tblDynamic import *
from ORM.tables.tblHeaders import *
from ORM.tables.tblPLCrawlResult import *
from ORM.tables.tblRetailer import *
from ORM.tables.tblStatic import *
from ORM.tables.tblUrlQueue import *
from ORM.tables.tblUrls import *
from ORM.tables.tblMatches import *
from ORM.tables.tblCaptcha import *

from dbBase import Base

from engine_session import create_session


session = create_session().return_session()



skip_matched = session.query(Matches.matBaseStaId).distinct()

retailer_1_product = session.query(Urls, Static, Dynamic).\
							join(Static, Dynamic).\
							filter(Static.staRetId==1, Static.staId.notin_(skip_matched)).\
							with_entities(Static.staId, Static.staBrand, Static.staPartNumber, Static.staProductName, Dynamic.dynPrice, Static.staRetId).\
							limit(10000).\
							all()



retailer_2_products = session.query(Urls, Static, Dynamic).\
							join(Static, Dynamic).\
							filter(Static.staRetId==2).\
							with_entities(Static.staId, Static.staBrand, Static.staPartNumber, Static.staProductName, Dynamic.dynPrice).\
							all()


for row in skip_matched:
	print(row)

for row in retailer_1_product:
	print(row)






for ret_1_prod in retailer_1_product:
	print("-------------------------------------------")
	print("Amazon: " + ''.join(str(ret_1_prod)))
	print("-------------------------------------------")
	ret_1_price = ret_1_prod[4]
	ret_1_staId = ret_1_prod[0]
	ret_1_id = ret_1_prod[5]

	for row in retailer_2_products:
		print("Sweetwater: " + ''.join(str(row)))
		manufacturer_ratio = fuzz.ratio(ret_1_prod[1], row[1])
		partnumber_ratio = fuzz.ratio(ret_1_prod[2], row[2])
		productname_ratio = fuzz.ratio(ret_1_prod[3], row[3])
		try:
			price_ratio = (abs(abs(ret_1_price - row[4]) / ret_1_price) * 100)
		except:
			price_ratio = 100
		if price_ratio > 20:
			price_ratio = 0
		else:
			price_ratio = 1

		manufacturer_weighted = manufacturer_ratio * 50
		partnumber_weighted = partnumber_ratio * 30
		productname_weighted = productname_ratio * 15
		price_weighted = price_ratio * 5

		weighted_avg = (manufacturer_weighted + partnumber_weighted + productname_weighted + price_weighted) / 100

		match_payload = {'matBaseRetId': ret_1_id, 'matBaseStaId': ret_1_staId, 'matSuggestedStaId': row[0], 'matManufacturerScore': manufacturer_ratio, 'matPartNumberScore': partnumber_ratio, 'matProductNameScore': productname_ratio, 'matPriceScore': price_ratio, 'matAverageScore': weighted_avg}

		print(match_payload)
		if weighted_avg > 50:
			insert_match = Matches(match_payload)
			session.add(insert_match)
			session.commit()
			session.flush()


