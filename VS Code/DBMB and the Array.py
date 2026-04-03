t=int(input(""))
for _ in range(t):
    n,s,x=map(int,input().split())
    L=list(map(int,input().split()))
    if sum(L)>s:
        print("NO")
    else:
        print("NO" if (s-sum(L))%x else "YES")