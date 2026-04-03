import heapq
def Neos_Escape(arr):
    n = len(arr)
    heap = [(-arr[i], i) for i in range(n)]
    heapq.heapify(heap)
    pressed = [False] * n
    clones = 0
    while heap:
        while heap and pressed[heap[0][1]]:
            heapq.heappop(heap)
        if not heap:
            break
        clones += 1
        _, idx = heapq.heappop(heap)
        pressed[idx] = True
        i = idx - 1
        current_weight = arr[idx]
        while i >= 0 and not pressed[i] and arr[i] <= current_weight:
            pressed[i] = True
            current_weight = arr[i]
            i -= 1
        i = idx + 1
        current_weight = arr[idx]
        while i < n and not pressed[i] and arr[i] <= current_weight:
            pressed[i] = True
            current_weight = arr[i]
            i += 1
    return clones
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    List=list(map(int,input().split()))
    Final.append((Neos_Escape(List)))
for ans in Final:
    print(ans)