# -*- coding: utf-8 -*-
import random
from collections import Counter
data=[random.choice(xrange(1,10)) for _ in range(100)] 
s=Counter(data)
key=sorted((zip(s.keys(),s.values())),key=lambda x: x[1])
sorts=[]
def sort_index():
	for tubles in key:
		lists=list(tubles)
		index=int(lists[1])
		while index>0:
			sorts.append(lists[0])
			index=index-1
	return sorts
print s
print sort_index()



		















