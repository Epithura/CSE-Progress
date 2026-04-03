t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    indices = [i + 1 for i, ch in enumerate(s) if ch == '0']
    
    print(len(indices))
    if indices:
        print(*indices)
