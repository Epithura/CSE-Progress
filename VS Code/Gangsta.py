def f_sum_of_substrings(s):
    n = len(s)
    total = 0

    # For each position r in the string, compute f(s[l..r]) for all l <= r
    for i in range(n):
        c0 = 0
        c1 = 0
        for j in range(i, n):
            if s[j] == '0':
                c0 += 1
            else:
                c1 += 1
            total += max(c0, c1)

    return total
# Driver code
t = int(input())
L = []
for _ in range(t):
    n = int(input())
    string = input().strip()
    L.append(f_sum_of_substrings(string))

for ans in L:
    print(ans)