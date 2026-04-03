import heapq
t=int(input(""))
for i in range(t):
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    Alice=sum(A)
    Bob=sum(B)
    for i in range(n):
        A[i]=-A[i]
    for i in range(m):
        B[i]=-B[i]
    heapq.heapify(A)
    heapq.heapify(B)
    chance=0
    while Alice>0 and Bob>0:
        if not chance:
            x=-A[0]
            y=-heapq.heappop(B)
            z=max(0,y-x)
            heapq.heappush(B,-z)
            chance=1
            Bob+=z-y
        if chance:
            x=-B[0]
            y=-heapq.heappop(A)
            z=max(0,y-x)
            heapq.heappush(A,-z)
            chance=0
            Alice+=z-y
    if not Alice:
        print("Bob")
    if not Bob:
        print("Alice")