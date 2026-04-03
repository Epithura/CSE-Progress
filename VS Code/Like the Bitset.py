def finder(s, k):
    count = 0
    count1=0
    for char in s:
        if char == '1':
            count += 1
            count1+=1
            if count >= k:
                return "NO"
        else:
            count = 0
    L=[]
    j=0
    i=len(s)-count1
    for char in s:
        if char=="0":
            L.append(count1+1+j)
            j+=1
        else:
            L.append(len(s)-count1-i+1)
            i-=1
    return ["YES",L]
t=int(input(""))
Final=[]
for i in range(t):
    n,k=map(int,input().split())
    s=input("")
    Final.append(finder(s,k))
for ans in Final:
    if type(ans)==list:
        print(ans[0])
        print(*ans[1])
    else:
        print(ans)