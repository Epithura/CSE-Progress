q=int(input(""))
for i in range(q):
    n=int(input(""))
    s,t=map(str,input().split())
    print("YES" if sorted(s)==sorted(t) else "NO")