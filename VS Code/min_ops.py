def min_ops(Arr):
    count = 0
    """all_zeros_match = all(row[2] == row[0] for row in Arr)"""
    for a, b, c, d in Arr:
        """
        if all_zeros_match and b > d:
            count += a
        """
        if c > a:
            count += c - a
        if d > b and c>a:
            count += d - b + c - a
        if d > b:
            count += d - b
    return count

t=int(input(""))
Final=[]
for i in range(t):
    n=int(input())
    Arr=[]
    for j in range(n):
        a,b,c,d=map(int,input().split())
        Arr.append([a,b,c,d])
    Final.append(min_ops(Arr))
for ans in Final:
    print(ans)
