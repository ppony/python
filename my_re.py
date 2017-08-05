import re

p=re.compile(r'b')
m=p.findall('abxd b')
print(m)

p = re.compile('\d+')
#m = p.findall('12 drummer, 11 pipers')
#print(m)
#print(p.sub('-','abxd'))

iterator = p.finditer('12 ddd, 11 ppp')
for m in iterator:
	print(m)


