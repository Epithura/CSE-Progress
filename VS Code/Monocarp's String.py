def find_subarray_to_remove(arr):
    n=len(arr)
    transformed=[-1 if x == "a" else 1 for x in arr]
    total=sum(transformed)
    if total==0:
        return 0
    prefix_sum=0
    mp={0:-1}  
    L=[]
    for i,val in enumerate(transformed):
        prefix_sum+=val
        if (prefix_sum-total) in mp:
            start=mp[prefix_sum-total]+1
            end=i
            L.append(end-start+1) 
        mp[prefix_sum]=i
    return min(L) if min(L)<len(arr) else -1 
t=int(input(""))
for i in range(t):
    n=int(input(""))
    string=str(input(""))
    nums=[ch for ch in string]
    print(find_subarray_to_remove(nums))