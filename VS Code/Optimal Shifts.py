def Optimal_Shifts(s):
    L=[]
    for i in range(len(s)):
        if s[i]=="1":
            L.append(i)
    L.append(L[0]+len(s))
    ans=0
    for i in range(len(L)-1):
        ans=max(L[i+1]-L[i]-1,ans)
    return ans
t=int(input(""))
for i in range(t):
    n=int(input(""))
    s=str(input(""))
    print(Optimal_Shifts(s))