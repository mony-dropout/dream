import copy
#just stupid ahh brute force
#btw i think the correct soln would be: generate all winning permutations, and then go back and store all positions you coulda got there from
#and like store it in a hash
#like lexographically order these things, and when you can go back and get there, add 1 to the map
board_state = []
for i in range(9):
    entry = input()
    board_state.append(entry)

def check_x_winner(board):
    x_win_count = 0
    if board[0] == board[1] == board[2] == "X":
        if board[0] == board[3] == board[6] == "X":
            x_win_count += 1
        if board[1] == board[4] == board[7] == "X":
            x_win_count += 1
        if board[2] == board[5] == board[8] == "X":
            x_win_count += 1
        if board[0] == board[4] == board[8] == "X":
            x_win_count += 1
        if board[2] == board[4] == board[6] == "X":
            x_win_count += 1
        else:
            x_win_count += 1

    if board[3] == board[4] == board[5] == "X":
        if board[0] == board[3] == board[6] == "X":
            x_win_count += 1
        if board[1] == board[4] == board[7] == "X":
            x_win_count += 1
        if board[2] == board[5] == board[8] == "X":
            x_win_count += 1
        if board[0] == board[4] == board[8] == "X":
            x_win_count += 1
        if board[2] == board[4] == board[6] == "X":
            x_win_count += 1
        else:
            x_win_count += 1
    
    if board[6] == board[7] == board[8] == "X":
        if board[0] == board[3] == board[6] == "X":
            x_win_count += 1
        if board[1] == board[4] == board[7] == "X":
            x_win_count += 1
        if board[2] == board[5] == board[8] == "X":
            x_win_count += 1
        if board[0] == board[4] == board[8] == "X":
            x_win_count += 1
        if board[2] == board[4] == board[6] == "X":
            x_win_count += 1
        else:
            x_win_count += 1
    
    if x_win_count == 1:
        return "X win"
    if x_win_count == 0:
        return "continue"
    else:
        return "invalid input"

def check_o_winner(board):
    o_win_count = 0
    if board[0] == board[1] == board[2] == "O":
        o_win_count += 1
    if board[3] == board[4] == board[5] == "O":
        o_win_count += 1
    if board[6] == board[7] == board[8] == "O":
        o_win_count += 1
    if board[0] == board[4] == board[8] == "O":
        o_win_count += 1
    if board[2] == board[4] == board[6] == "O":
        o_win_count += 1
    if board[0] == board[3] == board[6] == "O":
        o_win_count += 1
    if board[1] == board[4] == board[7] == "O":
        o_win_count += 1
    if board[2] == board[5] == board[8] == "O":
        o_win_count += 1
    
    if o_win_count == 1:
        return "O win"
    if o_win_count == 0:
        return "continue"
    else:
        return "invalid input"

if check_o_winner(board_state) and check_x_winner(board_state) != "continue":
    print("INVALID INPUT", end="")
    quit()

available_moves = []
for idx, val in enumerate(board_state):
    if val == "-1":
        available_moves.append(idx)

x_count, o_count = board_state.count("X"), board_state.count("O")
if x_count - o_count > 1 or o_count > x_count:
    print("INVALID INPUT", end="")
    exit()

winning_boards = []
for move_x in available_moves:
    temp_board = board_state.copy()
    temp_board[move_x] = "X"
    if check_x_winner(temp_board) == "X win":
        winning_boards.append(temp_board)
    elif check_x_winner(temp_board) == "continue":
        for move_o in available_moves:
            if move_x != move_o:
                temp_board2 = temp_board.copy()
                temp_board2[move_o] = "O"
                if check_o_winner(temp_board2) == "continue":
                    for move_x2 in available_moves:
                        if move_x != move_o != move_x2:
                            temp_board3 = temp_board2.copy()
                            temp_board3[move_x2] = "X"
                            if check_x_winner(temp_board3) == "X win":
                                winning_boards.append(temp_board3)
unique_boards = []
for b in winning_boards:
    if b not in unique_boards:
        unique_boards.append(b)
print(len(unique_boards), end="")