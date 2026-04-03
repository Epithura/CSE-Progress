import math as meth
a=int(input("Enter a"))
b=int(input("Enter b"))
x=1
while True:
  if x%a==0 and x%b==0:
    break
  else:x=x+1
print(x, "is the LCM of", a, "and", b)
