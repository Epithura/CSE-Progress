def Winner(n):
    c0 = (n + 3) // 4
    c1 = (n + 2) // 4
    c2 = (n + 1) // 4
    c3 = n // 4

    pair12 = min(c1, c2)
    pair03 = min(c0, c3)

    total_pairs = pair12 + pair03

    if total_pairs * 2 == n:
        print("Bob")
    else:
        print("Alice")
t = int(input())
inputs = [int(input()) for _ in range(t)]

for n in inputs:
    (Winner(n))
