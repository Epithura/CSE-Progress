t=int(input(""))
for _ in range(t):
    n=int(input(""))
    L=[int(char) for char in str(n)]
    L[0]-=1
    L.sort()
    steps=0
    s=sum(L)
    while s>=9:
        s-=L.pop()
        steps+=1
    print(steps)