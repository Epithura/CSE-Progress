def myAtoi(s):
    Lfinal = []
    L2 = []
    L1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    digits = ['1','2','3','4','5','6','7','8','9']  # changed to strings

    L = [ch for ch in s]  # renamed 'String' to 'ch' (Python naming convention)

    while " " in L:
        L.remove(" ")

    for i in range(26):
        if L1[i] in L:
            L2.append(L.index(L1[i]))

    if L2:
        a = min(L2)
        # Delete using slicing instead of looping with del
        L = L[:a]

    if L and L[0] == "+":
        del L[0]

    if L and L[0] == "-":
        del L[0]
        Lfinal.append("-")

    while L and L[0] == "0":
        L.pop(0)

    Lfinal += L  # use += instead of append to avoid nested list
    Str = "".join(Lfinal)
    return Str

# Run it
x = input()
_x_ = myAtoi(x)
print(_x_)
