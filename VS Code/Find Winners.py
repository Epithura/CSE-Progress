L=[]
m=int(input(""))
n=int(input(""))
for i in range(m):
    M=[]
    for j in range(n):
        k=int(input(""))
        M.append(k)
    L.append(M)
def find_winners(List):
    W=[]
    for i in range(m):
        q=max(List[i])
        Wi=List[i].index(q)
        W.append(Wi)
    return W
print(find_winners(L))

