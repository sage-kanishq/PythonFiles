# Even more efficient than merge sort, whose time efficiency is O(nlogn).
# While counter sort is O(n)

def count_sort(a):
    from collections import defaultdict,Counter
    j = defaultdict(list)
    sort = []
    for i in a:
        j[i].append(i)

    for k,i in j.items():
        sort.extend(i)
    return sort



# a = [1,1,2,3,4,2,7,1]
# print(count_sort(a))
