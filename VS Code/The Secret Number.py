t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=[]
    k=1
    while 1+10**k<=n:
        if not n%(1+10**k):
            L.append(n//(1+10**k))
        k+=1
    if L:
        print(len(L))
        L.sort()
        print(*L)
    else:
        print(0)