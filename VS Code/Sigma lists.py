x=int(input(""))
L=[]
for i in range(x):
    L.append(int(input("")))
def sum(n):
    if n==1:
        return L[0]
    else:
        return sum(n-1)+L[n-1]
print(sum(len(L)))