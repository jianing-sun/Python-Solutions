# 12/03/2017
# Jianing Sun


from IPython.display import clear_output
import numpy as np
import random

win = 0
tie = 0
marker = " "
board = [" "] * 9


def print_board(board):
    print("|||||||||||||")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("|||||||||||||")
    return board

def player_input(player):
    board_position = input("Player %s, Please enter a number for the board position from 1-9: " % player)

    while board_position.isdigit() == False:
        board_position = input("Please enter a digit from 1 to 9: ")

    board_position = (int)(board_position)
    while board[board_position-1] != " ":
        print("Warning: Position %s has already a marker. Please try another" % board_position)
        board_position = input("Try another: ")
        board_position = (int)(board_position)

    # marker = input("X for player 1, O for player 2: ")
    if player == 2:
        marker = 'O'
    elif player == 1:
        marker = 'X'

    while marker != 'X' and marker != 'O':
        marker = input("Please enter X or O: ")
    board[board_position - 1] = marker

    return marker,board_position

def which_player(marker, player_initial):
    if marker == " ":
        player = player_initial
    elif marker == "X":
        player = 2
    elif marker == "O":
        player = 1

    return player

def put_marker(board, marker, position):
    board[position-1]=marker
    return board

def choose_first():
    player_initial = random.randint(1, 2)
    if player_initial == 1: temp_mark='X'
    elif player_initial == 2:temp_mark='O'
    print("Player %s goes first with marker %%s" %player_initial %temp_mark)
    return player_initial

def win_check(mark):
    win=0
    tie=0
    if (board[0] == board[1] == board[2] == mark) or \
       (board[0] == board[3] == board[6] == mark) or \
       (board[0] == board[4] == board[8] == mark):
        win = 1
    elif (board[3] == board[4] == board[5] == mark) or \
         (board[6] == board[7] == board[8] == mark) or \
         (board[1] == board[4] == board[7] == mark) or \
         (board[2] == board[5] == board[8] == mark) or \
         (board[2] == board[4] == board[6] == mark):
        win = 1
    if win == 1:
        if mark == 'O':
            print('Game Over. Player 2 won the game. Congratulations!')
        elif mark == 'X':
            print('Game Over. Player 1 won the game. Congratulations!')
    # print('board[0]: {}. board[1]: {}. board[2]: {}. mark: {}.'.format(board[0], board[1], board[2], mark))
    return win == 1

def tie_check(board):
    if " " in board[1:]:
        return False
    else:
        return True

def reset_board():
    global board
    board = [" "] * 9


if __name__ == '__main__':
    print('Welcome to Tic Tac Toe!')
    GameOver = False
    Tie = False
    Begin = True
    Game_state = True
    player_initial = choose_first()
    while Begin == True:
        while GameOver == False and Tie == False:
            player = which_player(marker, player_initial)
            marker, position = player_input(player)
            board = put_marker(board, marker, position)
            print_board(board)
            GameOver = win_check(marker)
            Tie = tie_check(board)
            if Tie == True:
                print("Tie! No more space. What a neck-and-neck game!")
                print("Game Over.")
            if GameOver == True or Tie == True :
                Game_state = False
            if Game_state == False:
                try_again = input("Would you like to play again? y/n ")
                if try_again == 'y':
                    Begin = True
                    Tie = False
                    GameOver = False
                    Game_state = True
                    clear_output()
                    reset_board()
                    print("\n")
                    print('Welcome to Tic Tac Toe!')
                    choose_first()
                else:
                    Begin = False
                    print("Thank you. Have a nice day!")





