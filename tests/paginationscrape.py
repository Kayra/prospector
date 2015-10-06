import urllib
from bs4 import BeautifulSoup


url = "http://www.ayima.com/seo-knowledge/conquering-pagination-guide.html"

htmltext = urllib.urlopen(url).read()

soup = BeautifulSoup('<link rel="prev" href="http://www.site.com/page1.html"> <link rel="next" href="http://www.site.com/page3.html">')

pagination = ""
for pagin in soup.find_all('link'):
	try:
		if ('prev' or 'next') in pagin['rel']:
			pagination = pagin
	except KeyError:
			print 'Key error: the input tag did not contain a viewstate attribute.'

print pagination