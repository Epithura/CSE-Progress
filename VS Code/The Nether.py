import heapq
t=int(input())
for i in range(t):
    n=int(input())
    L=[i+1 for i in range(n)]
    HEAP=[]
    heapq.heapify(HEAP)
    for i in range(n):
        print(f"? {i+1} {n} {' '.join(str(char) for char in L)}",flush=True)
        response=int(input())
        heapq.heappush(HEAP,(-response,i+1))
    Max,Start=heapq.heappop(HEAP)
    Path=[Start]
    while HEAP:
        a=heapq.heappop(HEAP)
        print(f"? {Start} {len(Path)+1} {' '.join(str(char) for char in Path)} {a[1]}",flush=True)
        response=int(input())
        if response==len(Path)+1:
            Path.append(a[1])
    print(f"! {len(Path)} {' '.join(str(char) for char in Path)}",flush=True)