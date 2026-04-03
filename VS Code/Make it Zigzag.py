def Make_it_Zigzag(L):
    arr=L[:]
    Max=arr[0]
    i=0
    Steps=0
    while i<len(arr)-1:
        if Max<L[i]:
            Max=L[i]
        if i%2!=0:
            if Max<=arr[i+1]:
                Steps+=arr[i+1]-Max+1
                arr[i]=Max
                arr[i+1]=Max-1
        else:
            if arr[i]>=arr[i+1]:
                if Max==arr[i]:
                    Steps+=1
                    arr[i]-=1
                else:
                    arr[i+1]=Max
        i+=1
    return Steps
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    Final.append(Make_it_Zigzag(L))
for ans in Final:
    print(ans)