import time
t = time.time()
s = str(t)
delset = '.'
l = s.translate(None,delset)

print "s:" + s
print "l:" + l


