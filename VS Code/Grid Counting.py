from math import comb
MOD = 998244353
def Grid_Counting(arr):
    n=len(arr)
    Sigma=0
    n=len(arr)
    if arr[0]<2:
        return 0
    for i in range(n):
        if arr[i]>max(n-2*i,0):
            return 0
        Sigma+=arr[i]
    if Sigma!=n:
        return 0
    if n%2==0:
        Sigma=0
        Ways=1
        for i in range(n//2,1,-1):
            Ways=Ways*comb(n-2*(i-1)-Sigma,arr[i-1])
            Ways=Ways%MOD
            Sigma+=arr[i-1]
        Ways*=comb(n-2-Sigma,arr[0]-2)
        return Ways%MOD
    else:
        Sigma=0
        Ways=1
        for i in range(n//2+1,1,-1):
            Ways=Ways*comb(n-2*(i-1)-Sigma,arr[i-1])
            Ways=Ways%MOD
            Sigma+=arr[i-1]
        Ways*=comb(n-2-Sigma,arr[0]-2)
        return Ways%MOD
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    arr=list(map(int,input().split()))
    Final.append(Grid_Counting(arr))
for ans in Final:
    print(ans)