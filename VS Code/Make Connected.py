def Connected(M):
    Blacks=[]
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j]=="#":
                Blacks.append((i,j))
    if not Blacks or len(Blacks)==1:
        return "YES"
    for i in range(len(Blacks)):
        for j in range(i+1,len(Blacks)):
            a=abs(Blacks[i][0]-Blacks[j][0])
            b=abs(Blacks[i][1]-Blacks[j][1])
            if not (a==b or a==b-1 or a==b+1):
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
    Final.append(Connected(M))
for ans in Final:
    print(ans)