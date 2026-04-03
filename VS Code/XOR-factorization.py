n=int(input(""))
alpha=n
y=0
L=[]
for i in range(n.bit_count()):
    n&=(n-1)
    res=n|y
    L.append(res)
    y=n^alpha
print(L)