from collections import defaultdict
def construct_heights(ranges):
    if not ranges:
        return []
    max_r = max(r for _, r in ranges)
    diff = [0] * (max_r + 2)
    for l, r in ranges:
        diff[l] += 1
        diff[r + 1] -= 1
    height = [0] * (max_r + 1)
    height[0] = diff[0]
    for i in range(1, len(height)):
        height[i] = height[i - 1] + diff[i]
    return height
def MEX_count(arr):
    A=[]
    D=defaultdict(int)
    for i in range(len(arr)):
        D[arr[i]]+=1
    for i in range(max(arr)+2):
        A.append((i,D[i]))
    A.sort(key=lambda x: x[0])
    Wastes=[0]*(A[-1][0]+1)
    for i in range(1,A[-1][0]+1):
        Wastes[-i-1]=Wastes[-i]+A[-i][1]
    Final=[]
    PSum=0
    MEX=0
    for i in range(len(A)):
        if A[MEX][1]==0:
            break
        else:
            MEX+=1
    for i in range(MEX+1):
        if i>0:
            PSum+=A[i-1][1]-1
        Range=(A[i][1],A[i][1]+Wastes[i]+PSum)
        Final.append(Range)
    return construct_heights(Final)
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    Final.append(MEX_count(L))
for ans in Final:
    print(*ans)