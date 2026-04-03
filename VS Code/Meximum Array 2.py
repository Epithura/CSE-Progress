from collections import defaultdict
t=int(input(""))
for _ in range(t):
    n,k,q=map(int,input().split())
    L=[set() for zeta in range(n)]
    Q=[-1]*n
    D=defaultdict(int)
    for i in range(q):
        c,l,r=map(int,input().split())
        for j in range(l-1,r):
            L[j].add(c)
            if c==2:
                D[j]+=1
    print(D)
    i=0
    while i<n:
        if not len(L[i]):
            L[i]=0
            i+=1
        elif len(L[i])==1:
            if 1 in L[i]:
                L[i]=k
                i+=1
            elif 2 in L[i]:
                j=i
                if D[j]==1:
                    while j<n and len(L[j])==1 and 2 in L[j] and D[j]==1:
                        L[j]=(j-i)%k
                        j+=1
                    if not i-j:
                        i+=1
                    else:
                        i=j
                if D[j]>=2:
                    while j<n and len(L[j])==1 and 2 in L[j] and D[j]>=2:
                        L[j]=(j-i)%k
                        j+=1
                    if not i-j:
                        i+=1
                    else:
                        i=j
        elif len(L[i])==2:
            L[i]=k+1
            i+=1
    print(*L)