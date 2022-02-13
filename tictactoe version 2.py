# Tic-Tac-Toe V2

import random


def draw_board(board):
    print("|" + board[1] + "|" + board[2] + "|" + board[3] + "|")
    print("|" + board[4] + "|" + board[5] + "|" + board[6] + "|")
    print("|" + board[7] + "|" + board[8] + "|" + board[9] + "|")


def input_player_letter():
    letter = ""
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    # First element is the player, second is the computer
    if letter == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


def who_goes_first():
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"


def play_again():
    print("Would you like to play again? (yes or no)")
    return input().lower().startswith("y")


def make_move(board, letter, move):
    board[move] = letter


def is_winner(board, letter):
    winning_combos = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for combo in winning_combos:
        return board[combo[0]] == letter and board[combo[1]] == letter and board[combo[2]] == letter


def get_board_copy(board):
    board_copy = []
    for n in board:
        board_copy.append(n)
    return board_copy


def is_space_free(board, move):
    return board[move] == ""


def get_player_move(board):
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split():
        print("What is your next move? (1-9)")
        move = input()
    return int(move)


def choose_random_move_from_list(board, moves_list):
    possible_moves = []
    for move in moves_list:
        if is_space_free(board, move):
            possible_moves.append(move)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


def get_computer_move(board, computer_letter):
    # Given a board and the computer's letter, determine where to move and return that move.
    if computer_letter == "X":
        player_letter = "O"
    else:
        player_letter = "X"

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i

    # Check if the player could win on his next move, and block them.
    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    # Try to take one of the corners, if they are free.
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if is_space_free(board, 5):
        return 5

    # Move on one of the sides.
    return choose_random_move_from_list(board, [2, 4, 6, 8])

def is_board_full(board):
    # Return True if every space on the board has been taken; otherwise return False.
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


print("Welcome to the game of Tic Tac Toe!")

while True:
    # Set an empty board.
    board = [" "] * 10
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()
    print("The " + turn.capitalize() + " goes first!")
    game_is_playing = True
    count = 0

    while game_is_playing:
        if turn == "player":
            # Player's turn.
            draw_board(board)
            move = get_player_move(board)
            board[move] = player_letter
            count += 1

            if is_winner(board, player_letter):
                draw_board(board)
                print("The Player is the winner!")
                game_is_playing = False
            else:
                if count > 9:
                    draw_board(board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "computer"

        else:
            # Computer's turn.
            move = get_computer_move(board, computer_letter)
            board[move] = computer_letter
            count += 1

            if is_winner(board, computer_letter):
                draw_board(board)
                print("The Computer is the winner! You lose.")
                game_is_playing = False
            else:
                if count > 9:
                    draw_board(board)
                    print("The game is a tie!")
                    break
                else:
                    turn = "player"

    if not play_again():
        break
