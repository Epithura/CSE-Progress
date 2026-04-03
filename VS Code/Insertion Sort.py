def ins_sort(L):
    sortedlist=[L[0]]
    for i in range(len(L)-1):
        if L[i]>sortedlist[i-1]:
            sortedlist.append(L[i])
        else:
            sortedlist.insert(i-1,L[i])
        return sortedlist
List=[4,8,7,9,8,3]
print(ins_sort(List))