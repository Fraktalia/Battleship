import time

def main():
    ships_1 = 5
    ships_2 = 5
    board_1 = init_board()
    board_2 = init_board_1()
    while ships_1 > 0:
        print ("PLAYER 1")
        display_board(board_1)
        player = "X"
        move = get_move(board_1)
        board_1 = mark(board_1,move[0],move[1],player)
        ships_1 = ships_1 - 1

    time.sleep(0.5)  
    print ("DUPA")
    time.sleep(0.5)  

    while ships_2 > 0:
        print ("PLAYER 2")
        display_board(board_2)
        player = "X"
        move = get_move(board_2)
        board_2 = mark(board_2,move[0],move[1],player)
        ships_2 = ships_2 - 1


def init_board():
    board = [ ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"], 
            ["0", "0", "0", "0", "0"], 
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0",] ]
    return board

def init_board_1():
    board = [ ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"], 
            ["0", "0", "0", "0", "0"], 
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0",] ]
    return board

def display_board(board):

    print('    A', '  B', '  C', '  D', '  E\n')
    for count, row in enumerate(board, 1):
        print(count,' ','   '.join([str(elem) for elem in row]))
    return


def get_move(board):
    is_input_valid = False
    while (not is_input_valid):
        player_input = input("Enter the field, e.g. A1:").upper()
        coordinates = row_and_col(player_input)
        if len(player_input) > 2:
            row = -1

        if coordinates[0] < 0 or coordinates[1] < 0:
            print("\nYou're out of range!")
        elif board[coordinates[0]][coordinates[1]] == "X":
            print("\nHere you already tried, try again!")
        else:
            is_input_valid = True

    return coordinates

def row_and_col(player_input):

        if "A" in player_input:
            col = 0
        elif "B" in player_input:
            col = 1
        elif "C" in player_input:
            col = 2
        elif "D" in player_input:
            col = 3
        elif "E" in player_input:
            col = 4
        else:
            col = -1

        if "1" in player_input:
            row = 0
        elif "2" in player_input:
            row = 1
        elif "3" in player_input:
            row = 2
        elif "4" in player_input:
            row = 3
        elif "5" in player_input:
            row = 4
        else:
            row = -1
        return row, col

def mark(board, row, col, player):
    board[row][col]=player
    return board
    

if __name__ == "__main__":
    main()
