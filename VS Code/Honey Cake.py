from collections import defaultdict
def pf(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    if n > 1:
        factors.append(n)
    return factors
w,h,d=map(int,input().split())
n=int(input(""))
if (w*h*d)%n:
    print(-1)
else:
    vol=(w*h*d)//n
    L=pf(vol)
    A=pf(w)
    B=pf(h)
    C=pf(d)
    D=defaultdict(int)
    for i in range(len(L)):
        D[L[i]]+=1
    a=1
    b=1
    c=1
    for i in range(len(A)):
        if D[A[i]]>0:
            D[A[i]]-=1
            a*=A[i]
    for i in range(len(B)):
        if D[B[i]]>0:
            D[B[i]]-=1
            b*=B[i]
    for i in range(len(C)):
        if D[C[i]]>0:
            D[C[i]]-=1
            c*=C[i]
    print(w//a-1,h//b-1,d//c-1)