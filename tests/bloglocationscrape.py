#from app import db, models
import urlparse
import urllib
from bs4 import BeautifulSoup


url = "http://www.ayima.com/seo-knowledge/conquering-pagination-guide.html"

htmltext = urllib.urlopen(url).read()

soup = BeautifulSoup("""<section class="eight columns">
				<nav class="links">
					<ul>
						<li><a href="#">blog</a></li>
						<li><a href="blog">research and development</a></li>
						<li><a href="#">fitness</a></li>
					</ul>
				</nav>
			</section>""")

bloglocation = ""
for blog in soup.findAll('a', href=True):

	try:
		if ('blog' in str(blog)) or ('blog' in blog['href']):
			bloglocation += blog['href'] + '@'
	except KeyError:
			print 'Key error: meta tag did not contain content attribute'

print bloglocation