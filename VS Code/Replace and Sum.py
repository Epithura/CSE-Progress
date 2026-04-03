t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    Query=[]
    for i in range(q):
        l,r=map(int,input().split())
        Query.append((l,r))
    C=[0]*n
    C[-1]=max(A[-1],B[-1])
    for i in range(n-2,-1,-1):
        C[i]=max(A[i],B[i],C[i+1])
    pref=[0]*(n+1)
    for i in range(n):
        pref[i+1]=pref[i]+C[i]
    ans=[]
    for l,r in Query:
        ans.append(str(pref[r]-pref[l-1]))
    print(" ".join(ans))