def Nez(d,h):
    if h==1:
        return 2*d
    low,high=0,d-1
    ans=None
    while low<=high:
        lam=(low+high)//2
        k=lam+1
        q=d//k
        r=d-q*k
        S =r*(q+1)**2+(k-r)*(q**2)
        if d-2*h+S<2*lam:
            ans=lam
            high=lam-1
        else:
            low=lam+1
    return ans+d
t=int(input(""))
for i in range(t):
    d,h=map(int,input().split())
    d,h=h,d
    print(Nez(d,h))