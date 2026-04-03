def minimal_max(Arr):
    rows, cols = len(Arr), len(Arr[0])
    maximum = max(max(row) for row in Arr)
    L = []
    for i in range(rows):
        for j in range(cols):
            if Arr[i][j] == maximum:
                L.append([i + 1, j + 1])
    if not L:  
        return maximum
    Store = L[:]  
    row = L[0][0]
    col = L[0][1]
    s = set()
    for i in range(len(L)):
        if L[i][0] == row:
            L[i] = False
    for i in range(len(L)):
        if L[i] != False:
            s.add(L[i][1])
    if len(s) <= 1:
        return maximum - 1
    L = Store[:]
    s.clear()
    for i in range(len(L)):
        if L[i][1] == col:
            L[i] = False
    for i in range(len(L)):
        if L[i] != False:
            s.add(L[i][0])
    if len(s) <= 1:
        return maximum - 1
    return maximum
t=int(input(""))
Final=[]
for i in range(t):
    n,m=map(int,input().split())
    A=[]
    for j in range(n):
        L=list(map(int,input().split()))
        A.append(L)
    Final.append(minimal_max(A))
for ans in Final:
    print(ans)