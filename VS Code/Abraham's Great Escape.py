def Escape(n,k):
    if n==2:
        if n==2:
            if k==1:
                return('UD\nRL')
            elif k==2:
                return('UU\nRL')
            elif k==3:
                return('NO')
            else:
                return('UU\nUU')
    if k>4*n-4:
        return "NO"
    matrix = [['0' for _ in range(n)] for _ in range(n)]
    if n >= 3:
        mid = n // 2
        matrix[1][mid] = 'R'
        if mid + 1 < n - 1:
            matrix[1][mid + 1] = 'L'
        for i in range(1, n - 1):
            if i != mid and i != mid + 1:
                if i < mid:
                    matrix[1][i] = 'R'
                else:
                    matrix[1][i] = 'L'

    for i in range(2, n - 1):
        for j in range(1, n - 1):
            matrix[i][j] = 'U'
    def set_edge(i, j, outward):
        if i == 0:
            matrix[i][j] = 'U' if outward else 'D'
        elif i == n - 1:
            matrix[i][j] = 'D' if outward else 'U'
        elif j == 0:
            matrix[i][j] = 'L' if outward else 'R'
        elif j == n - 1:
            matrix[i][j] = 'R' if outward else 'L'

    edges = []
    for j in range(n):
        edges.append((0, j))
    for i in range(1, n):
        edges.append((i, n - 1))
    for j in range(n - 2, -1, -1):
        edges.append((n - 1, j))
    for i in range(n - 2, 0, -1):
        edges.append((i, 0))
    edges = list(dict.fromkeys(edges))

    total_edges = len(edges)
    k = min(k, total_edges)
    for idx, (i, j) in enumerate(edges):
        set_edge(i, j, outward=(idx < k))

    return matrix

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n==2:
        if Escape(2,k)!="NO":
            print("YES")
            print(Escape(2,k))
    else:
        A=Escape(n,k)
        if A=="NO":
            print("NO")
        else:
            print("YES")
            for row in A:
                print(*row)