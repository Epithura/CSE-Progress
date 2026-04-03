import heapq
from collections import defaultdict
from functools import lru_cache
def Binary_Search(Arr,t):
    high=len(Arr)-1
    low=0
    while high>=low:
        mid=(high+low)//2
        if Arr[mid]<t:
            low=mid+1
        elif Arr[mid]>t:
            high=mid-1
        else:
            return mid
    return -1
def Max_Tree(Arr):
    D=defaultdict(list)
    for i in range(len(Arr)):
        u=Arr[i][0]
        v=Arr[i][1]
        x=Arr[i][2]
        y=Arr[i][3]
        if x>y:
            D[u].append(v)
        else:
            D[v].append(u)
    @lru_cache(maxsize=None)
    def expand(node):
        if node not in D:
            return set()
        res = set(D[node])
        for child in D[node]:
            res |= expand(child)
        return res

    L = list(D.keys())
    L.sort()
    for k in L:
        D[k] = list(expand(k))
    PList=[]
    for k in L:
        PList.append((-len(D[k]),k))
    heapq.heapify(PList)
    edges=len(Arr)
    s=1
    m=edges+1
    Permutation=[0]*m
    while PList:
        A=heapq.heappop(PList)
        Permutation[A[1]-1]=m
        m-=1
    m=edges+1
    for i in range(m):
        if Permutation[i]==0:
            Permutation[i]=s
            s+=1
    return Permutation
t=int(input())
for i in range(t):
    n=int(input())
    Arr=[]
    for j in range(n-1):
        L=list(map(int,input().split()))
        Arr.append(L)
    print(*Max_Tree(Arr))