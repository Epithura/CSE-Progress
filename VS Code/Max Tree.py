from collections import defaultdict, deque
def inv(p):
    n=len(p)
    q=[0]*n
    for i in range(n):
        q[p[i]-1]=i+1
    return q
def Kahn(L):
    adj=defaultdict(list)
    indegree=defaultdict(int)
    nodes=set()
    for u,v in L:
        adj[u].append(v)
        indegree[v]+=1
        nodes.add(u)
        nodes.add(v)
    q=deque([x for x in nodes if indegree[x]==0])
    topo=[]
    while q:
        x=q.popleft()
        topo.append(x)
        for y in adj[x]:
            indegree[y]-=1
            if indegree[y]==0:
                q.append(y)
    if len(topo)!=len(nodes):
        return None
    return topo
def Max_Tree(Arr):
    Dirt=[]
    for i in range(len(Arr)):
        if Arr[i][2]>Arr[i][3]:
            Dirt.append([Arr[i][1],Arr[i][0]])
        else:
            Dirt.append([Arr[i][0],Arr[i][1]])
    return inv(Kahn(Dirt))
t=int(input(""))
for i in range(t):
    n=int(input(""))
    Arr=[]
    for j in range(n-1):
        L=list(map(int,input().split()))
        Arr.append(L)
    print(*Max_Tree(Arr))