sudoku = [["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]

#row valid

for i in range(9):
    temp_arr = []
    for j in range(9):
        if sudoku[i][j] == ".":
            sudoku[i][j] = 0
        # print(sudoku[i][j], end="   ")

        element = int(sudoku[i][j])

        if ((1<= element <= 9) and (element not in temp_arr)) or (element == 0):
            temp_arr.append(element)
        else:
            print(False)
    print(temp_arr)
    # print("\n")

iter = 1

temp2d = [[]]

for i in range(9):
        
