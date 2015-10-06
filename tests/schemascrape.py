#from app import db, models
import urlparse
import urllib
from bs4 import BeautifulSoup


url = "http://www.ayima.com/seo-knowledge/conquering-pagination-guide.html"

htmltext = urllib.urlopen(url).read()

soup = BeautifulSoup("""<div itemscope itemtype="http://schema.org/Movie">
  <h1>Avatar</h1>
  <span>Director: James Cameron (born August 16, 1954)</span>
  <span>Science fiction</span>
  <a href="../movies/avatar-theatrical-trailer.html">Trailer</a>
</div>""")

schematag = ""
for schema in soup.find_all('div'):
	try:
		if schema['itemtype']:
			schematag += str(schema) + '#'
	except KeyError:
			print 'Key error: meta tag did not contain content attribute'

print schematag