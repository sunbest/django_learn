import re
filters=re.findall(r"\b(\d+)\b",open("data_test.txt",'r', re.I).read())
line=[int(s) for s in filters ]
print line











