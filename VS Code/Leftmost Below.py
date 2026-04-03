t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    Min=float("inf")
    Fail=False
    for k in range(len(L)-1):
        if Min>L[k]:
            Min=L[k]
        if L[k+1]>=2*Min:
            print("NO")
            Fail=True
            break
    if not Fail:
        print("YES")