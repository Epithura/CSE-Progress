def build_permutation_from_s(s: str):
    n = len(s)
    ones = [i for i, ch in enumerate(s) if ch == '1']
    p = [0] * n
    if not ones:
        if n == 1:
            return None
        vals = list(range(1, n + 1))
        for j, pos in enumerate(range(0, n)):
            p[pos] = vals[(j + 1) % n]
        return p
    first = ones[0]
    k = first  
    if k == 1:
        return None
    if k > 0:
        vals = list(range(1, first + 1))  
        pos_list = list(range(0, first))
        for j, pos in enumerate(pos_list):
            p[pos] = vals[(j + 1) % k]
    p[first] = first + 1
    for idx in range(len(ones) - 1):
        prev = ones[idx]
        cur = ones[idx + 1]
        l = prev + 1
        r = cur - 1
        k = r - l + 1
        if k == 1:
            return None
        if k > 0:
            vals = list(range(prev + 2, cur + 1))  
            pos_list = list(range(l, r + 1))
            for j, pos in enumerate(pos_list):
                p[pos] = vals[(j + 1) % k]
        p[cur] = cur + 1
    last = ones[-1]
    l = last + 1
    k = n - l
    if k == 1:
        return None
    if k > 0:
        vals = list(range(last + 2, n + 1))  
        pos_list = list(range(l, n))
        for j, pos in enumerate(pos_list):
            p[pos] = vals[(j + 1) % k]

    return p
t = int(input())
Final = []
for _ in range(t):
    n = int(input())
    s = input()
    res=build_permutation_from_s(s)
    if res is None:
        print("NO")
    else:
        print("YES")
        print(*res)
