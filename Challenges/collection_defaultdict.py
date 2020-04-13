import collections
# Makes a dictionary with lots of features

a,b = list(map(int,input().split(' ')))
array_a = collections.defaultdict(list)
array_b = []
for i in range(a):
    letters = input()
    array_a[letters].append(str(i+1))

for i in range(b):
    letters = input()
    if letters in array_a:
        print(" ".join(array_a[letters]))

    else:
        print(-1)

print(array_a)
