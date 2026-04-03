t=int(input(""))
for _ in range(t):
    n=int(input(""))
    a=list(map(int,input("").split()))
    D={}
    for i in range(1,n+1):
        D[i]=0
    count=0
    C=[]
    for i in range(n):
        if D[i+1]==0:
            count+=1
            D[a[i]]=1
            C.append(count)
        else:
            D[a[i]]=1
            C.append(count)
    print(max(C))