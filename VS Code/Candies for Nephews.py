t=int(input(""))
for i in range(t):
    n=int(input(""))
    if n%3==0:
        print(0)
    else:
        print(3-n%3)