def Villagers(arr):
    arr.sort()
    count=0
    for i in range(len(arr)):
        if i%2==0:
            count+=arr[-1-i]
    return count
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    List=list(map(int,input().split()))
    Final.append(Villagers(List))
for ans in Final:
    print(ans)