n=int(input(""))
def fib(n):
        if n==1:
            return 0
        elif n==2:
            return 1
        else:
            x=fib(n-1)+fib(n-2)
            return x
L=[]
for i in range(0,n):
     L.append(fib(n-i))
print(L)

