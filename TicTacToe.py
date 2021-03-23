import sys
from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(
        '+-------+-------+-------+\n'
        '|       |       |       |\n'
        '|   ' + str(board[0][0]) + '   |   ' + str(board[0][1]) + '   |   ' + str(board[0][2]) + '   |\n'
        '|       |       |       |\n'
        '+-------+-------+-------+\n'
        '|       |       |       |\n'
        '|   ' + str(board[1][0]) + '   |   ' + str(board[1][1]) + '   |   ' + str(board[1][2]) + '   |\n'
        '|       |       |       |\n'
        '+-------+-------+-------+\n'
        '|       |       |       |\n'
        '|   ' + str(board[2][0]) + '   |   ' + str(board[2][1]) + '   |   ' + str(board[2][2]) + '   |\n'
        '|       |       |       |\n'
        '+-------+-------+-------+\n'
    )

    return None


def enter_move(board):
    # The function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision.
    free_fields = make_list_of_free_fields(board)
    while True:
        try:
            inp = int(input("Enter your move: "))
        except:
            print("Please use numbers from 1 to 9")
            continue
        if inp not in free_fields:
            print("Wrong move")
            continue
        break
    board[(inp - 1) // 3][(inp - 1) % 3] = 'O'
    display_board(board)
    victory_for(board, 'O')
    draw_move(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares = []
    for x in board:
        for y in x:
            if y in range(0, 10):
                free_squares.append(y)
    return free_squares


def victory_for(board, sign):
    # The function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    if sign == 'O':
        if (board[0][0] == board[0][1] == board[0][2] == 'O' or
                board[1][0] == board[1][1] == board[1][2] == 'O' or
                board[2][0] == board[2][1] == board[2][2] == 'O' or
                board[0][0] == board[1][0] == board[2][0] == 'O' or
                board[0][1] == board[1][1] == board[2][1] == 'O' or
                board[0][2] == board[1][2] == board[2][2] == 'O' or
                board[0][2] == board[1][1] == board[2][0] == 'O' or
                board[0][0] == board[1][1] == board[2][2] == 'O'):
            print('Congratulations you WON!!!')
            sys.exit()
    if sign == 'X':
        if (board[0][0] == board[0][1] == board[0][2] == 'X' or
                board[1][0] == board[1][1] == board[1][2] == 'X' or
                board[2][0] == board[2][1] == board[2][2] == 'X' or
                board[0][0] == board[1][0] == board[2][0] == 'X' or
                board[0][1] == board[1][1] == board[2][1] == 'X' or
                board[0][2] == board[1][2] == board[2][2] == 'X' or
                board[0][2] == board[1][1] == board[2][0] == 'X' or
                board[0][0] == board[1][1] == board[2][2] == 'X'):
            print('Computer is the WINNER. You LOST!!!')
            sys.exit()
    if len(make_list_of_free_fields(board)) == 0:
        print('That\'s a tie. No winner.')
        sys.exit()


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    print('Computer\'s move...')
    x = -1
    while x not in make_list_of_free_fields(board):
        x = randrange(1, 9)
        continue
    board[(x - 1) // 3][(x - 1) % 3] = 'X'
    display_board(board)
    victory_for(board, 'X')
    enter_move(board)


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
board[1][1] = 'X'
display_board(board)
enter_move(board)
