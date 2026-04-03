t=int(input(""))
for i in range(t):
    n,k=map(int,input().split())
    s=str(input(""))
    print("Alice" if (k>n//2 or k>=s.count("1")) else "Bob")