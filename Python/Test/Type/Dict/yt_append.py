import collections

d = collections.defaultdict()
d2 = {'test':121}

d['test'] = 11
d2['blue'] = 'color'

print list(d.items())
print d
print d2['blue']
print type(d)
print type(d2)

flag = d2.get('red')
print "flag:%s" % flag
