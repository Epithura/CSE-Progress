import heapq
def Pos_Set(arr,k,x):
    arr=sorted(set(arr))
    L=[]
    for i in range(1,len(arr)):
        heapq.heappush(L,(-(arr[i]-arr[i-1])//2,(arr[i]+arr[i-1])//2))
    Ans=[]
    l,r,m=0,x,0
    a=heapq.heappop(L) if L else None
    while m<k:
        if a:
            edge=max(arr[0]-l,r-arr[-1],-a[0])
            if edge==arr[0]-l:
                Ans.append(l);l+=1
            elif edge==r-arr[-1]:
                Ans.append(r);r-=1
            else:
                Ans.append(a[1])
                heapq.heappush(L,(-a[0]+1,a[1]+1))
                heapq.heappush(L,(-a[0]+1,a[1]-1))
                a=heapq.heappop(L) if L else None
        else:
            edge=max(arr[0]-l,r-arr[-1])
            if edge==arr[0]-l:
                Ans.append(l);l+=1
            else:
                Ans.append(r);r-=1
        m+=1
    Ans.sort()
    return Ans
q=int(input(""))
Final=[]
for i in range(q):
    n,k,x=map(int,input().split())
    L=list(map(int,input().split()))
    L=list(set(L))
    Final.append(Pos_Set(L,k,x))
for ans in Final:
    print(*ans)