from classes import Node
from main import board, printBoard
from recursion import solve, minimax, bringUp, findScore
from copy import deepcopy
import time


def work():
    print(time.perf_counter())
    wboard = deepcopy(board)
    wboard[1][1] = "X"
    printBoard(wboard)
    start = Node(wboard, [], False, None, 1, None, 2)

    solve(start, 2, wboard, 0)

    for child in start.children:
        bringUp(child, child.bringUp)
        print(child.bringUp)

    for child in start.children:
        print(len(child.bringUp))

    for child in start.children:
        findScore(child)
        print(child.move_dict)


    scores = []
    for child in start.children:
        scores.append(child.getScore())

    print(scores)

    print(wboard)
    print(start.state)
    print(time.perf_counter())

work()