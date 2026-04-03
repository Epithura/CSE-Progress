def max_bonus_points(prices, X):
    prices.sort()
    l, r = 0, len(prices) - 1
    S = 0
    bonus = 0
    order = []
    while l <= r:
        if (S // X) < ((S + prices[r]) // X):
            bonus += prices[r]
            S += prices[r]
            order.append(prices[r])
            r -= 1
        else:
            S += prices[l]
            order.append(prices[l])
            l += 1
    return bonus, order
t=int(input(""))
Final=[]
for i in range(t):
    n,X=map(int,input().split())
    M=list(map(int,input().split()))
    Final.append(max_bonus_points(M,X))
for ans in Final:
    print(ans[0])
    print(*ans[1])