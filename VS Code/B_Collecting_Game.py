import bisect
def count_leq(a, x):
    return bisect.bisect_right(a, x)
t=int(input(""))
for _ in range(t):
    n=int(input(""))
    a=list(map(int,input("").split()))
    b=a[:]
    b.sort()
    P=[b[0]]
    i=1
    while i<n:
        if b[i]<=P[-1]:
            P[-1]+=b[i]
            i+=1
        else:
            while len(P)!=i:
                P.append(P[-1])
            P.append(b[i]+P[-1])
            i+=1
    while len(P)!=n:
        P.append(P[-1])
    L=[]
    for i in range(n):
        L.append(count_leq(b,P[i]))
    D={}
    for i in range(n):
        D[b[i]]=L[i]
    Ans=[]
    for i in range(n):
        Ans.append(D[a[i]]-1)
    print(*Ans)