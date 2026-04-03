import math
class SparseTable:
    def __init__(self, arr):
        self.n = len(arr)
        self.LOG = int(math.log2(self.n)) + 1
        self.arr = arr
        self.min_table = [[0] * self.LOG for _ in range(self.n)]
        self.max_table = [[0] * self.LOG for _ in range(self.n)]
        self.build()
    def build(self):
        for i in range(self.n):
            self.min_table[i][0] = self.arr[i]
            self.max_table[i][0] = self.arr[i]
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.min_table[i][j] = min(self.min_table[i][j - 1],
                                           self.min_table[i + (1 << (j - 1))][j - 1])

                self.max_table[i][j] = max(self.max_table[i][j - 1],
                                           self.max_table[i + (1 << (j - 1))][j - 1])
                i += 1
            j += 1
    def query_min(self, L, R):
        length = R - L + 1
        k = int(math.log2(length))
        return min(self.min_table[L][k],
                   self.min_table[R - (1 << k) + 1][k])
    def query_max(self, L, R):
        length = R - L + 1
        k = int(math.log2(length))
        return max(self.max_table[L][k],
                   self.max_table[R - (1 << k) + 1][k])
def Monopati1(top, bot):
    arr=top+bot
    st=SparseTable(arr)
    n=len(top)
    L=set()
    for i in range(n):
        l=min(st.query_min(0,i),st.query_min(n+i,2*n-1))
        r=max(st.query_max(0,i),st.query_max(n+i,2*n-1))
        L.add((l,r))
    Final=list(L)
    print(Final)
    L_inter=max(a for a,b in Final)
    R_inter=min(b for a,b in Final)
    if (L_inter,R_inter) in Final:
        return L_inter*(2*n-R_inter+1)
    else:
        S1=[]
        S2=[]
        for i in range(len(Final)):
            if Final[i][0]==L_inter:
                S1.append(Final[i][1])
            if Final[i][1]==R_inter:
                S2.append(Final[i][0])
        Intervals=[(L_inter,min(S1)),(max(S2),R_inter)]
        return L_inter*(2*n-Intervals[0][1]+1)+(Intervals[0][1]-R_inter)*Intervals[1][0]
def Monopati2(top, bot):
    n = len(top)
    N = 2 * n
    pref_min_top = [0] * n
    pref_max_top = [0] * n
    pref_min_top[0] = pref_max_top[0] = top[0]
    for i in range(1, n):
        pref_min_top[i] = min(pref_min_top[i - 1], top[i])
        pref_max_top[i] = max(pref_max_top[i - 1], top[i])
    suff_min_bot = [0] * n
    suff_max_bot = [0] * n
    suff_min_bot[-1] = suff_max_bot[-1] = bot[-1]
    for i in range(n - 2, -1, -1):
        suff_min_bot[i] = min(suff_min_bot[i + 1], bot[i])
        suff_max_bot[i] = max(suff_max_bot[i + 1], bot[i])
    INF = 10**9
    minR_at_L = [INF] * (N + 2)
    for k in range(n):
        Lk = min(pref_min_top[k], suff_min_bot[k])
        Rk = max(pref_max_top[k], suff_max_bot[k])
        if Rk < minR_at_L[Lk]:
            minR_at_L[Lk] = Rk
    bestR = [INF] * (N + 3)
    cur = INF
    for l in range(N, 0, -1):
        if minR_at_L[l] < cur:
            cur = minR_at_L[l]
        bestR[l] = cur
    total = 0
    for l in range(1, N + 1):
        br = bestR[l]
        if br == INF:
            continue
        r0 = br if br > l else l
        if r0 <= N:
            total += (N - r0 + 1)
    return total
def compare_solutions(test_cases):
    all_match = True
    for idx, (row1, row2) in enumerate(test_cases, 1):
        out1 = Monopati1(row1, row2)
        out2 = Monopati2(row1, row2)
        if out1 != out2:
            all_match = False
            print(f"Mismatch in test case {idx}:")
            print(f"Row1: {row1}")
            print(f"Row2: {row2}")
            print(f"def1 output: {out1}")
            print(f"def2 output: {out2}")
            print("------")
    if all_match:
        print("All outputs match!")
import random
# Function to generate random test cases
def generate_test_cases(num_cases, n_min=2, n_max=2*10**5):
    test_cases = []
    for _ in range(num_cases):
        n = random.randint(n_min, n_max)
        row1 = [random.randint(1, 2*n) for _ in range(n)]
        row2 = [random.randint(1, 2*n) for _ in range(n)]
        test_cases.append((row1, row2))
    return test_cases
test_cases = generate_test_cases(1000, n_min=2, n_max=2000)  # smaller n for demo
compare_solutions(test_cases)