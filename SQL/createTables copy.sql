
DROP TABLE dataFetch.tblUrlQueue;

CREATE TABLE IF NOT EXISTS dataFetch.tblUrlQueue (
    qrlId INT AUTO_INCREMENT,
    qrlUrlId INT, #FOREIGN KEYYYYYY
    qrlUrl VARCHAR(255) NOT NULL,
    qrlRetId INT NOT NULL,
    qrlLastAck DATETIME,
    qrlAck BIT DEFAULT 0,
    qrlPriority TINYINT DEFAULT 0,
    PRIMARY KEY (qrlId, qrlUrl)
)  ENGINE=INNODB;



INSERT INTO dataFetch.tblUrlQueue (qrlUrl, qrlRetId) VALUES ('https://www.amazon.com/dp/B07BHYZRYG',1);
INSERT INTO dataFetch.tblUrlQueue (qrlUrl, qrlRetId) VALUES ('https://www.amazon.com/dp/B07BKQ6M22',1);
INSERT INTO dataFetch.tblUrlQueue (qrlUrl, qrlRetId) VALUES ('https://www.amazon.com/dp/B004M8YPKM',1);
INSERT INTO dataFetch.tblUrlQueue (qrlUrl, qrlRetId) VALUES ('https://www.amazon.com/dp/B00V5BP2H4',1);
INSERT INTO dataFetch.tblUrlQueue (qrlUrl, qrlRetId) VALUES ('https://www.amazon.com/dp/B07D1GNLDM',1);
INSERT INTO dataFetch.tblUrlQueue (qrlUrl, qrlRetId) VALUES ('https://www.amazon.com/dp/B01HZ8UG62',1);
INSERT INTO dataFetch.tblUrlQueue (qrlUrl, qrlRetId) VALUES ('https://www.amazon.com/dp/B01N8ZRV3V',1);
INSERT INTO dataFetch.tblUrlQueue (qrlUrl, qrlRetId) VALUES ('https://www.amazon.com/dp/B00684KFFW',1);
INSERT INTO dataFetch.tblUrlQueue (qrlUrl, qrlRetId) VALUES ('https://www.amazon.com/dp/B00CAKSVTU',1);
INSERT INTO dataFetch.tblUrlQueue (qrlUrl, qrlRetId) VALUES ('https://www.amazon.com/dp/B00G31YMVS',1);
INSERT INTO dataFetch.tblUrlQueue (qrlUrl, qrlRetId) VALUES ('https://www.amazon.com/dp/B0000WS0SC',1);



update dataFetch.tblUrlQueue set qrlAck = 1 where qrlId  in (6,12,4,5);

update dataFetch.tblUrlQueue set qrlAck = 0 where qrlId in (10);










select * from dataFetch.tblUrlQueue where qrlPriority = 1;

update dataFetch.tblUrlQueue set qrlUrlId = 1 where qrlId in (2)

update dataFetch.tblUrlQueue set qrlPriority = 1 where qrlId in (6,12,4,5)


update dataFetch.tblUrlQueue set qrlPriority = 0 where qrlId > 1;


CREATE TABLE IF NOT EXISTS dataFetch.tblRetailer (
    retId INT AUTO_INCREMENT,
    retName VARCHAR(255) NOT NULL,
    PRIMARY KEY (retId, retName)
)  ENGINE=INNODB;


INSERT INTO dataFetch.tblRetailer (retName) VALUES ('Amazon2')

select * from dataFetch.tblRetailer 




CREATE TABLE IF NOT EXISTS dataFetch.tblUrls (
	urlId INT AUTO_INCREMENT,
	urlUrl VARCHAR(255) NOT NULL,
	urlRetId INT,
	urlBadUrl BIT,
	urlBadUrlReason INT,
	urlBadUrlLastDate DATETIME,
	urlBadUrlHistory INT,
	urlDateInserted DATETIME,
	urlDateModified DATETIME,
	urlPriority INT,
	urlNotes VARCHAR(255),

    PRIMARY KEY (urlId, urlUrl)
)  ENGINE=INNODB;

SELECT * FROM dataFetch.tblUrls;




