from collections import defaultdict,deque
mod=10**9+7

def compute_L_iterative(D,Leafs,n):
    L=[0]*(n+1)
    stack=[(1,0)]
    visited=[0]*(n+1)
    while stack:
        i,state=stack.pop()
        if state==0:
            stack.append((i,1))
            for j in D[i]:
                if not visited[j]:
                    stack.append((j,0))
        else:
            visited[i]=1
            for j in D[i]:
                L[i]=(L[i]+L[j]+2)%mod
    return L

def compute_depths(D,n):
    depth=[-1]*(n+1)
    q=deque([0])
    depth[0]=0
    while q:
        i=q.popleft()
        for j in D[i]:
            depth[j]=depth[i]+1
            q.append(j)
    return depth

t=int(input())
for _ in range(t):
    n=int(input())
    D=defaultdict(list)
    D[0].append(1)
    Leafs=[0]*(n+1)
    for i in range(n):
        a,b=map(int,input().split())
        if not(a or b):
            Leafs[i+1]=1
        if a:
            D[i+1].append(a)
        if b:
            D[i+1].append(b)
    L=compute_L_iterative(D,Leafs,n)
    q=deque([0])
    while q:
        i=q.popleft()
        for j in D[i]:
            L[j]=(L[j]+L[i])%mod
            q.append(j)
    H=compute_depths(D,n)
    for i in range(1,n+1):
        L[i]=(L[i]+H[i])%mod
    print(*L[1:n+1])