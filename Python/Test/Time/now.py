import time
from datetime import datetime

def now():
    now = str(datetime.now())
    return now

print "Now is: " + now()

time.sleep(1.4)

print "Now is: " + now()
