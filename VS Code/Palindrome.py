n=int(input(""))
digits=[int(digit) for digit in str(n)]
if len(digits)%2==0:
    Palindrome=all(digits[i]==digits[len(digits)-i-1] for i in range(0,int(len(digits)/2)))
    if Palindrome==True:
        print("True")
    else:print("False")
else:
    Palindrome=all(digits[i]==digits[len(digits)-i-1] for i in range(0,int(len(digits)/2)))
    if Palindrome==True:
        print("True")
    else:print("False")
