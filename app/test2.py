import re

url = 'http://www.stackoverflow.com/questions/569137/how-to-get-domain-name-from-url'

domainname = re.match(r'get', url, re.M|re.I),  

domainnamee = url.split(".")

print domainnamee[1]

# line = "Cats are smarter than dogs"

# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

# if matchObj:
# 	print "matchObj.group() : ", matchObj.group()
# 	print "matchObj.group(1) : ", matchObj.group(1)
# 	print "matchObj.group(2) : ", matchObj.group(2)
# else:
# 	print "No match!!"