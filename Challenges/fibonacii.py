def fib(r=0,zero=0,one=1,count=0):
    for i in range(r):
        if i == 0:
            print(0,end=" ")

        elif i == 1:
            print(1,end=" ")

        else:
            zero,one = one,zero+one
            print(one,end=" ")

    
fib(10)

        
    