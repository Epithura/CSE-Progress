def Gen(arr, x):
    n = len(arr)
    if x[0] == '1' or x[-1] == '1':
        return -1
    groups = []
    i = 0
    while i < n:
        if x[i] == '1':
            j = i
            while j < n and x[j] == '1':
                j += 1
            groups.append((i, j - 1))
            i = j
        else:
            i += 1

    if not groups:
        return []

    if len(groups) > 5:
        return -1
    ops_set = set()

    for L, R in groups:
        seg_min = min(arr[L:R + 1])
        seg_max = max(arr[L:R + 1])
        found = False

        for l in range(0, L):
            for r in range(R + 1, n):
                low = min(arr[l], arr[r])
                high = max(arr[l], arr[r])
                if low < seg_min and seg_max < high:
                    ops_set.add((l + 1, r + 1))
                    found = True
                    break
            if found:
                break

        if not found:
            return -1
    ops = list(ops_set)
    if len(ops) > 5:
        return -1
    return ops
t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    x=str(input(""))
    Res=Gen(L,x)
    if Res!=-1:
        print(len(Res))
        for q in range(len(Res)):
            print(f"{Res[q][0]} {Res[q][1]}")
    else:
        print(-1)