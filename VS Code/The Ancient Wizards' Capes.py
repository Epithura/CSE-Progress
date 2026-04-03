def Ways(a):
    n = len(a)
    c = [0] * n
    for i in range(1, n):
        c[i] = a[i] - a[i-1] + 1
    def valid_with_b1(b1):
        b = [0] * n
        b[0] = b1
        for i in range(1, n):
            b[i] = c[i] - b[i-1]
            if b[i] not in (0, 1):
                return False

        S = sum(b)
        if a[0] != b1 + (n - S): 
            return False
        if a[-1] != S + (1 - b[-1]):
            return False
        return True
    count = 0
    if valid_with_b1(0):
        count += 1
    if valid_with_b1(1):
        count += 1
    return count
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    Final.append(Ways(L))
for ans in Final:
    print(ans)