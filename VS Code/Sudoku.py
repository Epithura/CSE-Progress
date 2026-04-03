I=[0,1,2,3,4,5,6,7,8]
board=[]
for i in range(9):
    row = list(map(int, input().split()))  # Take a row as input
    if len(row) != 9:  # Check if the row has exactly '9' elements
        print("INVALID INPUT")
        exit()
    else:
       board.append(row)  # Append the valid row
for i in range(9):
    I.remove(i)
    if board[i].count(i+1)!=1:
        print("False", end="")
        exit()
    elif any(board[i][0]==board[j][0] for j in I):
        print("False", end="")
        exit()

for row in range(0, 9, 3):  # Step by 3 for rows
    for col in range(0, 9, 3):  # Step by 3 for columns
        sub_box = []
        for i in range(3):  # 3 rows inside a box
            for j in range(3):  # 3 columns inside a box
                num = board[row + i][col + j]
                if num in sub_box:  # Duplicate number
                    print("False", end="")
                    exit()
                sub_box.append(num)

print("True", end="")  # If all checks pass, it's a valid Sudoku board
