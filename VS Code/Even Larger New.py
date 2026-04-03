def Fixer(a):
    n=len(a)
    b=a[:]
    for i in range(n-1):
        if i%2==0:
            if b[i]>b[i+1]:
                b[i]=b[i+1]
        else:
            if b[i+1]>b[i]:
                b[i+1]=b[i]
    for i in range(n-2):
        if i%2==0:
            if b[i+1]<b[i]+b[i+2]:
                if b[i]>b[i+2]:
                    reduce_bi2=min(b[i+2],b[i]+b[i+2]-b[i+1])
                    b[i+2]-=reduce_bi2
                    reduce_bi=max(0,(b[i]+b[i+2]-b[i+1])-reduce_bi2)
                    b[i]-=reduce_bi
                else:
                    b[i+2]-=b[i+2]+b[i]-b[i+1]
    count=0
    for i in range(n):
        count+=a[i]-b[i]
    return count
t=int(input(""))
L=[]
for i in range(t):
    n=int(input(""))
    L.append(Fixer(list(map(int,input().split()))))
for ans in L:
    print(ans)