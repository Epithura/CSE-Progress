t=int(input(""))
for i in range(t):
    n,rk,ck,rd,cd=map(int,input().split())
    print(max((rd)*(rd>rk),(n-rd)*(rd<rk),(cd)*(cd>ck),(n-cd)*(cd<ck)))
