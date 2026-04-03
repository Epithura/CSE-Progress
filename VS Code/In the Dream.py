def In_the_Dream(a,b,c,d):
    if min(a,b)>=(max(a,b)-2)/2 and (min(d-b,c-a)>=(max(c-a,d-b)-2)/2):
        return "YES"
    return "NO"
t=int(input(""))
Final=[]
for i in range(t):
    a,b,c,d=map(int,input().split())
    Final.append(In_the_Dream(a,b,c,d))
for ans in Final:
    print(ans)