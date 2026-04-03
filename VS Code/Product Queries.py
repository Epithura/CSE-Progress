def f(a):
    n=len(a)
    a=set(a)
    has1=1 in a
    a=[x for x in a if x<=n]
    INF=float("inf")
    dp=[INF]*(n+1)
    dp[1]=0
    for x in a:
        for m in range(x,n+1,x):
            if dp[m//x]!=INF:
                dp[m]=min(dp[m],dp[m//x]+1)
    res=[]
    for i in range(1,n+1):
        if i==1:
            res.append(1 if has1 else -1)
        elif dp[i]==INF:
            res.append(-1)
        else:
            res.append(dp[i])
    return res
t=int(input(""))
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    Ans=f(a)
    print(*Ans)