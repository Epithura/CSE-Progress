import math
def T(x):return x*(x+1)//2
t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    ans=1
    for l in range(k):
        tl=T(l)
        if tl>m:break
        rem=m-tl
        u=(math.isqrt(1+8*rem)-1)//2
        if u>n-k:u=n-k
        if l+u+1>ans:ans=l+u+1
    print(ans)
