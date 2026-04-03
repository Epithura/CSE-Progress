Inputs = ["X", "O", "-1"]
L = []

# Taking 9 inputs for Tic-Tac-Toe board
for i in range(9):
    a = input()
    L.append(a)

# Validate inputs
for q in range(9):
    if L[q] not in Inputs:
        print("INVALID INPUT", end="")
        exit()

# Validate counts of X and O
if L.count("X") - L.count("O") not in [0, 1]:
    print("INVALID INPUT", end="")
    exit()

# Define winning combinations
winrows = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

def check_winner(player, board):
    """Check if the given player has won."""
    return any(all(board[i] == player for i in win) for win in winrows)

# Check if game is already concluded
XWins = check_winner("X", L)
OWins = check_winner("O", L)

if XWins or OWins:
    print("INVALID INPUT", end="")
    exit()
elif not XWins and not OWins and "-1" not in L:
    print("INVALID INPUT", end="")
# Set to store unique final board positions
unique_final_boards = set()

# Iterate over all empty positions where X can play
for i in range(9):
    if L[i] == "-1":
        L[i] = "X"  # X makes the first move
        
        # Check if X wins immediately
        if check_winner("X", L):
            unique_final_boards.add(tuple(L))
        else:
            # Iterate over remaining empty positions where O can play
            for j in range(9):
                if L[j] == "-1":
                    L[j] = "O"  # O plays optimally
                    
                    # Check if O wins (if O wins, this branch is invalid)
                    if not check_winner("O", L):
                        # X's second move
                        for k in range(9):
                            if L[k] == "-1":
                                L[k] = "X"  # X makes the second move
                                if check_winner("X", L):
                                    unique_final_boards.add(tuple(L))
                                L[k] = "-1"  # Reset position
                    L[j] = "-1"  # Reset position
        L[i] = "-1"  # Reset position

# Print the number of unique final boards
print(len(unique_final_boards), end='')
