import math
import random
from Models.Grid import Grid
from Models.Node import Node
from Models.Tree import Tree
from Views.GridView import GridView

class Agent:
    def __init__ (self, team:str):
        self.team = team
        if team == "x":
            self.otherTeam = "o"
        else:
            self.otherTeam = "x"

    # agent makes a play
    # @param board: current state of the game
    # @returns: board after the move is made or None if no move can be made
    def make_move(self, board:Grid):
        # make first move of game random
        if len(board.get_empty_cells()) == 9:
            copy = board.copy()
            copy.cells[random.randint(0, 8)].value = self.team
            return copy

        root = Node(board)
        bestMove = self.minimax_Descision(root, -math.inf, math.inf, True)
        
        for i in range(0, len(root.children)):
            hasBest = self.find(root.children[i], bestMove)
            if hasBest:
                return root.children[i].grid

        return bestMove.grid

    def find(self, node:Node, goal:Node):
        b = False
        for i in range(0, len(node.children)):
            # view = GridView()
            # view.display(node.grid)
            if node.children[i].grid.cells == goal.grid.cells:
                return True
            else:
                b = self.find(node.children[i], goal)
                if b:
                    return True


        return b

    def minimax_Descision(self, board:Node, a:int, b:int, maximizingAgent:bool):
        if self.has_goal(board.grid, self.team):
            board.score = 1
            return board
        elif self.has_goal(board.grid, self.otherTeam):
            board.score = -1
            return board
        elif len(board.grid.get_empty_cells()) == 0:
            board.score = 0
            return board
        
        if maximizingAgent:
            return self.max_value(board, a, b, True)
        else:
            return self.min_value(board, a, b, False)

    def min_value(self, board:Node, a:int, b:int, maximizingAgent:bool):
        minEvaluation = Node(None)
        minEvaluation.score = math.inf

        empty = board.grid.get_empty_cells()
        for i in range(0, len(empty)):
            deepcopy = board.grid.copy()
            deepcopy.getCell(empty[i].xPos, empty[i].yPos).value = self.otherTeam
            deepcopyNode = Node(deepcopy)
            board.add_child(deepcopyNode)
            evaluation = self.minimax_Descision(deepcopyNode, a, b, not maximizingAgent)
            minEvaluation = self.min(minEvaluation, evaluation)
            minEvaluation.parent = board
            b = min(b, evaluation.score)
            if b < a:
                break

        return minEvaluation

    def max_value(self, board:Node, a:int, b:int, maximizingAgent:bool):
        maxEvaluation = Node(None)
        maxEvaluation.score = -math.inf

        empty = board.grid.get_empty_cells()
        for i in range(0, len(empty)):
            deepcopy = board.grid.copy()
            deepcopy.getCell(empty[i].xPos, empty[i].yPos).value = self.team
            deepcopyNode = Node(deepcopy)
            board.add_child(deepcopyNode)
            evaluation = self.minimax_Descision(deepcopyNode, a, b, not maximizingAgent)
            maxEvaluation = self.max(maxEvaluation, evaluation)
            a = max(a, evaluation.score)
            if b < a:
                break

        return maxEvaluation

    def min(self, minEvaluation:Node, evaluation:Node):
        if minEvaluation.score < evaluation.score:
            return minEvaluation

        return evaluation

    def max(self, maxEvaluation:Node, evaluation:Node):
        if maxEvaluation.score > evaluation.score:
            return maxEvaluation

        return evaluation

    def has_goal(self, board:Grid, team:str):

        if board == None:
            return False

        # for any given cell
        if board.cells[0].value == team and board.cells[1].value == team and board.cells[2].value == team:
            return True

        if board.cells[3].value == team and board.cells[4].value == team and board.cells[5].value == team:
            return True

        if board.cells[6].value == team and board.cells[7].value == team and board.cells[8].value == team:
            return True

        if board.cells[0].value == team and board.cells[3].value == team and board.cells[6].value == team:
            return True

        if board.cells[1].value == team and board.cells[4].value == team and board.cells[7].value == team:
            return True

        if board.cells[2].value == team and board.cells[5].value == team and board.cells[8].value == team:
            return True

        if board.cells[0].value == team and board.cells[4].value == team and board.cells[8].value == team:
            return True

        if board.cells[6].value == team and board.cells[4].value == team and board.cells[2].value == team:
            return True

        return False