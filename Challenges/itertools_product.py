import itertools
# Somewhat like permutations and combinations but here it is the different
a = input().split(' ')
a = list(map(int,a))
b = input().split(' ')
b = list(map(int,b))
for i in list(itertools.product(a,b)):
    print(i , end = " ")