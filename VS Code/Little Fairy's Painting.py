import bisect
t=int(input(""))
for i in range(t):
    n=int(input(""))
    arr=list(map(int,input().split()))
    arr.sort()
    al=len(set(arr))
    idx=bisect.bisect_left(arr,al)
    print(max(al,arr[idx]))