def make_good_min_ops(a):
    n = len(a)
    if n <= 1:
        return 0, a[:] 
    m = (n + 1) // 2
    U = [0]*m
    for k in range(m):
        pos = 2*k
        u = a[pos]
        if pos-1 >= 0: u = min(u, a[pos-1])
        if pos+1 < n:  u = min(u, a[pos+1])
        U[k] = u
    b = U[:]  
    for k in range(m-1):
        c = a[2*k+1]                 
        surplus = b[k] + b[k+1] - c
        if surplus > 0:
            take = min(b[k+1], surplus)  
            b[k+1] -= take
            surplus -= take
            if surplus > 0:
                b[k] -= surplus
    orig_odd_sum = sum(a[2*k] for k in range(m))
    final_odd_sum = sum(b)
    ops = orig_odd_sum - final_odd_sum
    final = a[:]
    for k in range(m):
        final[2*k] = b[k]
    return ops
t=int(input(""))
Final=[]
for i in range(t):
    n=map(int,input().split())
    arr=list(map(int,input().split()))
    Final.append(make_good_min_ops(arr))
for ans in Final:
    print(ans)