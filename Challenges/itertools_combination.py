import itertools
l = lambda a : print("".join(a),end = "\n")
word = input().split(' ')
word[0] = sorted(word[0])

for i in range(0,int(word[1])):
    len_list = list(itertools.combinations(word[0],i+1))
    len_list = list(map(l,len_list))   




# list(itertools.combinations(word,2))