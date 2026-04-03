Inputs = ["X", "O", "-1"]
L = []

for i in range(9):
    a = input()
    L.append(a)

for q in range(9):
    if L[q] not in Inputs:
        print("INVALID INPUT",end="")
        exit()

if L.count("X") - L.count("O") not in [0, 1]:
    print("INVALID INPUT",end="")
    exit()

for z in range(3):
    XWins = (
        all(L[z + 3 * k] == "X" for k in range(3)) or
        all(L[3 * z + k] == "X" for k in range(3)) or
        all(L[4 * k] == "X" for k in range(3)) or
        all(L[2 + 2 * k] == "X" for k in range(3))
    )
    OWins = (
        all(L[z + 3 * k] == "O" for k in range(3)) or
        all(L[3 * z + k] == "O" for k in range(3)) or
        all(L[4 * k] == "O" for k in range(3)) or
        all(L[2 + 2 * k] == "O" for k in range(3))
    )

    if XWins:
        print("X wins",end="")
        exit()
    elif OWins:
        print("O wins",end="")
        exit()
else:
    print("INVALID INPUT",end="")