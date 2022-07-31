from random import randint
from msvcrt import getch

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def board():
    # Board for holding ship locations
    HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
    # Board for displaying hits and misses
    GUESS_BOARD = [[" "] * 8 for x in range(8)]
    return HIDDEN_BOARD, GUESS_BOARD


# displaying the board
def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


# computer create 5 ships
def create_ships(board):
    ship_row, ship_column = randint(0, 7), randint(0, 7)
    board[ship_row][ship_column] = "X"
    ship = 1
    while ship < 5:
        k = 0
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        if board[ship_row][ship_column] == "X":
            k = 1
        else:
            for x in range(ship_row - 1, ship_row + 2):
                for y in range(ship_column - 1, ship_column + 2):
                    if x == -1 or x == 8 or y == -1 or y == 8:
                        l = 0
                    elif board[x][y] == "X":
                        k = 1
                        break
        if k == 0:
            board[ship_row][ship_column] = "X"
            ship += 1


# get the location from the use
def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, Please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, Please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]


# check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def battleship(HIDDEN_BOARD, GUESS_BOARD):
    create_ships(HIDDEN_BOARD)
    turns = 11
    while turns > 0:
        print('Guess a Battleship location')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "-"
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You win!")
            break
        print(f"You have {str(turns)} turns left")
        if turns == 0:
            print("You ran out of turns")
            print("Hit enter to see the location of Battleships")
            getch()
            print('-------Here is the true location of Battleships--------')
            print_board(HIDDEN_BOARD)


def main():
    HIDDEN_BOARD, GUESS_BOARD = board()
    battleship(HIDDEN_BOARD, GUESS_BOARD)
    restart = "1"
    while restart == "1":
        restart = input("Do you wish to Play again?\nIf YES type \"1\" Else type \"0\" :: ")
        if restart == "1":
            HIDDEN_BOARD, GUESS_BOARD = board()
            battleship(HIDDEN_BOARD, GUESS_BOARD)
        elif restart == "0":
            exit()
        else:
            print('Not an appropriate choice.')
            restart = "1"


if __name__ == "__main__":
    main()
