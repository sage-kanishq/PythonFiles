import itertools
word,num = input().split(' ')
l = lambda a : print("".join(a),end = '\n')
k = list(itertools.combinations_with_replacement(sorted(word),int(num)))
k = list(map(l,k))




# list(itertools.combinations_with_replacement(sorted(word),int(num)))