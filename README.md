# dataFetch
Web crawling platform for scraping e-commerce pages and generating fuzzy match suggestions

# About
Hello and thank you for checking out dataFetch. This application is my first big side project as a developer, and as I built it I taught myself Python. I built the application for self enrichment while I was attending Launch Academy, a web development bootcamp focusing on Rails and React. I had a lot of fun building this application and it was an amazing learning process for me. That being said, please keep in mind this is still a work in progress and I am still learning new things every day :)

I built this application using Python and MySQL. Main Python libraries used include SqlAlchemy, Beautifulsoup, Flask and fuzzywuzzy.

Also be sure to check out my related application matchMaker, it is a UI for reviewing match suggestions built with Rails and React: https://github.com/jkc909/match-maker

### Some features of dataFetch:
- New products can be added to an existing retailer simply by inserting a new URL
- The master.py file triggers the crawling process and listens to the database for new URLs to be added to the queue
- Crawls are triggered when URLs in the queue are marked for crawling
- Crawl results are divided into two data types and stored accordingly: Static data (product name, brand, part number, etc) and Dynamic data (price, review count, shipping estimates, etc)
- Status of crawl attemps are stored for review (captchas, 404s, parser errors, etc)
- Users can schedule URLs to be crawled periodically
- Users can customize and dynamically change headers they use to make HTTP requests
- Users can add new retailers to be scraped; new retailers are easily integrated into the data structure
- When developing a new spider/parser, users can use the TDD (unittest) process I've developed that make sure the correct data types are being returned
- Users can run groups of products through the matching algorithem to generate a list of potential match pairs

For a visual overview of how the application works, I put together this diagram that demonstrates the lifecycle of a crawl:
https://drive.google.com/file/d/1ulUbgYF2WlA6SK955dz_Cr7WUWTQ9pQO/view?usp=sharing

As well as this ER diagram of my database:
https://drive.google.com/file/d/1FOQD-_1HNvV-ozuXO72Wyjway_bDlowO/view?usp=sharing

Please feel free to reach out to me with any questions, and thank you for checking out dataFetch!
