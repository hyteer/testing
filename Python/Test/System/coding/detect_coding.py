import urllib
html = urllib.urlopen('http://www.chinaunix.net').read()
html_wsh = urllib.urlopen('http://testnewwsh.snsshop.net').read()
import chardet
print chardet.detect(html_wsh)
