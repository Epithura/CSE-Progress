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
def Monopati(top, bot):
    arr=top+bot
    st=SparseTable(arr)
    n=len(top)
    L=set()
    for i in range(n):
        l=min(st.query_min(0,i),st.query_min(n+i,2*n-1))
        r=max(st.query_max(0,i),st.query_max(n+i,2*n-1))
        L.add((l,r))
    Final=list(L)
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
t=int(input(""))
for i in range(t):
    n=int(input(""))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(Monopati(a,b))