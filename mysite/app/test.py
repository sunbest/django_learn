# -*- coding: utf-8 -*-
import xlrd
workbook = xlrd.open_workbook(r'C:\Python27\Scripts\test.xlsx')
sheet2 = workbook.sheet_by_index(1)
#print sheet2.col(1)[2].value
row_one = sheet2.col_values(0)
row_two = sheet2.col_values(1)
row_three = sheet2.col_values(2)
ID=[ID for ID in row_one ]
name=[name for name in row_two ]
principal=[pricipal for pricipal in row_two ]
d=zip(ID,name,pricipal)
for school in d:
	print school









	

		



	



