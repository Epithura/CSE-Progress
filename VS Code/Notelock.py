def Notelock(s,k):
    count=0
    if s[0]==1:
        count+=1
    for i in range(1,len(s)):
        if s[i]==1:
            if max(s[max(i-k+1,0):i])==0:
                count+=1
    return count
t=int(input(""))
Final=[]
for i in range(t):
    n,k=map(int,input().split())
    s=str(input(""))
    L=list(int(char) for char in s)
    Final.append(Notelock(L,k))
for ans in Final:
    print(ans)
