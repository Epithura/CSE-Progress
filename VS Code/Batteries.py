t=int(input(""))
for m in range(t):
    n=int(input(""))
    used_pairs = set()
    size = 2
    while size <= n:
        for start in range(1, n+1, size):
            end = min(start + size - 1, n)
            block = list(range(start, end+1))
            pairs = []
            for i in range(len(block)):
                for j in range(i+1, len(block)):
                    pair = (block[i], block[j])
                    if pair not in used_pairs:
                        pairs.append(pair)
                        used_pairs.add(pair)
            if pairs:
                for a,b in pairs:
                    print(*[a,b])
                    Omega=int(input(""))
                    if Omega:
                        break
                if Omega:
                    break
            if Omega:
                break
        if Omega:
            break
        size *= 2
    if Omega:
        continue
    else:
        found = False
        for i in range(1,size//2+1):
            for j in range(size//2+1, n+1):
                print(i, j)
                Omega = int(input())
                if Omega:
                    found = True
                    break
            if found:
                break