import copy
#this is again ez, you js go through rows and cols one by one, the main thing is the 3by3 thingy
def rotate_matrix(matrix):
    rotated = []
    size = len(matrix)
    for col in range(size):
        new_row = [row[col] for row in matrix]
        rotated.append(new_row)
    return rotated
#this is the main function 
def check_sudoku(grid):
    if not grid or len(grid) == 1:
        return True
    temp_cols = copy.deepcopy(grid)
    temp_rows = copy.deepcopy(grid)
    
    size = len(grid)
    check_count = (size - 1) * size * 2
    
    for column in rotate_matrix(temp_cols):
        last_value = column.pop()
        check_count -= sum(1 for val in column if val != last_value)

    for row in temp_rows:
        last_value = row.pop()
        check_count -= sum(1 for val in row if val != last_value)

    

    grid.pop()
    for row in grid:
        row.pop()

    return check_count == 0 and check_sudoku(grid)

valid_digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
sudoku_board = []

#just take inputs now
for _ in range(9):
    row_input = input()
    sudoku_board.append([char for char in row_input if char in valid_digits])
#done
print(check_sudoku(sudoku_board), end="")