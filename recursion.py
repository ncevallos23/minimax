from classes import GoalMet, Node
from main import checkState, checkFull

from copy import deepcopy

import numpy as np

def getMoves(board):
    possible_moves = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    moves = []
    for move in possible_moves:
        if board[int(move[0])][int(move[1])] == '.':
            moves.append(move)

    return moves

def solve(node, player, board, nummove):
    win, nodeplayer = checkState(node.state, node.player)
    if win:
        node.setGoal(True)
        if nodeplayer % 2 == 0:
            node.setScore(1)
        else:
            node.setScore(-1)

    if checkFull(node.state):
        node.setGoal(True)
        node.setScore(0)

    if node.goal:
        return None

    children = []

    for move in getMoves(board):
        workingBoard = deepcopy(board)
        if player % 2 == 0:
            workingBoard[int(move[0])][int(move[1])] = "O"
        else:
            workingBoard[int(move[0])][int(move[1])] = "X"    

        children.append(Node(workingBoard, [], None, node, player, None, nummove + 1))

    node.children = deepcopy(children)

    for child in node.children:
        solve(child, player + 1, child.state, nummove + 1)


def getScore(node):
    node.parent.score_multiplyer = 100
    max_moves = 9
    score = max_moves - node.move
    if node.goal:
        if node.player % 2 == 0:
            return score * node.score_multiplyer
        else:
            return score * -1 * node.score_multiplyer

    if checkFull(node.state):
        return 0 * node.score_multiplyer

def minimax(node):
    if node.goal:
        return getScore(node)

    if node.player % 2 == 0:
        value = np.NINF

        for child in node.children:
            value = max(value, minimax(child))

        return value
    else:
        value = np.inf

        for child in node.children:
            value = min(value, minimax(child))

        return value

def bringUp(node, runningList):

    runningList.append(node)

    win, player = checkState(node.state, node.player)

    if win:
        return("your mom")

    for child in node.children:
        bringUp(child, runningList)

def findScore(node):
    for i in node.bringUp:
        win, player = checkState(i.state, i.player)
        if win:
            if player % 2 == 0:
                node.move_dict["O"] += 1
            else:
                node.move_dict["X"] += 1
        
        if checkFull(i.state):
            node.move_dict["CAT"] += 1




