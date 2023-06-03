import math
import random
from Models.Grid import Grid
from Models.Node import Node
from Models.SudokuBoard import SudokuBoard
from Models.Tree import Tree
from Views.GridView import GridView

# global constraint Alldiff - all the variables involved in the 
# constraint must have different values.
#
# Domain of variables 1 though 9
#
# sudoku rules:
# no col can have repeat value
# no row can have repeat value
# 81 total cells in grid
# some cells have a filled in value (domain 1 to 9)
# is a CSP with 81 variables (each cell)
# empty cell domain 1 to 9
# row / column domain 1 to 9 : x != xi
# total 27 different alldiff constraints, one for each row, col, 3x3 box


class Agent:
    def __init__ (self):
        return None

    def make_move(self, board:SudokuBoard):
        return self.back_tracking_search(board)

    def back_tracking_search(self, board:SudokuBoard):
        return self.back_track(board)

    def back_track(self, board:SudokuBoard):
        return None

    def find(self, node:Node, goal:Node):
       return None

    def all_different(self, list:list):
        seen = []
        for i in range(0, len(list)):
            #ignore empty cells
            if list[i] == " ":
                continue

            if list[i] in seen:
                return False
            else:
                seen.append(list[i])

        return True

    def has_goal(self, board:Grid, team:str):
        return False