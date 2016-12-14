# encoding: utf-8
import sys as mysys
reload(mysys)
mysys.setdefaultencoding('utf-8')

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from ScspDev import CommonUtils
#from Scsp import CommonUtils as Cm2
#from .. Scsp import Ytools2
#import Scsp


#from Lib.Scsp import CommonUtils


#print Scsp._version_

cm = CommonUtils()

print cm.sp_test("silly")
cm.sp_version()
print cm.yt_md5("silly2")
print type(cm.yt_md5("silly2"))



#md5_str = cm.yt_md5("silly")

#print md5_str

#print cm.sp_test("silly11")


