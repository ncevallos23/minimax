import random
from main import board, printBoard, checkFull, checkState
from classes import Node, GoalMet
from recursion import solve, minimax, bringUp, findScore
from copy import deepcopy
import numpy as np

working = deepcopy(board)

global move_num
move_num = 1

#TODO correct this to wokr with new checkState and solve functions, do recusions
def play(board, num):
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
        return True, board

    if checkFull(board):
        return True, board

    num += 1

    #player two down below
    node = Node(board, [], False, None, 2, None, num)
    solve(node, 2, board, num)

    printBoard(board)
    print("Player 2")


    start_val = np.NINF

    for child in node.children:
        bringUp(child, child.bringUp)
    
    for child in node.children:
        findScore(child)

    choosen_child = None

    for child in node.children:
        start_val = max(start_val, child.getScore())

        if child.getScore() == start_val:
            choosen_child = child


    wboard = deepcopy(choosen_child.state)

    win, winplayer = checkState(wboard, 2)

    if win:
        return True, wboard

    if checkFull(wboard):
        return True, wboard

    return False, wboard

while True:
    win_state, working = play(working, move_num)
    if win_state:
        printBoard(working)
        break
