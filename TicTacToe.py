import numpy as np
import random
from time import sleep
import sys

game_board = np.array(["-", "-", "-", "-", "-", "-", "-", "-", "-"])


def player_choice():
    try:

        choice = int(input('Player choose 1. X or 2. O : '))
        if choice == 1:
            player = 'X'
        elif choice == 2:
            player = 'O'
        else:
            raise Exception()

        if player == 'X':
            computer = 'O'
        else:
            computer = 'X'

    except:
        print('Invalid Selection!')
        exit()

    return player, computer


def print_board():
    print(" " + game_board[0] + " | " + game_board[1] + " | " + game_board[2] + "  ")
    # print("---+---+---")
    print(" " + game_board[3] + " | " + game_board[4] + " | " + game_board[5] + "  ")
    # print("---+---+---")
    print(" " + game_board[6] + " | " + game_board[7] + " | " + game_board[8] + "  ")


def getPlayerMove():
    while True:
        try:
            moveTo = int(input('Player choose your move : '))

            if game_board[moveTo] == '-':
                return moveTo
                break
            else:
                print('Place already occupied. Choose an empty place')
                continue
        except:
            print('Invalid input', sys.exc_info()[0])


def getComputerMove():
    while True:
        sleep(2)
        moveTo = random.randint(0, 8)

        if game_board[moveTo] == '-':
            return moveTo
            break
        else:
            print('Place already occupied. Choose another random number')
            continue


def evaluateBoard(player, computer):
    result, sign = checkRows()

    if result:
        return sign

    result, sign = checkColumns()
    if result:
        return sign

    result, sign = checkDiagonals()
    if result:
        return sign
    return '-'


def checkDiagonals():
    won = False
    sign = '-'
    for diag in range(2):
        current_diag = getDiagonals(diag)
        if allSame(current_diag):
            won = True
            sign = current_diag[0]
            return won, sign
        # break
    return won, sign


def getDiagonals(d):
    if d == 0:
        return [game_board[i] for i in range(d, 9, 4)]
    else:
        return [game_board[i] for i in range(2, 7, 2)]


def checkColumns():
    won = False
    sign = '-'

    for col in range(3):
        current_col = getColumns(col)
        '''if col == 0:
            current_col = [game_board[i] for i in range(0, 7, 3)]
        elif col == 1:
            current_col = [game_board[i] for i in range(1, 8, 3)]
        else:
            current_col = [game_board[i] for i in range(2, 9, 3)]'''

        if allSame(current_col):
            won = True
            sign = current_col[0]
            return won, sign
            # break
    return won, sign


def getColumns(col):
    return [game_board[i] for i in range(col, col + 7, 3)]


def checkRows():
    won = False
    sign = '-'
    for row in range(3):
        if row == 0:
            current_row = list(game_board[0:3])
        elif row == 1:
            current_row = list(game_board[3:6])
        else:
            current_row = list(game_board[6:9])

        if allSame(current_row):
            won = True
            sign = current_row[0]
            return won, sign
            # break
    return won, sign


def allSame(line):
    if line.count(line[0]) == len(line) and line[0] != '-':
        return True
    else:
        return False


def fillBoard(pos, sign):
    game_board[pos] = sign


def play_game(player, computer):
    # game_board = np.array(["-", "-", "-", "-", "-", "-", "-", "-", "-"])
    counter = 0
    move = 0
    sign = ''
    won = '-'

    while counter <= 8:
        # if counter == 0 or counter == 2 or counter == 4 or counter == 6 or counter == 8:
        if counter in [0, 2, 4, 6, 8]:
            move = getPlayerMove()
            sign = player
        else:
            move = getComputerMove()
            sign = computer
        fillBoard(move, sign)
        print_board()
        if counter >= 4:
            won = evaluateBoard(player, computer)
            # print('Counter is at : ', counter)
            if won != '-':
                tie = 1
                break
        counter += 1

    return won


def main():
    print("TIC TAC TOE")
    while True:
        player, computer = player_choice()
        print_board()
        won = play_game(player, computer)

        if won == player:
            print('Player is the winner !')
            break
        elif won == computer:
            print('Computer is the winner !')
            break
        else:
            ans = input('Its a tie. Do you want to play again ? (Y/N) ')

            if ans == 'Y' or ans == 'y':
                for i in range(9):
                    game_board[i] = '-'
                    continue
            else:
                break


main()
