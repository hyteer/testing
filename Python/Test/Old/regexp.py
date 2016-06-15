# -*- coding: UTF-8 -*-
import re
print(re.match('www','wwww.ifcld.com').span())
print(re.match('www','wwwwww.ifcld.com').group())
print(re.search('cld','www.ifcld.com').span())
print(re.match('cld','www.ifcld.com'))

