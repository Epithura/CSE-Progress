t=int(input())
for _ in range(t):
    n=int(input())
    M=1<<n
    ans=[]
    for k in range(n,0,-1):
        ans.append((1<<k)-1)
    for x in range(3,M,2):
        if (x+1)&x:
            ans.append(x)
    for x in range(0,M,2):
        ans.append(x)
    print(*ans)