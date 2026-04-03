t=int(input(""))
for i in range(t):
    n=int(input(""))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    maxk=[max(-a[0],b[0])]
    mink=[min(-a[0],b[0])]
    for i in range(1,n):
        k1=maxk[-1]-a[i]
        k2=b[i]-maxk[-1]
        k3=mink[-1]-a[i]
        k4=b[i]-mink[-1]
        maxk.append(max(k1,k2,k3,k4))
        mink.append(min(k1,k2,k3,k4))
    print(max(maxk[-1],mink[-1]))