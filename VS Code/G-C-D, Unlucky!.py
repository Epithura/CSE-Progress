import math
def GCD_Unlucky(p,s,n):
    Alpha=math.gcd(p[0],s[0])
    for i in range(n):
        if math.gcd(p[i],s[i])!=Alpha or (i+1<n and math.gcd(p[i],s[i+1])!=Alpha):
            return "NO"
    if len(s)==len(p)==1 and p[0]!=s[0]:
        return "NO"
    for i in range(n-1):
        if p[i]%p[i+1]!=0 or s[i+1]%s[i]!=0:
            return "NO"
    if math.lcm(p[0],s[0])!=p[0] or math.lcm(p[-1],s[-1])!=s[-1]:
        return "NO"
    return "YES"
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    p=list(map(int,input().split()))
    s=list(map(int,input().split()))
    Final.append(GCD_Unlucky(p,s,n))
for ans in Final:
    print(ans)