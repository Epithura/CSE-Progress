def PMinSMax(arr):
    PrefixMin=arr[0]
    SuffixMaxList=[]
    MaxS=arr[-1]
    for i in range(len(arr)):
        if arr[len(arr)-i-1]>=MaxS: 
            MaxS=arr[len(arr)-i-1]
        SuffixMaxList.append(MaxS)
    Max=max(arr)
    Min=min(arr)
    L=[1]
    for i in range(1,len(arr)-1):
        SuffixMax=SuffixMaxList[len(arr)-i-1]
        if arr[i]==Min or arr[i]==Max:
            L.append(1)
        elif arr[i]<=PrefixMin or arr[i]>=SuffixMax:
            L.append(1)
        else:
            L.append(0)
        if arr[i]<=PrefixMin:
            PrefixMin=arr[i]
    L.append(1)
    s=''.join(map(str, L))
    return s
t = int(input())
X = []
for _ in range(t):
    n = int(input())
    L = list(map(int, input().split()))
    X.append(L)

for i in range(len(X)):
    print(PMinSMax(X[i]))