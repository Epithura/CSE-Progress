MOD = 998244353
MAXN = 200_000  # maximum possible n

# --------------------------
# Precompute factorials and inverse factorials
# --------------------------
fact = [1] * (MAXN + 1)
inv_fact = [1] * (MAXN + 1)

for i in range(1, MAXN + 1):
    fact[i] = fact[i - 1] * i % MOD

inv_fact[MAXN] = pow(fact[MAXN], MOD - 2, MOD)
for i in range(MAXN - 1, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

# --------------------------
# Combinations in O(1)
# --------------------------
def C(n, k):
    if k < 0 or k > n: 
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

# --------------------------
# Grid Counting function
# --------------------------
def Grid_Counting(arr):
    n = len(arr)
    
    # Basic validation
    if arr[0] < 2:
        return 0
    Sigma = 0
    for i in range(n):
        if arr[i] > max(n - 2 * i, 0):
            return 0
        Sigma += arr[i]
    if Sigma != n:
        return 0

    # Main computation
    Ways = 1
    Sigma = 0
    
    if n % 2 == 0:
        for i in range(n // 2, 0, -1):
            Ways = Ways * C(n - 2 * (i - 1) - Sigma, arr[i - 1]) % MOD
            Sigma += arr[i - 1]
        Ways = Ways * C(n - 2 - Sigma, arr[0] - 2) % MOD
    else:
        for i in range(n // 2, 0, -1):
            Ways = Ways * C(n - 2 * (i - 1) - Sigma, arr[i - 1]) % MOD
            Sigma += arr[i - 1]
        Ways = Ways * C(n - 2 - Sigma, arr[0] - 2) % MOD

    return Ways

# --------------------------
# Input & Output
# --------------------------
t = int(input())
Final = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    Final.append(Grid_Counting(arr))

for ans in Final:
    print(ans)