t=int(input(""))
for i in range(t):
    n=int(input(""))
    Store=[False for _ in range(2*n)]
    Interval=[0]
    for i in range(1,len(Store)):
        k=len(Interval)+1
        print(f"? {k} {' '.join(str(char+1) for char in Interval)} {i+1}")
        response=int(input(""))
        if response:
            Store[i]=response
        else:
            Interval.append(i)
    L=[]
    for i in range(len(Store)):
        if Store[i]:
            L.append(i)
    for i in range(len(L)):
        k=len(L)+1
        print(f"? {k} {' '.join(str(char+1) for char in L)} {Interval[i]+1}")
        response=int(input(""))
        Store[Interval[i]]=response
    print(f"! {' '.join(str(char) for char in Store)}")