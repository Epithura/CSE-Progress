def ops(a):
    if not a:
        return 0
    cur=a[0]
    ops=0
    for x in a[1:]:
        if x>=cur:
            cur=x
        else:
            ops+=1
    return ops
t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    print(ops(L))