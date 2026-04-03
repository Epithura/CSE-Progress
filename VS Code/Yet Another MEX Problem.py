from collections import defaultdict
t=int(input(""))
for _ in range(t):
    n,k=map(int,input().split())
    L=list(map(int,input().split()))
    a=L[:]
    a=list(set(a))
    a.sort()
    i=0
    mex=-1
    while i<len(a):
        if a[i]!=i:
            mex=i
            break
        i+=1
    if mex==-1:
        mex=len(a)
    D=defaultdict(int)
    waste=0
    for i in range(len(L)):
        if L[i]<mex:
            if not D[L[i]]:
                D[L[i]]=1
            else:
                waste+=1
        else:
            waste+=1
    print(min(k-1,mex,n-waste))