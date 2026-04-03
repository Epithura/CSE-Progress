def max_peaks(arr, k):
    n = len(arr)
    count = 0
    i = 0

    window_sum = sum(arr[0:k])
    while i <= n - k:
        if window_sum == 0:
            count += 1
            i += k + 1
            if i <= n - k:
                window_sum = sum(arr[i:i + k])
        else:
            window_sum -= arr[i]
            if i + k < n:
                window_sum += arr[i + k]
            i += 1
    return count
t=int(input(""))
Final=[]
for i in range(t):
    n,k=map(int,input().split())
    L=list(map(int,input().split()))
    Final.append(max_peaks(L,k))
for ans in Final:
    print(ans)