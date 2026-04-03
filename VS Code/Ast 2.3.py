Inputs=["X","O","-1"]
for i in range (9):
    L=[]
    a=input("")
    L.append(a)
for q in range (0,9):
    if L[q] not in Inputs:
        print("INVALID INPUT")
    elif L.count("X")!=L.count("O") or L.count("X")!=(L.count("O")+1):
        print("INVALID INPUT")
    else:
        while z<=2:
            XWins=(all(L[z+3*k] == "X" for k in range(3)) or all(L[3*z+k] == "X" for k in range(3)) or all(L[4*k] == "X" for k in range(3)) or all(L[2+2*k] == "X" for k in range(3)))
            OWins=(all(L[z+3*k] == "O" for k in range(3)) or all(L[3*z+k] == "O" for k in range(3)) or all(L[4*k] == "O" for k in range(3)) or all(L[2+2*k] == "O" for k in range(3)))
            if XWins or OWins == True:
                print("OK")
                break
            else:
                print("INVALID INPUT")
                
