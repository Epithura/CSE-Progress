h, k = 0, 0
x = input("")

# Validate cipher (should have exactly 4 unique positive digits and be an integer)
if not x.isdigit() or len(x) != 4 or len(set(x)) != 4 or '0' in x:
    print("INVALID INPUT")
else:
    digits = [int(digit) for digit in x]
    y = sum(digits)

    North = y // digits[0]
    South = y // digits[1]
    East = y // digits[2]
    West = y // digits[3]

    Directions = [North, South, East, West]
    entries = []
    for i in range(12):
        a = input("")
        if not a.lstrip('-').isdigit(): 
            print("INVALID INPUT")
            break
        entries.append(int(a))
    else:
        for n in range(0, 12, 2):
            if entries[n] not in Directions:
                print("INVALID INPUT")
                break
            else:
                if entries[n] == North:
                    k += entries[n + 1]
                elif entries[n] == South:
                    k -= entries[n + 1]
                elif entries[n] == East:
                    h += entries[n + 1]
                elif entries[n] == West:
                    h -= entries[n + 1]
        else:
            print(f"({h}, {k})",end="")
