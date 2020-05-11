from Demo_log_package.log import log


def complex():
	try:
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

	except Exception as e:
		log.logged(e,log.getNameOfFile(__file__))
complex()