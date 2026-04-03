def Add_0_or_K(arr,k):
    max_add=k*k
    check=bool(any(x%2==0 for x in arr))
    if len(arr)==1 and arr[0]==1:
        arr[0]+=max_add
        return arr
    if k%2==0:
        for i in range(len(arr)):
            if arr[i]%(k+1)!=0:
                arr[i]+=k*(arr[i]%(k+1))
        return arr
    else:
        for i in range(len(arr)):
            if arr[i]%2!=0:
                arr[i]+=k
        return arr
t=int(input(""))
Final=[]
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    Final.append(Add_0_or_K(arr,k))
for ans in Final:
    print(*ans)