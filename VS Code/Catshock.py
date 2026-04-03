from collections import deque
from collections import defaultdict
def Catshock(nD,n):
    D={}
    Visited=[0]*(n+1)
    Visited[1]=1
    Queue=deque([1])
    while not Visited[n]:
        Curr=Queue.popleft()
        for Neighbour in nD[Curr]:
            if not Visited[Neighbour]:
                Visited[Neighbour]=1
                Queue.append(Neighbour)
                D[Neighbour]=Curr
    Local=n
    path=deque([n])
    while Local!=1:
        path.appendleft(D[Local])
        Local=D[Local]
    Ans=[]
    for i in range(len(path)-1):
        u=path[i]
        nxt=path[i+1]
        for v in nD[u]:
            if v!=nxt:
                Ans.append([2,v])  
                Ans.append([1])     
    print(len(Ans))
    for op in Ans:
        print(*op)
t=int(input(""))
for i in range(t):
    n=int(input(""))
    nD=defaultdict(list)
    for j in range(n-1):
        a,b=map(int,input().split())
        nD[a].append(b)
        nD[b].append(a)
    Catshock(nD,n)