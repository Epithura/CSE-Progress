from collections import defaultdict 
def Addition_on_a_Segment(b):
    b.sort()
    n=len(b)
    S=sum(b)
    Z=0
    for x in b:
        if x==0:
            Z+=1
        else:
            break
    return min(n-Z,S-(n-1))
t=int(input(""))
for i in range(t):
    n=int(input(""))
    arr=list(map(int,input().split()))
    print(Addition_on_a_Segment(arr))