t=int(input(""))
for _ in range(t):
    x,y=map(int,input("").split())
    L=[-1 for i in range(y)]+[1 for i in range(x)]
    a=max(x,y)
    b=min(x,y)
    boxes=a-b
    c=0
    if not boxes:
        print(1)
        print(*L)
        continue
    for i in range(boxes):
        if boxes%(i+1)==0:
            c+=1
    print(c)
    print(*L)