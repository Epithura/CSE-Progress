def Deck(n,arr):
    k=len(arr)
    if k>=n:
        return "-"*n
    D={0:0,1:0,2:0}
    for i in range(k):
        D[arr[i]]+=1
    Sleft="-"*D[0]
    Sright="-"*D[1]
    Question="?"*D[2]
    if len(Sleft)+len(Sright)+2*len(Question)<n:
        Left=Sleft+Question
        Right=Question+Sright
        Known="+"*max(n-len(Left)-len(Right),0)
        return Left+Known+Right
    else:
        M="?"*(n-len(Sright)-len(Sleft))
        return Sleft+M+Sright
t=int(input(""))
for i in range(t):
    n,k=map(int,input().split())
    string=str(input(""))
    nums=[int(ch) for ch in string]
    print(Deck(n,nums))