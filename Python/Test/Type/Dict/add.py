from collections import defaultdict
initial_list = [
    ['G1R', '2.56'],
    ['E219D', '11.56'],
    ['L335D', '2.56'],
    ['E248D', '90.28'],
    ['E219D', '2.56'],
    ['G1R', '15.78'],
    ['L335D', '2.56'],
]
d = defaultdict(list)
for k, v in initial_list:
    d[k].append(v)  # possibly `int(v)` ?

print d