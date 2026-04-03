t=int(input(""))
for i in range(t):
    n,k=map(int,input().split())
    s=str(input(""))
    L=list(s)
    Counter=0
    for i in range(len(s)):
        if L[i]=="1":
            Counter=k
        elif Counter>0:
            L[i]="1"
            Counter-=1
    print(L.count("0"))