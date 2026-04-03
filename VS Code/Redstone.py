def Redstone(arr):
    if len(arr) != len(set(arr)):
        return("Yes")
    else:
        return("No")
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    List=list(map(int,input().split()))
    Final.append(Redstone(List))
for ans in Final:
    print(ans)