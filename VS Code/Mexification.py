from collections import defaultdict
def mex(arr):
    s=set(arr)
    n=len(arr)
    for i in range(n+1):
        if i not in s:
            return i
def Mexification(arr,k):
    n=len(arr)
    for _ in range(k):
        M=mex(arr)
        Q=[]
        D=defaultdict(int)
        for i in range(n):
            D[arr[i]]+=1
        for i in range(n):
            other_count=D[arr[i]]
            if arr[i]>M or other_count>1:
                Q.append(M)
            else:
                Q.append(arr[i])
        if Q==arr:
            break
        arr=Q
    return sum(arr)
t=int(input(""))
for i in range(t):
    n,k=map(int,input().split())
    L=list(map(int,input().split()))
    print(Mexification(L,k))