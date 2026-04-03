t=int(input(""))
for i in range(t):
    R0,X,D,n=map(int,input().split())
    s=str(input(""))
    R=R0
    count=0
    for j in range(n):
        if s[j]=="1":
            R-=D
            count+=1
        elif s[j]=="2" and R<X:
            R-=D
            count+=1
    print(count)