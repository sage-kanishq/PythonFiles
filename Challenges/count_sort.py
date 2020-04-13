
def sorter(arr):
    indexes = [None]*max(arr)
    sort = []
    for i in range(len(arr)):
        try:
            if indexes[arr[i]]!=None:
                indexes.insert(arr[i],arr[i])     
            else:
                indexes[arr[i]]=arr[i]
        except Exception as e:
            indexes.insert(arr[i],arr[i])       
    for i in range(len(indexes)):
        if indexes[i]!=None:
            sort.append(indexes[i])
    return sort





