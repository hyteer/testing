# -*- coding:utf-8 -*-
def total(a,b):
	print a+b;
	pass

info = { 'name': '永堂', 'sex': 'Male', 'height':172, 'age':32}

def showInfo(num,x):
	if num>=5:
		print info[x]

showInfo(8,'sex')