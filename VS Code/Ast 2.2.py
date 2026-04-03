list=[]                             
list2=[1,0]                          
for i in range (8):                   
    a=int(input())
    list.append(a)
for e in list:                      
    if e not in list2:
        print('INVALID INPUT',end="")
        exit()
b=list[0:4]                           
c=list[4:8]
finaldigit=[]
carry=0
b.insert(0,0)                           
c.insert(0,0)
for i in range (0,5):
    digit=(b[4-i]+c[4-i]+carry)%2           
    finaldigit.insert(0,digit)
    carry=(b[4-i]+c[4-i]+carry)//2
for i in range (0,5):
    print(finaldigit[i],end="")          