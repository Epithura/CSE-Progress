from collections import defaultdict,deque
t=int(input(""))
for _ in range(t):
    D=defaultdict(list)
    n=int(input(""))
    for i in range(n-1):
        u,v=map(int,input().split())
        D[u].append(v)
        D[v].append(u)
    height=[-1]*(n+1)
    q=deque([1])
    height[1]=0
    while q:
        u=q.popleft()
        for v in D[u]:
            if height[v]==-1:
                height[v]=height[u]+1
                q.append(v)
    HD=[0]*(max(height)+1)
    for i in range(1,len(height)):
        HD[height[i]]+=1