import urlparse
import urllib
from bs4 import BeautifulSoup

url = "http://www.redweb.com"

def Crawler(url):

	urls = [url]
	visited = [url]

	#Download the page
	domainhtml = urllib.urlopen(url).read()
	domainsoup = BeautifulSoup(domainhtml)

	#Scrape the page
	#Scrape domain stuff
	#Scrape page stuff
	print "Scraped domain page"

	#Get all the urls in the page
	GetUrls(domainsoup, urls, visited)

	print urls

	while (len(urls) > 0) and (len(visited) < 30):
		for pageurl in urls:

			#Download the page
			pagehtml = urllib.urlopen(url).read()
			pagesoup = BeautifulSoup(pagehtml)

			#Get all the urls in the page
			GetUrls(pagesoup, urls, visited)

			#Scrape the page
			print "Scrape the specific page"
			print pageurl

			urls.pop(0)

	print len(visited)

def GetUrls(soup, urls, visited):

	for tag in soup.findAll('a', href=True):
		#Ensures the top level domain is included
		currenturl = urlparse.urljoin(url, tag['href'])

		#Check that the url goes to the website we are scraping
		#Make sure we haven't already visited it
		if (url in currenturl) and (currenturl not in visited):
			#Add to urls to scrape
			urls.append(currenturl)
			visited.append(currenturl)

Crawler(url)

