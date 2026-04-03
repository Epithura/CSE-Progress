def Cakes(arr, m):
    arr.sort(reverse=True)  
    n=len(arr)
    k=min(n,m)
    total=0
    for j in range(k):
        total+=arr[j]*(m-j)
    return total
t=int(input(""))
for i in range(t):
    n,m=map(int,input().split())
    Arr=list(map(int,input().split()))
    print(Cakes(Arr,m))