from bs4 import BeautifulSoup

soup = BeautifulSoup("""<html>
<head>
<title>...</title>
<META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW">
</head>
</html>""")

noindexnofollow = ""
for noindextag in soup.find_all('meta'):
	try:
		if 'noindex, nofollow' in noindextag['content'].lower():
			noindexnofollow = noindextag
	except KeyError:
			print 'Key error: meta tag did not contain content attribute'

print noindexnofollow