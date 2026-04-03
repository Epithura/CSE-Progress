import bisect
from collections import defaultdict 
t=int(input(""))
for i in range(t):
    n,m,k=map(int,input().split())
    A=list(map(int,input().split())) #robots
    B=list(map(int,input().split())) #spikes
    s=str(input())
    B.sort()
    for i in range(n):
        lam=bisect.bisect_right(B,A[i])-1
        if lam>=0:
            left=B[lam]-A[i]
        else:
            left=float('-inf')
        beta=bisect.bisect_left(B,A[i])
        if beta<m:
            right=B[beta]-A[i]
        else:
            right=float('inf')
        A[i]=(left,right)
    L=[]
    Q={"L":-1,"R":1}
    for i in range(k):
        if not L:
            L.append(Q[s[i]])
        else:
            L.append(L[-1]+Q[s[i]])
    D=defaultdict(lambda: 10**9+1)
    for i in range(k):
        D[L[i]]=min(D[L[i]],i+1)
    Fin=[]
    for i in range(n):
        if min(D[A[i][0]],D[A[i][1]])<10**9+1:
            Fin.append(min(D[A[i][0]],D[A[i][1]]))
    Dick=defaultdict(int)
    for i in range(len(Fin)):
        Dick[Fin[i]]+=1
    Ans=[n]*k
    for i in range(k):
        if i>0:
            Ans[i]=Ans[i-1]-Dick[i+1]
        else:
            Ans[i]=n-Dick[i+1]
    print(*Ans)