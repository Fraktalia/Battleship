def main():
    player = "X"
    board = init_board()
    display_board(board)
    move = get_move(board)
    mark(board,move[0],move[1],player)
    display_board(board)


def init_board():
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

        if len(player_input) > 2:
            row = -1

        if row < 0 or col < 0:
            print("\nYou're out of range!")
        elif board[row][col] != "0":
            print("\nHere you already tried, try again!")
        else:
            is_input_valid = True

    return row, col

def mark(board, row, col, player):
    board[row][col]=player
    return board
    

if __name__ == "__main__":
    main()
