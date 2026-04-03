t=int(input(""))
for i in range(t):
    n=int(input(""))
    L=list(map(int,input().split()))
    S=set(L)
    if 0 in S:
        print(2*len(S)-2)
    else:
        print(2*len(S)-1)