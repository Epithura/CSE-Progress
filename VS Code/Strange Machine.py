def Strange_Machine(s,arr):
    All_A=all(s[i]=="A" for i in range(len(s)))
    if All_A:
        return arr
    else:
        L=[]
        for i in range(len(arr)):
            num=arr[i]
            count=0
            sec=0
            while num!=0:
                if s[count]=="A":
                    num-=1
                    count+=1
                    sec+=1
                elif s[count]=="B":
                    num=num//2
                    count+=1
                    sec+=1
                if count==len(s):
                    count=0
            L.append(sec)
        return L
t=int(input(""))
Final=[]
for i in range(t):
    n,q=map(int,input().split())
    s=str(input(""))
    arr=list(map(int,input().split()))
    Final.append(Strange_Machine(s,arr))
for ans in Final:
    for res in ans:
        print(res)