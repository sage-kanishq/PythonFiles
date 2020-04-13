import collections
# Collecions Counter makes a dict in where it shows how many times does a value occur in an array
len_size = int(input())
sizes = list(map(int,input().split(' ')))
manage = collections.Counter(sizes)
days_pay = 0
for i in range(int(input())):
    need_size,cost = list(map(int,input().split(' ')))
    if need_size in manage.keys() and manage[need_size]>0:
        manage[need_size]-=1
        days_pay += cost
print(days_pay)