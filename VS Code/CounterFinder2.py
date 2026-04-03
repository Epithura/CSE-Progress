from math import gcd
import random

# ----------------------------------------------------------
# Build GCD sparse table for interval GCD queries
# ----------------------------------------------------------
class GCDSparseTable:
    def __init__(self, arr):
        self.n = len(arr)
        self.LOG = self.n.bit_length()
        self.st = [[0]*self.n for _ in range(self.LOG)]

        for i in range(self.n):
            self.st[0][i] = arr[i]

        j = 1
        while (1 << j) <= self.n:
            i = 0
            while i + (1 << j) <= self.n:
                self.st[j][i] = gcd(self.st[j-1][i],
                                    self.st[j-1][i + (1 << (j-1))])
                i += 1
            j += 1

    def query(self, l, r):
        j = (r - l + 1).bit_length() - 1
        return gcd(self.st[j][l], self.st[j][r - (1 << j) + 1])


# ----------------------------------------------------------
# Your two-pointer greedy code
# ----------------------------------------------------------
def your_code(a):
    n = len(a)
    arr=GCDSparseTable(a)
    b=1
    B=1
    while b<n:
        if gcd(a[b],a[b-1])<gcd(a[B],a[B-1]):
            B=b
        b+=1
    i=0
    j=n-1
    S=arr.query(i,j)
    while i+1<j:
        if arr.query(i+1,j)>arr.query(i,j-1):
            S+=arr.query(i,j-1)
            j-=1
        elif arr.query(i+1,j)<arr.query(i,j-1):
            S+=arr.query(i+1,j)
            i+=1
        else:
            if i<B-1:
                S+=arr.query(i+1,j)
                i+=1
            else:
                S+=arr.query(i,j-1)
                j-=1
    return S


# ----------------------------------------------------------
# Prefix/suffix GCD method
# ----------------------------------------------------------
def prefix_suffix(a):
    n = len(a)
    pre = [0]*n
    end = [0]*n

    pre[0] = a[0]
    for i in range(1, n):
        pre[i] = gcd(pre[i-1], a[i])

    end[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        end[i] = gcd(end[i+1], a[i])

    ans = 0
    for i in range(1, n):
        ans += min(pre[i], end[i])

    return ans


# ----------------------------------------------------------
# Exhaustive tester
# ----------------------------------------------------------
def find_counterexample():

    for _ in range(100000):  # runs fast
        n = random.randint(3, 1000)
        a = [random.randint(1, 20) for _ in range(n)]

        y = your_code(a)
        p = prefix_suffix(a)

        if y != p:
            print("❌ Counterexample found!")
            print("Array:", a)
            print("Your code =", y)
            print("Prefix/Suffix =", p)
            return

    print("No mismatch found (increase search if needed).")


# Run test
find_counterexample()
