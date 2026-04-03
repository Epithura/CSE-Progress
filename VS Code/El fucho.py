def Matches(n):
    Winners=n
    Losers=0
    count=0
    while not (Winners==Losers==1):
        Current=Winners
        Winners-=Current//2
        Losers+=Current//2
        count+=Current//2
        Save=Losers
        Losers-=Save//2
        count+=Save//2
    return count+1
t=int(input(""))
for i in range(t):
    n=int(input(""))
    print(Matches(n))