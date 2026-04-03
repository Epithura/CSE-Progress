"""
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
"""
def longest_decreasing_subsequence(seq):
    n = len(seq)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if seq[j] > seq[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    idx = dp.index(max_len)
    lds = []
    while idx != -1:
        lds.append(seq[idx])
        idx = prev[idx]
    
    return lds[::-1]

def len_longest_subseq(L, K):
    if not L:
        return 0

    baseline = L[0]
    M = [baseline]

    for i in range(1, len(L)):
        # Safely choose a[i] in [L[i], K[i]] that is ≥ current baseline
        if baseline <= K[i]:
            # Choose the max between baseline and L[i], but not more than K[i]
            chosen = max(baseline, L[i])
            # Clamp to K[i] just in case
            chosen = min(chosen, K[i])
            M.append(chosen)
            baseline = chosen
        else:
            # If no valid value can maintain non-decreasing order
            M.append(K[i])
            baseline = K[i]

    return len(longest_decreasing_subsequence(M))

# Main input loop
x = int(input())
Sigma = []

for _ in range(x):
    z = int(input())
    L = []
    K = []

    for _ in range(z):
        a, b = map(int, input().split())
        L.append(a)
        K.append(b)

    Z = []
    for k in range(1, z + 1):
        Z.append(len_longest_subseq(L[:k], K[:k]))

    Sigma.append(Z)

# Print the output
for res in Sigma:
    print(*res)
