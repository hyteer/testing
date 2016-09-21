import re

str = 'ng-if="item.event == 3"'

match = re.search(r'(?<=\bevent.==.)\w+\b', str)

print "matches:",match.group()

####
str2 = '-Ewmsls-eWMMDn-'
search = re.search('ewm', str2, flags=re.IGNORECASE)
match = re.match(r'Ewm', str2, flags=0)
findall = re.findall(r'Ewm', str2, flags=re.IGNORECASE)
matlist = re.split(r'\bEwm\w', str2,maxsplit=0, flags=re.IGNORECASE)


print "match str2:",findall



####

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

print "matches#2:",searchObj.span()




