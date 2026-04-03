t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=[0]*n
    L[-1]=1
    k=n
    if n%2==0:
        for i in range(n-2,-1,-2):
            L[i]=i
            L[i-1]=i+1
        L[0]=n
        print(*L)
    else:
        for i in range(1,n-1,2):
            L[i]=i+2
            L[i+1]=i+1
        L[0]=n-1
        L[-1]=1
        print(*L)