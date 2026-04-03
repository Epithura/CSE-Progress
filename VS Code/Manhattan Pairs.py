t = int(input())
for j in range(t):
    n = int(input())
    pts = []
    for i in range(1, n+1):
        x, y = map(int, input().split())
        pts.append((x + y, i))
    pts.sort()
    for i in range(n//2):
        _, a = pts[i]
        _, b = pts[-1 - i]
        print(a, b)
