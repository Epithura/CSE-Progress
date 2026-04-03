t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    x=int(input(""))
    if min(L)<=x and max(L)>=x:
        print("YES")
    else:
        print("NO")
