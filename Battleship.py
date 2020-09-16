import time
import os

def main():
    small_ships_1 = 2
    small_ships_2 = 2
    big_ships_1 = 0
    big_ships_2 = 0
    board_1 = init_board()
    board_2 = init_board_1()

    while big_ships_1 > 0:
        print ("PLAYER 1")
        os.system("cls || clear")
        display_board(board_1)
        player = "X"
        move = get_move(board_1)
        board_1 = mark(board_1,move[0],move[1],player)
        display_board(board_1)
        move = get_move_rest_ship(board_1, move)
        board_1 = mark(board_1,move[0],move[1],player)
        big_ships_1 = big_ships_1 - 1

    while small_ships_1 > 0:
        print ("PLAYER 1")
        os.system("cls || clear")
        display_board(board_1)
        player = "X"
        move = get_move(board_1)
        board_1 = mark(board_1,move[0],move[1],player)
<<<<<<< Updated upstream
        ships_1 = ships_1 - 1
    display_board(board_1)
    
    time.sleep(3) 
=======
        small_ships_1 = small_ships_1 - 1

    time.sleep(0.5) 
>>>>>>> Stashed changes
    os.system("cls || clear")
    print ("\nNext player's placement phase. Please, press any button.")
    input ("")
    time.sleep(0.5)  

    while big_ships_2 > 0:
        print ("PLAYER 2")
        os.system("cls || clear")
        display_board(board_2)
        player = "X"
        move = get_move(board_2)
        board_2 = mark(board_2,move[0],move[1],player)
        display_board(board_1)
        move = get_move_rest_ship(board_2, move)
        board_2 = mark(board_2,move[0],move[1],player)
        big_ships_2 = big_ships_2 - 1

    while small_ships_2 > 0:
        print ("PLAYER 2")
        os.system("cls || clear")
        display_board(board_2)
        player = "X"
        move = get_move(board_2)
        board_2 = mark(board_2,move[0],move[1],player)
        small_ships_2 = small_ships_2 - 1


    os.system("cls || clear")

    start_game(board_1, board_2)


def shooting_board():
    board = [ [".", ".", ".", ".", "."],
            [".", ".", ".", ".", "."], 
            [".", ".", ".", ".", "."], 
            [".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".",] ]
    return board


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

<<<<<<< Updated upstream

def display_board(board):
=======
>>>>>>> Stashed changes

def display_board(board):
    print('    A', '  B', '  C', '  D', '  E\n')
    for count, row in enumerate(board, 1):
        print(count,' ','   '.join([str(elem) for elem in row]))
    return


def get_move(board):
<<<<<<< Updated upstream
    is_input_valid = False
    while (not is_input_valid):
        player_input = input("\nEnter the field, e.g. A1:").upper()
        coordinates = row_and_col(player_input)
        if len(player_input) > 2:
            row = -1

        if coordinates[0] < 0 or coordinates[1] < 0:
            print("\nYou're out of range!")
        elif board[coordinates[0]][coordinates[1]] == "X":
            print("\nHere you already tried, try again!")
        else:
            is_input_valid = True
=======
    coordinates = []
    while not placement_check(board, coordinates):
        if len(coordinates) > 0:
            print("You cannot place a ship here")
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
>>>>>>> Stashed changes

    return coordinates


<<<<<<< Updated upstream
=======
def get_move_rest_ship(board, previous_move):
    allowed_options = []
    while True:
        if previous_move[0] > 0:
            print("1 - North")
            allowed_options.append(1)
        if previous_move[0] < 4:
            print('2 - South')
            allowed_options.append(2)
        if previous_move[1] < 4:
            print('3 - East')
            allowed_options.append(3)
        if previous_move[1] >0:
            print("4 - West")
            allowed_options.append(4)
        big_ship = int(input("Enter direction of the ship: "))
        if big_ship in allowed_options:
            if big_ship == 1:
                return [previous_move[0]-1,previous_move[1]]
            if big_ship == 2:
                return [previous_move[0]+1,previous_move[1]]
            if big_ship == 3:
                return [previous_move[0],previous_move[1]+1]
            if big_ship == 4:
                return [previous_move[0],previous_move[1]-1]
        else:
            print("\nYou're out of range!")
    

>>>>>>> Stashed changes
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
    

<<<<<<< Updated upstream
=======
def placement_check(board, move):
    if len(move) == 0:
        return False
    if board[move[0]][move[1]] == '0':
        if board[get_index(move[0],1)][move[1]] == '0' and board[get_index(move[0],-1)][move[1]] == '0' and board[move[0]][get_index(move[1],1)] == '0' and board[move[0]][get_index(move[1],-1)] == '0':
            return True
        else:
            return False
    else:
        return False


def get_index(index, to_add):
    new_index = index + to_add
    if new_index < 0:
        return 0
    if new_index > 4:
        return 4
    return new_index




def start_game(board_1, board_2):
    shooting_board_1 = shooting_board()
    shooting_board_2 = shooting_board()
    current_shooting_board = shooting_board_1
    current_player_board = board_1
    current_player = 1
    while not has_won(current_shooting_board, current_player_board):
        os.system("cls || clear")
        display_board(current_shooting_board)
        player_input = input(f"\nPlayer {current_player} enter coordinates of your shoot e.g. A1:").upper()
        coordinates = row_and_col(player_input)


        if current_player_board[coordinates[0]][coordinates[1]] == "X":
            print("\nYou've hit a ship!")
            current_shooting_board[coordinates[0]][coordinates[1]] = "S"
        else:
            print("\nYou've missed!")
            current_shooting_board[coordinates[0]][coordinates[1]] = "M"

        input('Press enter to continue')

        if current_player == 1:
            current_player = 2
            current_shooting_board = shooting_board_2
            current_player_board = board_2
        else:
            current_shooting_board = shooting_board_1
            current_player_board = board_1
            current_player = 1
        
        
        
def has_won(current_shooting_board, current_player_board):
    pass     




>>>>>>> Stashed changes
if __name__ == "__main__":
    main()
