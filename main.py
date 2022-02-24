board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]

def printBoard(board):
    print(board[0])
    print(board[1])
    print(board[2])

def checkFull(board):
    emptyCount = 0
    for row in board:
        for cell in row:
            if cell == ".":
                emptyCount+=1
    
    if emptyCount == 0:
        return True
    else:
        return False

def checkState(board, player):
    #player1 will be X and player2 will be O
    #true means that won
    #false means that not won
    if player % 2 != 0:
        if board[0][0] == "X":
            if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
                return True, player
            elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
                return True, player
            elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                return True, player
            else:
                return False, player
        elif board[0][1] == "X":
            if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
                return True, player
            else:
                return False, player
        elif board[0][2] == "X":
            if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
                return True, player
            elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                return True, player
            else:
                return False, player
        elif board[1][0] == "X":
            if board[1][0] == board[1][1] and board[1][1] == board [1][2]:
                return True, player
            else:
                return False, player
        elif board[2][0] == "X":
            if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
                return True, player
            else:
                return False, player
        else:
            return False, player
    else:
        if board[0][0] == "O":
            if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
                return True, player
            elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
                return True, player
            elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                return True, player
            else:
                return False, player
        elif board[0][1] == "O":
            if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
                return True, player
            else:
                return False, player
        elif board[0][2] == "O":
            if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
                return True, player
            elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                return True, player
            else:
                return False, player
        elif board[1][0] == "O":
            if board[1][0] == board[1][1] and board[1][1] == board [1][2]:
                return True, player
            else:
                return False, player
        elif board[2][0] == "O":
            if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
                return True, player
            else:
                return False, player
        else:
            return False, player
