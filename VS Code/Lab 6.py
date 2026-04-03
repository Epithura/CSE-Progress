L=["A ","B ","C ","D ","E ","F ","G ","H ","I ","J ","K ","L ","M ","N ","O ","P ","Q ","R ","S ","T ","U ","V ","W ","X ","Y ","Z "]
n=input("")
if n.isdigit()==False or int(n)<=0 or int(n)>26:
    print("INVALID INPUT")
else:
    for i in range(int(n)+1):
        print(L[i-1]*i)