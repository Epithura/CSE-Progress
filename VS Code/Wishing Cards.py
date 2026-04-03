def Wishing_Cards(n,k,a):
    dp=[-1]*n
    dp[0]=min(a[0],k)
    sum=dp[0]
    k0=k
    k-=min(a[0],k) 
    KsConsumed=[0]*(k0+1) #Returns the max profit when you consume that much Ks
    KsConsumed[min(a[0],k)]=
    for i in range(1,n):
        if sum+dp[i-1]*(n-i)>=max(sum+min(a[i],k)*(n-i),min(a[i],k0)*(n-i)):
            dp[i]=dp[i-1]
            sum+=dp[i]
        else:
            if sum+min(a[i],k)*(n-i)>=min(a[i],k0)*(n-i):
                dp[i]=min(a[i],k)
                sum+=min(a[i],k)
                k-=min(a[i],k)
            else:
                dp[i]=min(a[i],k0)
                k=k0-min(a[i],k0)
                sum=dp[i]
    return sum
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    print(Wishing_Cards(n,k,a))