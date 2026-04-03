"""
List=[1,2,3,4,5,6,7,8,9]
List.remove(5)
List.pop(4)
del List[4]      #methods of removing element from list
Dict={"Alpha":1,"Beta":2,"Gamma":3}
print(Dict["Gamma"])
print(List)
import string
def RemovePunc(Text):
    return " ".join(char for char in Text if char not in string.punctuation)
x=input("")
L=tuple(x.split())
y=RemovePunc(L)
print(y)
"""
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
    return A
z=int(input("")) #length of l and r for nth test case
L=[]
K=[]
Z=[]
for j in range(z):
    a,b = map(int,input("").split())
    L.append(a)
    K.append(b)
Z.append(len_longest_subseq(L,K))
print(Z)