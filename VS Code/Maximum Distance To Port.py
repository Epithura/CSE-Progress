from collections import defaultdict,deque
n,m,k=map(int,input().split())
Types=list(map(int,input().split()))
A=[-1 for i in range(k)]
D=defaultdict(list)
Visited=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    D[a].append(b)
    D[b].append(a)
Queue=deque([(1,0)])
Visited[0]=1
while Queue:
    node,count=Queue.popleft()
    A[Types[node-1]-1]=max(A[Types[node-1]-1],count)
    for neighbour in D[node]:
        if not Visited[neighbour-1]:
            Visited[neighbour-1]=1
            Queue.append((neighbour,count+1))
print(*A)