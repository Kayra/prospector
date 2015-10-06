import urllib
from bs4 import BeautifulSoup

url = "http://www.redweb.com"

htmltext = urllib.urlopen(url).read()

soup = BeautifulSoup(htmltext)

domainurl = url

internallinksno = 0
for link in soup.findAll('a', href=True):
	try:
		if (domainurl in link['href']) or ('.' not in link['href']):
			internallinksno += 1
	except KeyError:
		print 'Key error: link tag did not contain href attribute'

print internallinksno