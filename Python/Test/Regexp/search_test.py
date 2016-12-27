import re

str = "<retmsg>SUCCESS</retmsg>"

result = re.search("SUCCESS",str)

print "result:",result
print result.string

if result is not None:
	print "match success!"
