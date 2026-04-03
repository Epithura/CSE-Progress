def Gen(n,k):
    max=int(n*(n-1)/2)
    sum=max
    L=[]
    while sum!=k:
        i=2
        while not sum<k:
            sum-=i-1
            i+=1
        L.append(i-1)
        sum+=i-1