def Range_Operation(a):
    n=len(a)
    a=[0]+a
    P=[0]*(n+1)
    for i in range(1,n+1):
        P[i]=P[i-1]+a[i]
    X=[0]*(n+1)
    Y=[0]*(n+1)
    for r in range(1,n+1):
        X[r]=r*r+r-P[r]
    for l in range(1,n+1):
        Y[l]=l*l-l-P[l-1]
    maxG=0
    bestY=float('inf')
    for r in range(1,n+1):
        bestY=min(bestY,Y[r])
        maxG=max(maxG,X[r]-bestY)
    return P[n]+maxG
t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    print(Range_Operation(L))