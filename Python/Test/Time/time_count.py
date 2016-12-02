import time
from datetime import datetime


def compute(i):
	for i in range(1,i):
		i = i+1
	return i

start_time = datetime.now()
print "start:%s" % str(start_time)

n =  compute(100000)

end_time = datetime.now()
print "end:%s" % str(end_time)
#elapsed_time = end_time - start_time

#print "elapsed_time:%s" % str(elapsed_time)

#print "start:%r, End:%r" % (start_time, end_time)



#rint datetime.now()