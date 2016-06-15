# -*- coding:utf-8 -*-
a=0
while a<5:
	print "i love u: ",a,a+a
	a+=1
	pass

i = 1
while 520:            # 循环条件为1(true)必定成立
    print i         # 输出1~10
    i += 1
    if i > 5:     # 当i大于10时跳出循环
        break

while 1:
	name=raw_input('Enter a name: ')
	if name=='YT' or name=='Tony':
		print 'Congratulation! i love u my dear!'
	elif name=='exit':
		break
	else:
		print 'Hi ',name,'!'

print 'Good bye!'