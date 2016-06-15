# _*_ coding: UTF-8 _*_

for num in range(10,20):	# Iteration 10 to 20
	for i in range(2,num):
		if num%i == 0:	# 确定第一个因子
			j = num/i
			print '%d 等于 %d * %d' % (num,i,j)
			break	# 跳出质数
	else:		# 循环的 else 部分
			print num, '是一个质数'
