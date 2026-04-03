x=int(input(""))
def binary(x):
    if x==0:
        return []
    else:
        return binary(int(x/2)) + [x%2]
a=str("")
for i in range(0,len(binary(x))):
    a=str(binary(x)[len(binary(x))-i-1])+a
print(a)