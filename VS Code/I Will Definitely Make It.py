def Binary_Search(Arr,Target):
    high=len(Arr)-1
    low=0
    while high>=low:
        mid=(high+low)//2
        if Arr[mid]<Target:
            low=mid+1
        elif Arr[mid]>Target:
            high=mid-1
        else:
            return mid
    return -1
def survival(Arr, k):
    time = 1  
    Height = Arr[k-1]
    Arr.sort()
    Pos=Binary_Search(Arr,Height)
    while Height<Arr[-1]:
        if 2*Height-time+1>=Arr[Pos+1]:
            Height=Arr[Pos+1]
            Pos+=1
            time+=Height-Arr[Pos-1]
        else:
            return "NO"
    return "YES"
t=int(input(""))
Final=[]
for i in range(t):
    n,k=map(int,input().split())
    L=list(map(int,input().split()))
    Final.append(survival(L,k))
for ans in Final:
    print(ans)