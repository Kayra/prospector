from app import db, models
import urlparse
import urllib
from bs4 import BeautifulSoup
import scraper

def Crawler(url):
	#urls to scrape
	urls = [url]

	#urls scraped
	visited = [url]

	pages = []

	#Download the homepage of the domain
	#Scrape the domain page
	domainhtml = urllib.urlopen(url).read()
	domainsoup = BeautifulSoup(domainhtml)
	domaindata = scraper.DomainScrape(domainsoup, url)
	homepagedata = scraper.PageScrape(domainsoup, url)

	#Cut out the domain name
	domainname = url.split(".")

	#Check if there is a robots file
	#Scrape the robots file
	robotsfile = ""
	robotsurl = urlparse.urljoin(url, 'robots.txt')
	robotsdata = urllib.urlopen(robotsurl).read()
	if robotsdata:
		robotsfile = robotsdata


	#Check if there is a sitemap file
	#Scrape the sitemap file
	sitemapfile = ""
	sitemapurl = urlparse.urljoin(url, 'sitemap.xml')
	sitemapdata = urllib.urlopen(sitemapurl).read()
	if sitemapdata:
		sitemapfile = sitemapdata

	#Add the domain url to the db
	url = url.encode('utf-8')
	s = models.Site(domainurl = url.decode('utf-8'), sitename = domainname[1], binganalytics = domaindata.binganalytics, googleanalytics = domaindata.googleanalytics, robots = robotsfile, sitemap = sitemapfile, ranking = 0)
	db.session.add(s)

	# h = models.Page(pageurl = url.decode('utf-8'), h1s = homepagedata.h1s.decode('utf-8'), h2s = homepagedata.h2s.decode('utf-8'), h3s = homepagedata.h3s.decode('utf-8'), alttags = homepagedata.alttags.decode('utf-8'), metadesc = homepagedata.metadesc.decode('utf-8'), title = homepagedata.title, viewstate = homepagedata.viewstate.decode('utf-8'), pagination = homepagedata.pagination.decode('utf-8'), iframe = homepagedata.iframe, flash = homepagedata.flash.decode('utf-8'), noindexnofollow = homepagedata.noindexnofollow.decode('utf-8'), schematag = homepagedata.schematag, bloglocation = homepagedata.bloglocation.decode('utf-8'), internallinksno = homepagedata.internallinksno, domainsite = s)
	# print type(h)
	# db.session.add(h)
	db.session.commit()

	while len(urls) > 0 :
		try:
			htmltext = urllib.urlopen(urls[0]).read()
		except:
			print urls[0]

		#Format the page with beautiful soup
		soup = BeautifulSoup(htmltext)

		urls.pop(0)

		print "Amount of urls"
		print len(urls)
		pagedata = scraper.PageScrape(soup, url)
		#Add the page url and page data to the db under the relevant domain
		p = models.Page(pageurl = url.decode('utf-8'), h1s = pagedata.h1s.decode('utf-8'), h2s = pagedata.h2s.decode('utf-8'), h3s = pagedata.h3s.decode('utf-8'), alttags = pagedata.alttags.decode('utf-8'), metadesc = pagedata.metadesc.decode('utf-8'), title = pagedata.title, viewstate = pagedata.viewstate.decode('utf-8'), pagination = pagedata.pagination.decode('utf-8'), iframe = pagedata.iframe, flash = pagedata.flash.decode('utf-8'), noindexnofollow = pagedata.noindexnofollow.decode('utf-8'), schematag = pagedata.schematag, bloglocation = pagedata.bloglocation.decode('utf-8'), internallinksno = pagedata.internallinksno, domainsite = s)
		db.session.add(p)
		db.session.commit()

		#find all the links in the page
		for tag in soup.findAll('a', href=True):

			#ensures the top level domain is included
			tag['href'] = urlparse.urljoin(url, tag['href'])

			#check that the url goes to the website we are scraping
			#and make sure we haven't already visited it
			if url in tag['href'] and tag['href'] not in visited:
				#add to urls to scrape
				urls.append(tag['href'])

				#add to urls scraped
				visited.append(tag['href'])

				#add the html to the pages list
				pages.append(soup)


		if len(urls) > 30:
			break

	return domainname[1]
	#print visited

	#print pages[0]
	
	#print 'It dun worked'