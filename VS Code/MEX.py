from collections import Counter

def binary_search(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return m
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

def compute_MEX(arr):
    i = 0
    while binary_search(arr, i) != -1:
        i += 1
    return i
Final1=[]
t = int(input())
for _ in range(t):
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    mex = compute_MEX(L)
    freq = Counter(L)
    cover = [0] * (n + 2)
    for j in range(mex + 1):
        l_j = freq.get(j, 0)      
        r_j = n - j               
        if l_j <= r_j:
            cover[l_j]   += 1
            cover[r_j+1] -= 1
    for k in range(1, n+1):
        cover[k] += cover[k-1]
    res = []
    for k in range(n+1):
        res.append(cover[k] if cover[k] > 0 else 1)
    Final1.append(res)
for ans in Final1:
    print(*ans)