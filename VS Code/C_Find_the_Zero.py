t=int(input(""))
for _ in range(t):
    n=int(input(""))
    x=0
    q=1
    while x!=1 and q<n:
        print(f"? {2*q+1} {2*q+2}")
        x=int(input(""))
        if x==1:
            print(f"! {2*q+1}")
        else:
            q+=1
    if x!=1:
        print(f"? {1} {3}")
        x=int(input(""))
        if x==1:
            print(f"! {1}")
        else:
            print(f"? {1} {4}")
            x=int(input(""))
            if x==1:
                print(f"! {1}")
            else:
                print(f"! {2}")