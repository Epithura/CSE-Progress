import math as mt
def divineness(n, m):
    if not (n <= m <= (n * (n + 1)) // 2):
        print(-1)
        return 0
    if n==m:
        print(1)
        for i in range(1,n):
            print(i, i+1)
        return 0
    k=mt.floor(mt.sqrt(n*n+n+0.25-2*m)+0.5)
    total=n*(n+1)/2 - k*(k+1)/2
    add_needed = m - total
    min_add = k
    seq = list(range(n, k, -1))
    if add_needed < min_add:
        seq[-1] += (add_needed - min_add)
    print(int(seq[0]))
    prev = seq[0]
    for x in seq[1:]:
        print(int(prev), int(x))
        prev = x
    used = set(seq)   
    for i in range(1, n+1):
        if i not in used:
            print(int(prev), int(i))
            prev = i
    return 0
t=int(input(""))
for i in range(t):
    n,m=map(int,input().split())
    divineness(n,m)