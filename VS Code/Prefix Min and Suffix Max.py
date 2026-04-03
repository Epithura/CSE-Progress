def PMinSMax(L):
    n = len(L)
    max_index = L.index(max(L))
    min_index = L.index(min(L))

    prefix_min = [L[0]] * n
    for i in range(1, n):
        prefix_min[i] = min(prefix_min[i - 1], L[i])

    suffix_max = [L[-1]] * n
    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(suffix_max[i + 1], L[i])

    A = []
    for i in range(n):
        # Case A: there is some element before i smaller than L[i] AND
        # some element after i greater than L[i]
        before_smaller = i > 0 and L[i] > prefix_min[i - 1]
        after_greater = i < n - 1 and L[i] < suffix_max[i + 1]

        if before_smaller and after_greater:
            A.append(0)
        elif (max_index < i < min_index) or \
             (i == max_index or i == min_index) or \
             (max_index > i and min_index > i and (i == 0 or all(L[i] < L[k] for k in range(0, i)))) or \
             (max_index < i and min_index < i and (i == n - 1 or all(L[i] > L[k] for k in range(i + 1, n)))):
            A.append(1)
        else:
            A.append(0)
    print(''.join(map(str, A)))

# Input reading
t = int(input())
X = []
for _ in range(t):
    n = int(input())
    L = list(map(int, input().split()))
    X.append(L)

for i in range(len(X)):
    PMinSMax(X[i])
