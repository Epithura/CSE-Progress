def max_carries(n, k):
    t = 0
    while n & 1:
        t += 1
        n >>= 1
    return k * t + k * (k + 1) // 2
t=int(input(""))
for i in range(t):
    n,k=map(int,input().split())
    print(max_carries(n,k))