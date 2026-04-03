import numpy as np
def longest_decreasing_subsequence(seq):
    n = len(seq)
    dp = [1] * n  # dp[i] = length of longest decreasing subsequence ending at i
    prev = [-1] * n  # to reconstruct the sequence

    for i in range(n):
        for j in range(i):
            if seq[j] > seq[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Find the index of the max value in dp
    max_len = max(dp)
    idx = dp.index(max_len)

    # Reconstruct the subsequence
    lds = []
    while idx != -1:
        lds.append(seq[idx])
        idx = prev[idx]
    
    return lds[::-1]
def len_longest_subseq(L,K):
    baseline=L[0]
    M=[baseline]
    for i in range(1,len(L)):
        if baseline>=L[i] and baseline<=K[i]:
            M.append(baseline)
        elif baseline<L[i]:
            M.append(L[i])
            baseline=L[i]
    if len(L)==1:
        return 1
    A=[]
    i=0
    while i<len(L)-1:
        count=0
        for j in range(i+1,len(L)):
            if K[j]>=L[i]:
                count+=1
        A.append(count)
        i=i+1
    A.append(0)
    return max(len(longest_decreasing_subsequence(A)),len(M))
x=int(input(""))
Sigma=[]
for i in range(x):
    z=int(input("")) #length of l and r for nth test case
    L=[]
    K=[]
    Z=[]
    for j in range(z):
        a,b = map(int,input("").split())
        L.append(a)
        K.append(b)
        Z.append(len_longest_subseq(L,K))
    Z1=np.array(Z)
    Sigma.append(Z1)
for h in range(x):
    print(*(Sigma[h]))
