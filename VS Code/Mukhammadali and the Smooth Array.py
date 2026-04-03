class FenwickMax:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)
    def update(self, i, val):
        while i <= self.n:
            if val > self.tree[i]:
                self.tree[i] = val
            else:
                pass
            i += i & -i
    def query(self, i):
        res = 0
        while i > 0:
            if self.tree[i] > res:
                res = self.tree[i]
            i -= i & -i
        return res
def min_cost_no_drops(a, c):
    n = len(a)
    total_cost = sum(c)
    vals = sorted(set(a))
    rank = {v: i+1 for i,v in enumerate(vals)}  
    fenw = FenwickMax(len(vals))
    best = 0
    for i in range(n):
        r = rank[a[i]]
        best_prefix = fenw.query(r)    
        dp = best_prefix + c[i]
        fenw.update(r, dp)
        if dp > best:
            best = dp
    return total_cost - best
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    a=list(map(int,input().split()))
    c=list(map(int,input().split()))
    Final.append(min_cost_no_drops(a,c))
for ans in Final:
    print(ans)