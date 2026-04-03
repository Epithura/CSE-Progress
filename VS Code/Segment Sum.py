l,r,k=map(int,input().split())
sum=0
for i in range(l,r+1):
    I=str(i)
    if len(set(I))<=k:
        sum+=i
print(sum)