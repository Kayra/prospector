from bs4 import BeautifulSoup

htmltext = """
<head>
	<meta name="msvalidate.01" content="67432G234FR634H326543F" />
</head>

<body>
<script type="text/javascript">
	if (!window.mstag) 
	mstag = {loadTag : function(){},time
</script>
</body> """

soup = BeautifulSoup(htmltext)

for script in soup.find_all('script'):
	if script.string and 'mstag' in script.string:
		print script.string
		break

for meta in soup.find_all('meta'):
	try:
		if 'msvalidate' in meta['name']:
			print meta
			break
	except KeyError:
		print 'Key error: meta tag did not contain name attribute'
