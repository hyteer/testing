import re

str = "<retmsg>SUCCESS</retmsg>"

result = re.search("SUCCESS",str)

print "result:",result

if result is not None:
	print "match success!"
