from bs4 import BeautifulSoup

soup = BeautifulSoup("""<html> 

<body> 

<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" 

codebase="http://download.macromedia.com/pub/shockwave/
cabs/flash/swflash.cab#version=6,0,40,0" 
 
width="468" height="60" 
 id="mymoviename"> 

<param name="movie"  

value="http://www.tizag.com/pics/example.swf" /> 
 
<param name="quality" value="high" /> 

<param name="bgcolor" value="#ffffff" /> 

<embed src="http://www.tizag.com/pics/example.swf" quality="high" bgcolor="#ffffff"

width="468" height="60" 

name="mymoviename" align="" type="application/x-shockwave-flash" 

pluginspage="http://www.macromedia.com/go/getflashplayer"> 


</embed> 

</object> 

</body>

</html>""")

flash = ""
for flashtag in soup.find_all('embed'):
	try:
		if '.swf' in flashtag['src']:
			flash = flashtag
	except KeyError:
			print 'Key error: embed tag did not contain an src attribute'

print flash