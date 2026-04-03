import random

def sol(n, k, a, b):
    a0 = a1 = float('-inf')
    t0 = t1 = 0
    for i in range(n):
        t1 = max(a[i] + b[i] + t0, t1 + a[i])
        t0 += a[i]
        a0 = max(a0, t0)
        a1 = max(a1, t1)
        if t0 < 0: t0 = 0
        if t1 < 0: t1 = 0
    return a1 if k & 1 else a0


from collections import deque
def Annoying_Game(arr,b,k):
    def Kadane(arr):
        B=float("-inf")
        C=0
        start=end=0
        Temp=0
        for i, x in enumerate(arr):
            C+=x
            if C>B:
                B=C
                start=Temp
                end=i
            if C<0:
                C=0
                Temp=i+1
        return B,start,end
    if k%2==0:
        A=Kadane(arr)
        return A[0]
    else:
        P=[0]
        S=deque([0])
        for i in range(1,len(arr)):
            P.append(max(P[-1]+arr[i-1],0))
            S.appendleft(max(S[0]+arr[-i],0))
        L=[]
        for i in range(len(arr)):
            L.append(arr[i]+b[i]+max(0,P[i])+max(0,S[i]))
        return max(L)


# -----------------------------------------------------
# COUNTEREXAMPLE FINDER
# -----------------------------------------------------

def find_counterexample(trials=100000):
    for _ in range(trials):
        n = random.randint(1, 8)
        k = random.randint(0, 3)

        a = [random.randint(-10, 10) for _ in range(n)]
        b = [random.randint(0, 20) for _ in range(n)]

        out1 = sol(n, k, a[:], b[:])
        out2 = Annoying_Game(a[:], b[:], k)

        if out1 != out2:
            print("FOUND COUNTEREXAMPLE:")
            print("n =", n, "k =", k)
            print("a =", a)
            print("b =", b)
            print("sol =", out1)
            print("Annoying_Game =", out2)
            return

    print("No counterexample found in", trials, "cases")
find_counterexample()