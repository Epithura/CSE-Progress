def Not_Alone(a):
    n = len(a)
    if n == 1:
        return 0
    if n == 2:
        return abs(a[0] - a[1])

    # Helper to compute cost for a linear array
    def linear_cost(arr):
        ops = 0
        i = 0
        while i < len(arr) - 1:
            if arr[i] != arr[i + 1]:
                ops += abs(arr[i] - arr[i + 1])
                arr[i + 1] = arr[i]  # match next element
            i += 2  # jump every second element
        return ops

    # Case 1: leave a[0] unchanged
    arr1 = a[:]
    ops1 = linear_cost(arr1)

    # Case 2: force a[0] to match a[-1]
    arr2 = a[:]
    ops2 = abs(arr2[0] - arr2[-1])
    arr2[0] = arr2[-1]
    ops2 += linear_cost(arr2)

    return min(ops1, ops2)
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    arr=list(map(int,input().split()))
    Final.append(Not_Alone(arr))
for ans in Final:
    print(ans)