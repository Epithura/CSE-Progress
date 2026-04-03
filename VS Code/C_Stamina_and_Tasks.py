t=int(input(""))
for _ in range(t):
    n=int(input(""))
    P=[]
    C=[]
    for i in range(n):
        c,p=map(int,input("").split())
        P.append(1-p/100)
        C.append(c)
    dp=[0]*(n+1)
    for i in range(n):
        dp[-i-2]=max(dp[-i-1],dp[-i-1]*P[-i-1]+C[-i-1])
    print(dp[0])