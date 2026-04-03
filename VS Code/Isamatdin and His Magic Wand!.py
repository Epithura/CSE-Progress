q=int(input(""))
for i in range(q):
    n=int(input(""))
    L=list(map(int,input().split()))
    R0=False
    R1=False
    for j in L:
        if j%2==0:
            R0=True
        else:
            R1=True
    print(*(sorted(L) if R1 and R0 else L))