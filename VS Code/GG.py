def GG(R, C):
    if R == 1 or C == 1 or (R == 2 and C == 2):
        return "NO"
    return "YES"
t=int(input(""))
Final=[]
for i in range(t):
    R,C=map(int,input().split())
    Final.append(GG(R,C))
for ans in Final:
    print(ans)