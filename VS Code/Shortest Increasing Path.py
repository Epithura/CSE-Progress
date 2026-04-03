t=int(input(""))
for i in range(t):
    x,y=map(int,input().split())
    if y==x or y==1 or x==0 or (x==y+1 and y!=0):
        print(-1)
    elif y==0:
        print(1)
    elif x<y:
        print(2)
    else:
        print(3)