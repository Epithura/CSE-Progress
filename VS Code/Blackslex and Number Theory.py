t=int(input(""))
Final=[]
for _ in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    a=min(L)
    L=[x for x in L if x!=a]
    b=min(L)
    Final.append(max(a,b-a))
for ans in Final:
    print(ans)