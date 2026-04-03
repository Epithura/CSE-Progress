from collections import deque
def QnR(q,R,k):
    q.sort()
    Q=deque(q)
    R.sort()
    count=0
    i=0
    while Q and R:
        if Q[0]+R[-1]+Q[0]*R[-1]<=k:
            Q.popleft()
            R.pop()
            count+=1
        else:
            R.pop()
    return count
t=int(input(""))
for i in range(t):
    n,k=map(int,input().split())
    q=list(map(int,input().split()))
    R=list(map(int,input().split()))
    print(QnR(q,R,k))