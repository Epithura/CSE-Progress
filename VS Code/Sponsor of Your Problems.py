def f(a,b):
    A=[k for k in str(a)]
    B=[k for k in str(b)]
    count=0
    for i in range(len(A)):
        if A[i]==B[i]:
            count+=1
    return count
def diff_by_prefix(a, b, digits):
    a_str = str(a)[:digits]
    b_str = str(b)[:digits]
    result = []

    for i in range(1, digits + 1):
        prefix_a = int(a_str[:i])
        prefix_b = int(b_str[:i])
        result.append(prefix_a - prefix_b)
    return result
t=int(input(""))
L=[]
R=[]
for i in range(t):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)
Z=[]
for j in range(t):
    l=L[j]
    r=R[j]
    L1=[int(k) for k in str(l)]
    diff=r-l
    Q=[int(k) for k in str(diff)]
    if diff==0:
        Z.append(2*len(L1))
    elif Q[0]==1:
        O=diff_by_prefix(r,l,len(L1)-len(Q)+1)
        Z.append(2*O.count(0)+O.count(1))
    else:
        O=diff_by_prefix(r,l,len(L1)-len(Q))
        Z.append(2*O.count(0)+O.count(1))
for i in range(len(Z)):
    print(Z[i])
