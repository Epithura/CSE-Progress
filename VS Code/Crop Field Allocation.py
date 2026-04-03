def LargestSquarein(mat):
    if not mat or not mat[0]:
        return 0, (-1, -1)
    
    n, m = len(mat), len(mat[0])
    Z = [[0] * m for _ in range(n)]
    Maximum = 0
    SubOrigin = (-1, -1)
    
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                if i == 0 or j == 0:
                    Z[i][j] = 1
                else:
                    Z[i][j] = min(Z[i-1][j], Z[i][j-1], Z[i-1][j-1]) + 1
                
                if Z[i][j] > Maximum:
                    Maximum = Z[i][j]
                    SubOrigin = (i - Maximum + 1, j - Maximum + 1)
    
    return Maximum, SubOrigin
ROW,COL=map(int, input().split())
def read_input():
    mat = []
    k=0
    
    while k< ROW :
        row = list(map(int, input().split()))
        mat.append(row)
        k=k+1
    return mat
mat = read_input()
Maximum, SubOrigin = LargestSquarein(mat)
print(Maximum)
print(SubOrigin[0], SubOrigin[1],end="")