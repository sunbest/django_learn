# -*- coding: utf-8 -*-
import random
n=random.randint(1,100)
sum=0
N=0
while N!=n and sum<5:
	print u'请输入1-100之间的任意数' 
	values=True
	while values:
		try:
			N=int(raw_input())
		except ValueError:
			print u'请重新输入'
		else:
			values=False
	sum=sum+1
	while N>100 or N<0:
		print u'范围不对,1-100之间的数'
		N=int(raw_input())
	if N==n:
		print u'恭喜你猜对了，你猜了%d 次' % sum
		exit()
	else:
		if N>n:
			print u'你输入的太大' 
		else:
			print u'你输入的太小'  
print u'抱歉次数已达到5次'


	



