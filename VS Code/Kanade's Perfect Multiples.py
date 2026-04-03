import heapq
from collections import defaultdict
def Kanade(arr,k):
    arr=list(set(arr))
    arr.sort()
    PRIMS=[[arr[0],2]]
    HEAP=[arr[0]]
    Seen=defaultdict(int)
    heapq.heapify(HEAP)
    for i in range(len(arr)):
        a=heapq.heappop(HEAP)
        if a<arr[i]:
            return []
        if a>arr[i]:
            PRIMS.append([arr[i],2])
            heapq.heappush(HEAP,a)
        for N in PRIMS:
            if not Seen[N[0]*N[1]]:
                heapq.heappush(HEAP,N[0]*N[1])
                Seen[N[0]*N[1]]=1
            N[1]+=1
    D=defaultdict(int)
    for i in range(len(arr)):
        D[arr[i]]=1
    for num in PRIMS:
        if not D[(k//num[0])*num[0]]:
            return []
    Fin=[]
    for i in range(len(PRIMS)):
        Fin.append(PRIMS[i][0])
    return Fin
t=int(input(""))
for i in range(t):
    n,k=map(int,input().split())
    L=list(map(int,input().split()))
    ans=Kanade(L,k)
    if not ans:
        print(-1)
    else:
        print(len(ans))
        print(*ans)