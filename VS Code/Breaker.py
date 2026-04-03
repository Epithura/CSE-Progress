def your_code(a, b):
    if a % 2 == 0:
        if b % 2 == 0:
            return int(a * b // 2 + 2)
        else:
            return -1
    else:
        if b % 2 == 0:
            if (b // 2) % 2 == 0:
                return int(a * b // 2 + 2)
            else:
                return -1
        else:
            return a * b + 1

def correct_code(a, b):
    best = -1
    k = 1
    while k * k <= b:
        if b % k == 0:
            val1 = a * k + b // k
            if val1 % 2 == 0:
                best = max(best, val1)
            k2 = b // k
            val2 = a * k2 + b // k2
            if val2 % 2 == 0:
                best = max(best, val2)
        k += 1
    return best

# Search for the smallest failing (a, b)
limit=5000  # you can increase this if needed
s=1
for a in range(s, limit + 1):
    for b in range(s, limit + 1):
        if your_code(a, b) != correct_code(a, b):
            print("Counterexample found!")
            print("a =", a, "b =", b)
            print("Your code gives:", your_code(a, b))
            print("Correct answer:", correct_code(a, b))
            raise SystemExit

print("No counterexample found up to", limit)
