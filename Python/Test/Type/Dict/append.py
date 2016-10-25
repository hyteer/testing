import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

d = collections.defaultdict(list)
d2 = {'test':121}
for k, v in s:
    d[k].append(v)

d['test'].append('value')

print list(d.items())
print d
print d['blue']
print type(d)
print type(d2)