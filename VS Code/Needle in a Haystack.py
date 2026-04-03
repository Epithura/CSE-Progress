from collections import defaultdict,deque
def Hide(s,t):
    D=defaultdict(int)
    for i in range(len(s)):
        D[s[i]]+=1
    for i in range(len(t)):
        D[t[i]]-=1
        if D[t[i]]<0:
            return "Impossible"
    t0=deque(list(t))
    Lex=deque([])
    Alph={'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    L=list(Alph.keys())
    for i in range(len(L)):
        while D[L[i]]:
            Lex.append(L[i])
            D[L[i]]-=1
    Final=[]
    while Lex and t0:
        if Alph[Lex[0]]<Alph[t0[0]]:
            Q=Lex.popleft()
            Final.append(Q)
        elif Alph[Lex[0]]>=Alph[t0[0]]:
            Q=t0.popleft()
            Final.append(Q)
    if t0:
        Final.extend(t0)
    if Lex:
        Final.extend(Lex)
    Fin="".join(Final)
    return Fin
T=int(input(""))
for _ in range(T):
    t=str(input(""))
    s=str(input(""))
    print(Hide(s,t))