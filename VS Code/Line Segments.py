import math
def is_polygon_possible_all_combinations(sides):
    n = len(sides)
    for i in range(n):
        other_sides_sum = sum(sides) - sides[i]
        if other_sides_sum < sides[i]:
            return "NO"
    return "YES"

def PDest(px,py,qx,qy,L):
    dist=math.sqrt((px-qx)**2 + (py-qy)**2)
    L.append(dist)
    return is_polygon_possible_all_combinations(L)
t=int(input(""))
X=[]
for i in range(t):
    lenarr=int(input(""))
    px,py,qx,qy=map(int,input().split())
    L = list(map(int, input().split()))
    X.append(PDest(px,py,qx,qy,L))
for i in range(len(X)):
    print(X[i])