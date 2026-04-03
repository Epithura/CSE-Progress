import heapq
def Discount(products, vouchers):
    price = 0
    total_voucher_items = sum(vouchers)
    total_products = len(products)
    products = [-p for p in products]
    heapq.heapify(products)
    heapq.heapify(vouchers)
    used = 0  
    while vouchers:
        a = heapq.heappop(vouchers)  
        used += a
        last = 0
        for _ in range(a):
            if not products:
                break
            last = -heapq.heappop(products)  
            price += last
        if last and (products or total_voucher_items == total_products or used == total_products):
            price -= last
    while products:
        price += -heapq.heappop(products)
    return price
t=int(input(""))
for i in range(t):
    n,k=map(int,input().split())
    Products=list(map(int,input().split()))
    Vouchers=list(map(int,input().split()))
    print(Discount(Products,Vouchers))