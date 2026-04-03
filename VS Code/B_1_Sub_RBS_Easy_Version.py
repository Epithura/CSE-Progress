t=int(input(""))
for _ in range(t):
    n=int(input(""))
    s=str(input(""))
    a=n//2
    L=[n//2-1]
    S=[n//2]
    for i in range(1,n):
        if s[i]=="(":
            L.append(L[-1]-1)
            S.append(S[-1])
        else:
            L.append(L[-1])
            S.append(S[-1]-1)
    P=[]
    for i in range(n):
        if s[i]==")":
            if L[i]>1:
                P.append(2*(S[i]))
    print(max(P) if P else -1)