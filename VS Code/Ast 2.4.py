N=int(input())                                   
N1=int(input())                                
N2=int(input())
if N1/10<=9.9 and N2/10<=9.9 and 1<N<=10:                               
    if N1%10<N and N2%10<N and N1//10<N and N2//10<N:
        rem1=N1%N
        rem2=N2%N
        rem0=(rem1+rem2)%N
        carry=(rem1+rem2)//N
        if ((N1//10+N2//10)+carry)<N:
            result=((N1//10+N2//10)+carry)*10+rem0
            print(result,end='')
        if ((N1//10+N2//10)+carry)>=N:
            result=(((N1//10+N2//10)+carry)//N)*100+(((N1//10+N2//10)+carry)%N)*10+rem0
            print(result,end='')
    else:
        print("INVALID INPUT",end='')
else:
    print("INVALID INPUT",end='')
