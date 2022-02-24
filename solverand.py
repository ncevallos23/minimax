import random
from main import board, printBoard, checkFull, checkState
from recursion import solve, minimax, bringUp, findScore

wboard = board

#TODO correct this to wokr with new checkState and solve functions, do recusions
def play(board):
    printBoard(board)
    print("Player 1")
    while True:
        Xmove = input("Player 1: ")
        #check move
        if board[int(Xmove[0])][int(Xmove[1])] == ".":
            break
    board[int(Xmove[0])][int(Xmove[1])] = "X"

    win, winplayer = checkState(board, 1)

    if win:
        return True

    if checkFull(board):
        return True


    printBoard(board)
    print("Player 2")
    while True:
        Ymove = [random.randint(0,2), random.randint(0,2)]
        #check move
        if board[int(Ymove[0])][int(Ymove[1])] == ".":
            break
    board[int(Ymove[0])][int(Ymove[1])] = "O"
    
    win, winplayer = checkState(board, 2)

    if win:
        return True

    if checkFull(board):
        return True

while True:
    if play(wboard):
        printBoard(wboard)
        break