INSERT INTO dataFetch.tblUrls (urlUrl, urlRetId) VALUES ('https://www.amazon.com/dp/B07BKQ6M22',1);
INSERT INTO dataFetch.tblUrls (urlUrl, urlRetId) VALUES ('https://www.amazon.com/dp/B07BKQ6M22',1);
INSERT INTO dataFetch.tblUrls (urlUrl, urlRetId) VALUES ('https://www.amazon.com/dp/B004M8YPKM',1);
INSERT INTO dataFetch.tblUrls (urlUrl, urlRetId) VALUES ('https://www.amazon.com/dp/B00V5BP2H4',1);
INSERT INTO dataFetch.tblUrls (urlUrl, urlRetId) VALUES ('https://www.amazon.com/dp/B07D1GNLDM',1);
INSERT INTO dataFetch.tblUrls (urlUrl, urlRetId) VALUES ('https://www.amazon.com/dp/B01HZ8UG62',1);
INSERT INTO dataFetch.tblUrls (urlUrl, urlRetId) VALUES ('https://www.amazon.com/dp/B01N8ZRV3V',1);
INSERT INTO dataFetch.tblUrls (urlUrl, urlRetId) VALUES ('https://www.amazon.com/dp/B00684KFFW',1);
INSERT INTO dataFetch.tblUrls (urlUrl, urlRetId) VALUES ('https://www.amazon.com/dp/B00CAKSVTU',1);
INSERT INTO dataFetch.tblUrls (urlUrl, urlRetId) VALUES ('https://www.amazon.com/dp/B00G31YMVS',1);
INSERT INTO dataFetch.tblUrls (urlUrl, urlRetId) VALUES ('https://www.amazon.com/dp/B0000WS0SC',1);











CREATE TABLE IF NOT EXISTS dataFetch.tblUrls (
	urlId INT AUTO_INCREMENT,
	urlUrl VARCHAR(255) NOT NULL,
	urlRetId INT,
	urlBadUrl BIT,
	urlBadUrlReason INT,
	urlBadUrlLastDate DATETIME,
	urlBadUrlHistory INT,
	urlDateInserted DATETIME,
	urlDateModified DATETIME,
	urlPriority INT,
	urlNotes VARCHAR(255),

    PRIMARY KEY (urlId, urlUrl)
)  ENGINE=INNODB;



drop table dataFetch.tblStatic ;

CREATE TABLE IF NOT EXISTS dataFetch.tblStatic (
	staId INT AUTO_INCREMENT,
	staUrlId INT NOT NULL,  
	staRetId INT,
	staProductName VARCHAR(255),
	staBreadcrumb VARCHAR(255),
	staOptionName VARCHAR(255),
	staChildIdentifier VARCHAR(255) NOT NULL,
	staParentIdentifier VARCHAR(255),
	staPartNumber VARCHAR(255),
	staImageCount VARCHAR(255),
	staDescription TEXT,
	staMainImage VARCHAR(255),
	staShippingWeight FLOAT,
	staShippingWeightUnit VARCHAR(50),
	staBestSeller1 VARCHAR(255),
	staBestSeller2 VARCHAR(255),
	staBestSeller3 VARCHAR(255) ,
	staFirstAvailable DATETIME,
	staBrand VARCHAR(255),
	staItemWeight FLOAT,
	staItemWeightUnit VARCHAR(255),
	staDimensions VARCHAR(255),
	staDimensionsUnit VARCHAR(50),
	staAplus BIT,
    
        PRIMARY KEY (staId, staChildIdentifier)
)  ENGINE=INNODB;



select * from dataFetch.tblStatic;

update dataFetch.tblStatic set staUrlId = 425 where staId in (1,2,3,4, 5);
update dataFetch.tblStatic set staUrlId = 41 where staId in (1,2,3,4);


drop table dataFetch.tblDynamic;

CREATE TABLE IF NOT EXISTS dataFetch.tblDynamic (
	dynId INT AUTO_INCREMENT,
	dynStaId INT NOT NULL,
    dynRetId INT,
	dynPrice FLOAT,
	dynStockStatus BIT,
	dynSeller VARCHAR(255) ,
	dynShippedBy VARCHAR(255) ,
	dynShipPrice FLOAT,
	dynAnsweredQuestions INT,
	dynRating FLOAT,
	dynReviewCount INT,
	dynStockMessage VARCHAR(255) ,
	dynZipCode VARCHAR(16) ,
	dynCrawlTime DATETIME,
        PRIMARY KEY (dynId)
)  ENGINE=INNODB;

select * From dataFetch.tblDynamic;


drop table dataFetch.tblHeaders;

CREATE TABLE IF NOT EXISTS dataFetch.tblHeaders (
	hedId INT AUTO_INCREMENT,
    hedHeader JSON NOT NULL,
	-- hedHeader VARCHAR(255)  NOT NULL,
    hedDateAdded DATETIME DEFAULT NOW(),
    hedScore INT DEFAULT 0,
        PRIMARY KEY (hedId)
)  ENGINE=INNODB;



insert into dataFetch.tblHeaders (hedHeader) values ("'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'");




insert into dataFetch.tblHeaders (hedHeader) values ("'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'");
insert into dataFetch.tblHeaders (hedHeader) values ("'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'");
insert into dataFetch.tblHeaders (hedHeader) values ("'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'");
insert into dataFetch.tblHeaders (hedHeader) values ("'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'");
insert into dataFetch.tblHeaders (hedHeader) values ("'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'");
insert into dataFetch.tblHeaders (hedHeader) values ("'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'");

select * From dataFetch.tblHeaders;