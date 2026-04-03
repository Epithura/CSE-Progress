class Fenwick:
    def __init__(self, n):
        self.n = n
        self.f = [0] * (n + 1)
    def add(self, i, v):
        while i <= self.n:
            self.f[i] += v
            i += i & -i
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.f[i]
            i -= i & -i
        return s

def sum_f_over_substrings(s: str) -> int:
    """
    Returns the value of
      sum_{1 <= l <= r <= n} max(#0s, #1s) in s[l..r]
    in O(n log n) time for len(s)=n.
    """
    n = len(s)
    # 1) S1 = sum_{L=1..n} L*(n-L+1)
    S1 = n * (n + 1) * (n + 2) // 6

    # 2) Build prefix‐balance B: B[k] = (#1 − #0) in s[0..k-1]
    B = [0] * (n + 1)
    for i, ch in enumerate(s, start=1):
        B[i] = B[i-1] + (1 if ch == '1' else -1)

    # 3) Coordinate‐compress the balances into [1..m]
    vals = sorted(set(B))
    comp = {v: i+1 for i, v in enumerate(vals)}
    m = len(vals)

    # 4) Fenwicks for counts and sums of previous B[i]
    bit_cnt = Fenwick(m)
    bit_sum = Fenwick(m)
    # insert B[0]
    bit_cnt.add(comp[B[0]], 1)
    bit_sum.add(comp[B[0]], B[0])

    # 5) S2 = sum_{1<=k<=n} sum_{i<k} |B[k] - B[i]|
    S2 = 0
    for k in range(1, n+1):
        x   = B[k]
        idx = comp[x]

        # # of previous i with B[i] <= x, and their sum
        cnt_le = bit_cnt.sum(idx)
        sum_le = bit_sum.sum(idx)

        # total previous count & sum
        cnt_tot = k       # i from 0..k-1
        sum_tot = bit_sum.sum(m)

        cnt_gt = cnt_tot - cnt_le
        sum_gt = sum_tot - sum_le

        # add |B[k] - B[i]| over all i<k
        S2 += x * cnt_le - sum_le
        S2 += sum_gt - x * cnt_gt

        # insert this B[k]
        bit_cnt.add(idx, 1)
        bit_sum.add(idx, x)

    # 6) final answer = (S1 + S2) // 2
    return (S1 + S2) // 2

t = int(input())
L = []
for _ in range(t):
    n = int(input())
    string = input().strip()
    L.append(sum_f_over_substrings(string))

for ans in L:
    print(ans)