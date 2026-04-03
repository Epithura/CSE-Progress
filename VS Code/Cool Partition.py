from collections import defaultdict
def Cool_Partition(arr):
    count=0
    i=0
    j=0
    s=set()
    Dic=defaultdict(bool)
    Dic[arr[0]]=False
    while i<len(arr):
        j=i
        while Dic and i<len(arr):
            s.add(arr[i])
            Dic[arr[i]]=False
            del Dic[arr[i]]
            i+=1
        if not Dic:
            count+=1
        Dic={}
        for k in s:
            Dic[k]=False
        s.clear()
        if i==j:
            i+=1
    return count
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    arr=list(map(int,input().split()))
    Final.append(Cool_Partition(arr))
for ans in Final:
    print(ans)