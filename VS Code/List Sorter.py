List=[]
k=int(input("ENTER LENGTH OF LIST"))
for j in range(1,k+1):
    q=float(input(f"ENTER ELEMENT {j}"))
    List.append(q)
l=[]
def sortmylist(L):
    for i in range(0,len(L)):
        y=max(L)
        L.remove(y)
        l.append(y)
    return l
print(sortmylist(List))