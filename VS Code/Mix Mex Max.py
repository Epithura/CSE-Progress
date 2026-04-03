def is_possible_good_array(a):
    if any(a[i]==0 for i in range(len(a))):
        return "NO"
    L=[]
    for i in range(len(a)):
        if a[i]!=-1 and a[i] not in L:
            L.append(a[i])
        if len(L)>1:
            return "NO"
    else:
        return "YES"
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    Final.append(is_possible_good_array(L))
for ans in Final:
    print(ans)