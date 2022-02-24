from main import checkState, checkFull

class Node():
    def __init__(self, state, children, goal, parent, player, score, move):
        self.state = state
        self.children = children
        self.goal = goal
        self.parent = parent
        self.score = score
        self.player = player
        self.move = int(move)
        self.score_multiplyer = 1
        self.move_dict = {"X": 0, "O": 0, "CAT": 0}
        self.bringUp = []
    def setChildren(self, child):
        self.children.append(child)
    def getParent(self):
        return self.parent
    def getState(self):
        return self.state
    def getChildren(self):
        return self.children
    def setGoal(self, goal):
        self.goal = goal
    def getGoal(self):
        return self.goal
    def getPlayer(self):
        return self.player
    def setScore(self, score):
        self.score = score
    def nodeReset(self, state, children, goal, parent, player, score):
        self.state = state
        self.children = children
        self.goal = goal
        self.parent = parent
        self.player = player
        self.score = score
    def getScore(self):
        win = None
        for child in self.children:
            win, player = checkState(child.state, child.player)
            if win:
                if player % 2 == 0:
                    self.score_multiplyer = 100
                else:
                    self.score_multiplyer = -100
                    break
        self.score = self.move_dict["X"] - self.move_dict["O"]
        if self.score < 0 and win and player % 2 != 0:
            return self.score * self.score_multiplyer * -1
        elif self.goal:
            return 1000000000
        else:
            return self.score * self.score_multiplyer


class GoalMet(Exception):
    pass