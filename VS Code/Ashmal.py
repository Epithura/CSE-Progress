def Ashmal(a,b):
    a1=b+a
    a2=a+b
    return min(a1, a2)
t=int(input(""))
for _ in range(t):
    n=int(input(""))
    L=list(map(str,input().split()))
    Ans=L[0]
    for i in range(1,len(L)):
        Ans=Ashmal(Ans,L[i])
    print(Ans)