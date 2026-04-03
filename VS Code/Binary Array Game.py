t=int(input(""))
for _ in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    c1=0
    c0=0
    while L:
        if L[-1]==0:
            c0+=1
            while L and L[-1]==0:
                L.pop()
        elif L[-1]==1:
            c1+=1
            while L and L[-1]==1:
                L.pop()
    if c1>=c0:
        print("Alice")
    else:
        print("Bob")