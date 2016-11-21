
from lxml import etree

mytree = etree.xml("<xml><retcode>0</retcode><retmsg>SUCCESS</retmsg></xml>")
str = "<xml><retcode>0</retcode><retmsg>SUCCESS</retmsg></xml>"

retmsg = mytree.xpath("//retmsg")

print "retmsg:",retmsg
