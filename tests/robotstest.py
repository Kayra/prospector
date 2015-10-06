import urlparse
import urllib

url = "www.redweb.com"

robotsfile = ""
robotsurl = urlparse.urljoin('http://www.redweb.com', 'robots.txt')

robotsdata = urllib.urlopen(robotsurl).read()

if robotsdata:
	robotsfile = robotsdata

print robotsfile