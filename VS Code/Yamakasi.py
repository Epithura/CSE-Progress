def Yamakasi(Arr,s,x):
    NewArr=[s]
    diff=s
    for j in range(len(Arr)):
        diff=diff-Arr[j]
        NewArr.append(diff)
    NewArr2 = list(reversed(NewArr))
    Dic = {}
    Count = {}
    Arr.insert(0,"a")
    for k in reversed(range(len(NewArr))):
        val = NewArr[k]
        Count[val] = Count.get(val, 0) + 1

        target = s + val
        suffix = NewArr2[len(NewArr) - 1 - k:]

        if target in suffix and Arr[suffix.index(target):k]!=[] and max(Arr[suffix.index(target):k])==x:
            idx = suffix.index(target)
            Dic[idx] = Dic.get(idx, 0) + Count[val]
    L=list(Dic.values())
    sum=1
    for values in L:
        sum+=values
    return sum

x=int(input(""))
final=[]
for i in range(x):
    n,s,x=map(int,input().split())
    L=list(map(int,input().split()))
    final.append(Yamakasi(L,s,x))
for ans in final:
    print(ans)