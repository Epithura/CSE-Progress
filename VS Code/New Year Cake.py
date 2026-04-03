def max_layers(a,b,sw):
    size=1
    layers=0
    wt=sw
    while True:
        if wt:
            if a<size:
                break
            a-=size
        else:
            if b<size:
                break
            b-=size
        layers+=1
        size*=2
        wt=not wt
    return layers
t=int(input(""))
for _ in range(t):
    a,b=map(int,input().split())
    ans=max(max_layers(a, b, True),max_layers(a, b, False))
    print(ans)