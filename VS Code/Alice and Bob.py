t=int(input(""))
for i in range(t):
    n,a=map(int,input().split())
    L=list(map(int,input().split()))
    if a in L:
        ia=L.index(a)
        c=L.count(a)
        print(a-1 if ia>=len(L)-ia-c+1 else a+1)
    else:
        count=0
        for i in range(len(L)-1):
            if L[i+1]>a:
                count=i+1
                break
        if count>len(L)-count:
            print(a-1)
        else:
            print(a+1)