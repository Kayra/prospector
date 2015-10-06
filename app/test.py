#from app import db, models
import urlparse
import urllib
from bs4 import BeautifulSoup


url = "http://robbycowell.com/"

htmltext = urllib.urlopen(url).read()

soup = BeautifulSoup(htmltext)

for script in soup.find_all('script'):
	if ('urchin' or 'googleanalytics') in script:
		if script.string:
			print script.string
		else:
			print script
		break;
	elif script.string and ('googleanalytics' or '_uacct' or 'pageTracker') in script.string.lower():
		if script.string:
			print script.string
		else:
			print script
		break;