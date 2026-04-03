def Chicken_Jockey(arr):
    b=[arr[0],arr[0]+arr[1]-1]
    for i in range(2,len(arr)):
        b.append(min(b[-1]+arr[i]-1,b[-2]+arr[i-1]+max(0,arr[i]-len(b))))
    return b[-1]
t=int(input(""))
F=[]
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    F.append(Chicken_Jockey(L))
for ans in F:
    print(ans)