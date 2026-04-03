from collections import deque,defaultdict
def MST(adj,start=1):
    Vis=set()
    Parent={}
    q=deque([start])
    Vis.add(start)
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in Vis:
                Vis.add(v)
                Parent[v]=u
                q.append(v)
    Edges=[]
    for v,u in Parent.items():
        Edges.append([u,v])
    return Edges
def Rae_Taylor(arr):
    P=[arr[0]]
    S=deque([arr[-1]])
    for i in range(1,len(arr)):
        P.append(min(P[-1],arr[i]))
        S.appendleft(max(S[0],arr[-1-i]))
    for i in range(1,len(arr)):
        if P[i-1]>S[i]:
            return 0
    D=defaultdict(list)
    for i in range(1,len(arr)):
        if P[i-1]<arr[i]:
            D[arr[i]].append(P[i-1])
            D[P[i-1]].append(arr[i])
        if S[i]>arr[i]:
            D[arr[i]].append(S[i])
            D[S[i]].append(arr[i])
        D[S[i]].append(P[i-1])
        D[P[i-1]].append(S[i])
    return MST(D)
t=int(input(""))
for i in range(t):
    n=int(input(""))
    p=list(map(int,input().split()))
    Ans=Rae_Taylor(p)
    if not Ans:
        print("NO")
    else:
        print("YES")
        for i in range(len(Ans)):
            print(*Ans[i])