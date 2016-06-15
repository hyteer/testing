# _*_ coding:UTF-8 _*_
# for and while nesting
''' 求2~100之间的素数'''
i = 2
while(i<100):
	j = 2
	while(j <= (i/j)):
		if not(i%j): break
		j = j+1
	if (j > i/j): print i, "是素数"
	i = i+1

print "Good bye"

