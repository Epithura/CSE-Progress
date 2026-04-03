import math

def compute_F(n, k):
    dp = [[0] * (k + 2) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(k + 1):
            dp[i][0] += dp[i - 1][j]
        for j in range(k):
            dp[i][j + 1] += dp[i - 1][j]
    return sum(dp[n][j] for j in range(k + 1))

def expected_max_streak(n):
    total = 0
    prev_F = compute_F(n, 0)
    for k in range(1, n + 1):
        curr_F = compute_F(n, k)
        total += k * (curr_F - prev_F)
        prev_F = curr_F
    return total / (2 ** n)

n = 400
expected = expected_max_streak(n)
log2_n = math.log2(n)
print("Expected Max Streak:", expected)
print("log2(n):", log2_n)
print("Difference:", expected - log2_n)
