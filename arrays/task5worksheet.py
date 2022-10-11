rows, cols = (6, 4)
arr = [["X" for i in range(cols)] for j in range(rows)]
row_move = 0
col_move = 0
arr[row_move][col_move] = "O"
print(arr)
while row_move != -1:
    arr[row_move][col_move] = "X"
    row_move = int(input("Enter row move")) - 1
    col_move = int(input("Enter column move")) - 1
    arr[row_move][col_move] = "O"
    print(arr)
#endwhile
