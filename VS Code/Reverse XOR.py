def check_x_exists(n):
    s = bin(n)[2:].rstrip('0')
    L = len(s)
    if L == 0:
        return "YES"
    if L % 2 == 0:
        return "YES" if s == s[::-1] else "NO"
    else:
        mid = L // 2
        outer_symmetric = s[:mid] == s[-1:mid:-1]
        middle_zero = s[mid] == '0'
        return "YES" if outer_symmetric and middle_zero else "NO"
t=int(input(""))
for i in range(t):
    n=int(input(""))
    print(check_x_exists(n))