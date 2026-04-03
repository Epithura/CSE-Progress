from collections import defaultdict
def Symmetrical_Polygons(arr):
    if len(arr) < 3:
        return 0  
    D = defaultdict(int)
    for x in arr:
        D[x] += 1
    L = []
    for key in D.keys():
        L += [key] * ((D[key] // 2) * 2)
    Sigma = sum(L)
    leftover = [key for key in D.keys() if D[key] % 2 != 0]
    leftover.sort(reverse=True)
    prevlen=len(L)
    if len(leftover)==1:
        if leftover[0]<Sigma:
            L.append(leftover[0])
    else:
        for i in range(len(leftover)-1):
            if leftover[i]<Sigma+leftover[i+1]:
                L.append(leftover[i])
                L.append(leftover[i+1])
                break
    if prevlen==len(L):
        for key in leftover: 
            if key < Sigma: 
                L.append(key) 
                break
    if len(L) < 3:
        return 0 
    return sum(L)
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    arr=list(map(int,input().split()))
    Final.append(Symmetrical_Polygons(arr))
for ans in Final:
    print(ans)