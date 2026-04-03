from collections import defaultdict
def Maxim(arr,k):
    arr.sort()
    D=defaultdict(int)
    for i in range(len(arr)):
        D[arr[i]]+=1
    def Adjusted_Binary_Search(num, arr):
        low,high=0,len(arr)-1
        while low<=high:
            mid = (low + high)//2
            if arr[mid]<num and (mid==len(arr)-1 or arr[mid+1]>=num):
                return mid
            elif arr[mid]>=num:
                high=mid-1
            else:
                low=mid+1
        return -1
    lam=1
    prev=1
    while lam<len(arr)+1:
        a=Adjusted_Binary_Search(4*lam,arr)
        if a-D[lam]-D[2*lam]-D[3*lam]+1<=k:
            prev=lam
        lam+=1
    return prev
Final=[]
t=int(input(""))
for i in range(t):
    n,k=map(int,input().split())
    L=list(map(int,input().split()))
    Final.append(Maxim(L,k))
for ans in Final:
    print(ans)