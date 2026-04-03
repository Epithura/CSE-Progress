def Multiple_Construction(n):
    L=[]
    A=[]
    for i in range(n-1):
        L.append(n-i-1)
        A.append(i+1)
    L.append(n)
    A.append(n)
    return L+A
t=int(input(""))
for i in range(t):
    n=int(input(""))
    print(*Multiple_Construction(n))