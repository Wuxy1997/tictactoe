import math
board=["_","_","_",
       "_","_","_",
       "_","_","_"]

game_still_going = True

winner=None

current_player = "X"

def displayboard():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

def play_game():

    displayboard()
    
    while game_still_going:
        print(current_player+"'s turn")
        handle_turn(current_player)

        check_if_game_over()

        flip_player()
        

    if winner == "X" or winner == "O":
        print (winner+"won")
    elif(winner == None):
        print ("Tie")

def handle_turn(player):
    position = input("choose a position from 1-9: ")
    while position not in {"1","2","3","4","5","6","7","8","9"}:
        position = input("only from 1-9: ")
    position = int(position) - 1

    board[position] = player
    displayboard()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    global winner

    row_winner = check_rows()
    columns_winner = check_columns()
    diagonals_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return

def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    diagnoals_1 = board[0] == board[4] == board[8] != "_"
    diagnoals_2 = board[2] == board[4] == board[6] != "_"
    if diagnoals_1 or diagnoals_2:
        game_still_going = False
    if diagnoals_1:
        return board[0]
    elif diagnoals_2:
        return board[2]
    return

def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False

    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()