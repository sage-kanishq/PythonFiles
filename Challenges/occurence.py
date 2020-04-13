import itertools as it
string = input()
for key, grp in it.groupby(string):
    print(f'({len(list(grp))},{key})',end = ' ')