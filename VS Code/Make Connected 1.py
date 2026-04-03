def can_paint(grid):
    """
    grid: list of strings (each string is a row of '.' and '#')
    returns "YES" or "NO"
    """
    n = len(grid)

    # Check for 3 consecutive blacks horizontally
    for r in range(n):
        if "###" in grid[r]:
            return "NO"

    # Check for 3 consecutive blacks vertically
    for c in range(n):
        col = "".join(grid[r][c] for r in range(n))
        if "###" in col:
            return "NO"

    return "YES"
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    M=[]
    for j in range(n):
        S=str(input(""))
        M.append(S)
    Final.append(can_paint(M))
for ans in Final:
    print(ans)