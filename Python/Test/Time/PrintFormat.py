import time
from datetime import datetime
now = datetime.now()

strnow = now.strftime("%Y-%m-%d_%H_%M_%S") + str(now.microsecond)
print "Now:%s%s"%(now.strftime("%Y-%m-%d_%H_%M_%S"),now.microsecond)
print "Now string:",strnow
