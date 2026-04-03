import sys
input = sys.stdin.readline
flush = sys.stdout.flush
def query_original(l, r):
    print(f"1 {l} {r}")
    flush()
    return int(input())
def query_modified(l, r):
    print(f"2 {l} {r}")
    flush()
    return int(input())
def find_incremented_range(n):
    total_p = query_original(1, n)
    total_a = query_modified(1, n)
    length = total_a - total_p 
    if length == 0:
        return None
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        sum_p = query_original(1, mid)
        sum_a = query_modified(1, mid)
        diff = sum_a - sum_p
        if diff >= 1:
            right = mid
        else:
            left = mid + 1
    l = left
    r = l + length - 1
    return l, r
t = int(input())
for _ in range(t):
    n = int(input())
    l, r = find_incremented_range(n)
    print(f"! {l} {r}")
    flush()
