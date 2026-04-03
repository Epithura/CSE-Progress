def Remove_the_Ends(A):
    count = 0
    l, r = 0, len(A) - 1
    while l <= r:
        sump, summ = 0, 0
        i = l
        check = False
        j = r
        while i <= r and sump <= summ:
            if A[i] < 0:
                if not check:
                    j = i
                    check = True
                summ += -A[i]
            else:
                sump += A[i]
            i += 1
        if sump>summ:  
            count += sump
            l = i             
        else:      
            count += summ
            r = j - 1         
    return count
t=int(input(""))
Final=[]
for i in range(t):
    n=int(input(""))
    List=list(map(int,input().split()))
    Final.append(Remove_the_Ends(List))
for ans in Final:
    print(ans)