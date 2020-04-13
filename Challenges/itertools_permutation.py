#Permutation creates different combinations
import itertools
para = input().split(' ') # Enter a string and an int separated by ' '
s = itertools.permutations(para[0],int(para[1]))
for i in sorted(list(s)):
    print("".join(i))


