import math

def rimes(num):
    a = True
    for i in range(1,int(math.sqrt(num))):
        if num%i==0:
            a=False
            break
    return a
            
print(rimes(4))
# a= 0

# while a<26:
#     letter = chr(65+a)

    