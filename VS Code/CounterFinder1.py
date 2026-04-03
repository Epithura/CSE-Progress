import random
from collections import deque

# -------------------------------------
# Your Code A (QnR)
# -------------------------------------
def QnR(q, R, k):
    q = sorted(q)
    Q = deque(q)
    R = sorted(R)
    count = 0

    while Q and R:
        if Q[0] + R[-1] + Q[0]*R[-1] <= k:
            Q.popleft()
            R.pop()
            count += 1
        else:
            R.pop()
    return count


# -------------------------------------
# Your Code B (pointer-based)
# -------------------------------------
def QnR_pointer(q, R, k):
    n = len(q)
    a = sorted(q)
    b = sorted(R)
    j = 0
    for i in range(1, n+1):
        if (b[-i] + 1) * a[j] + b[-i] <= k:
            j += 1
            if j == n:
                break
    return j


# -------------------------------------
# STRESS TEST DRIVER
# -------------------------------------
def stress_test():
    while True:
        # change max_n and max_k to make harder tests
        n = random.randint(1, 7)
        k = random.randint(1, 50)

        q = [random.randint(0, 10) for _ in range(n)]
        R = [random.randint(0, 10) for _ in range(n)]

        ans1 = QnR(q, R, k)
        ans2 = QnR_pointer(q, R, k)

        if ans1 != ans2:
            print("❗ DIFFERENCE FOUND")
            print("n =", n, "   k =", k)
            print("q =", q)
            print("r =", R)
            print("QnR =", ans1)
            print("QnR_pointer =", ans2)
            return


# -------------------------------------
# RUN THE TEST
# -------------------------------------
stress_test()