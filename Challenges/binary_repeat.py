c=format(951,'b')
d=0
ma=0
for e,i in enumerate(c):
	if i=='1':
		d+=1
	if i=='0' or d>ma and e==len(c)-1:
		if d>=ma:
			ma=d
			d=0
		d=0
print(ma)
