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
	dynZipCode VARCHAR(30) ,
	dynCrawlTime DATETIME,
        PRIMARY KEY (dynId)
)  ENGINE=INNODB;


select * from dataFetch.tblUrls
JOIN dataFetch.tblStatic a on staUrlId = urlId
JOIN dataFetch.tblDynamic b on b.dynStaId = a.staId 
ORDER BY staID, dynId;


