a=10
zero=0
one=1
for i in range(a):
	if i==0:
		print(zero,end=' ')
	if i ==1:
		print(one,end=' ')
	else:
		tot=one+zero
		zero=one
		one=tot
		print(tot,end=' ')
