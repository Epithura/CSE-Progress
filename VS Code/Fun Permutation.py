t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    m=max(L)
    ans=[]
    for j in L:
        ans.append(m-j+1)
    print(*ans)