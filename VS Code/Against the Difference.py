from collections import defaultdict
import bisect
def neat(arr):
    n = len(arr)
    pos = defaultdict(list)
    for i, num in enumerate(arr):
        pos[num].append(i)
    dp = [-1] * (n + 1)
    def solve(i):
        if i >= n:
            return 0
        if dp[i] != -1:
            return dp[i]
        best = solve(i + 1)
        x = arr[i]
        indices = pos[x]
        idx = bisect.bisect_left(indices, i)
        if idx + x - 1 < len(indices):
            block_end = indices[idx + x - 1] + 1
            best = max(best, x + solve(block_end))
        dp[i] = best
        return best
    return solve(0)
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    arr=list(map(int,input().split()))
    Final.append(neat(arr))
for ans in Final:
    print(ans)