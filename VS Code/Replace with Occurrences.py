from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    groups = defaultdict(list)
    for i, val in enumerate(b):
        groups[val].append(i)
    possible = True
    a = [0] * n
    label = 1

    for k, indices in groups.items():
        if len(indices) % k != 0:
            possible = False
            break
        for i in range(0, len(indices), k):
            for idx in indices[i:i+k]:
                a[idx] = label
            label += 1
    if not possible:
        print(-1)
    else:
        print(*a)
