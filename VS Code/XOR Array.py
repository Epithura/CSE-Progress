def XORArray(n,l,r):
    P=[0]*(n+1)
    for i in range(1,n+1):
        if i==r:
            P[i]=P[l-1]
        else:
            P[i]=i
    a=[P[i]^P[i-1] for i in range(1,n+1)]
    return a
t=int(input(""))
for i in range(t):
    n,k,l=map(int,input().split())
    print(*XORArray(n,k,l))