def solve(A, Q):
    n=len(A)
    def possible(x):
        q=Q[:]
        for i in range(n-1):
            if q[i]>x:
                d=q[i]-x
                q[i]-=d
                q[i+1]+=d*(1<<(A[i]-A[i+1]))
        return q[-1]<=x
    lo,hi=0,max(Q)
    while lo<hi:
        mid=(lo+hi)//2
        if possible(mid):
            hi=mid
        else:
            lo=mid+1
    return lo
t=int(input(""))
for _ in range(t):
    s,m=map(int,input().split())
    L=[]
    pos=0
    while m>0:
        if m&1:
            L.append(pos)
        m>>=1
        pos+=1
    Q=[]
    A=L[::-1]
    while s>0 and L:
        a=2**L[-1]
        num=s//a
        s-=num*a
        L.pop()
        Q.append(num)
    if s!=0:
        print(-1)
    else:
        while len(Q) < len(A):
            Q.append(0)
        print(solve(A,Q))