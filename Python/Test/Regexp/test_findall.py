import re

url = 'http://betanewwsh.snsshop.net'
match = re.findall(r'(?<=http://).*', url)

print match[0]
