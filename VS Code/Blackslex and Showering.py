t=int(input(""))
for _ in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    P=0
    for i in range(n-1):
        P+=abs(L[i+1]-L[i])
    Res=[P-abs(L[1]-L[0])]
    for i in range(1,n-1):
        Res.append(P-(abs(L[i]-L[i+1])+abs(L[i]-L[i-1]))+abs(L[i-1]-L[i+1]))
    Res.append(P-abs(L[-1]-L[-2]))
    print(min(Res))