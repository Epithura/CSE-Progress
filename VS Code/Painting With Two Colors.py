def Checker(n,a,b):
    if (n-b)%2!=0:
        return "NO"
    if a<=b:
        return "YES"
    return "YES" if (n-a)%2==0 else "NO"
t=int(input(""))
Final=[]
for i in range(t):
    n,a,b=map(int,input().split())
    Final.append(Checker(n,a,b))
for ans in Final:
    print(ans)