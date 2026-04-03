def maxDistance(s: str, k: int) -> int:
        L=[]
        for i in range(len(s)):
            K=k
            Q=s[0:i]
            if Q.count("N")>Q.count("S"): #making sure North is the minority
                Q=Q.replace("N","_")
                Q=Q.replace("S","N")
                Q=Q.replace("_","S")
            if Q.count("E")>Q.count("W"): #making sure East is the minority
                Q=Q.replace("E","_")
                Q=Q.replace("W","E")
                Q=Q.replace("_","W")
            Q=list(Q)
            j=0
            while K>0 and j<i:
                if Q[j]=="N":
                    Q[j]="S"
                    K=K-1
                    j=j+1
                elif Q[j]=="E":
                    Q[j]="W"
                    K=K-1
                    j=j+1
            L.append(Q.count("W")+Q.count("S")-Q.count("N")-Q.count("E"))
        return max(L)