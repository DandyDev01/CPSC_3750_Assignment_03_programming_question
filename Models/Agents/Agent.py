import math
import random
from Models.Grid import Grid
from Models.Node import Node
from Models.SudokuBoard import SudokuBoard
from Models.Tree import Tree
from Views.GridView import GridView
from Views.SudokuView import SudokuView

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

    def __init__(self):
        self.count = 0

    def make_move(self, board:SudokuBoard):
        return self.back_tracking_search(board)

    def back_tracking_search(self, board:SudokuBoard):
        return self.back_track(board, 0, 0)

    def back_track(self, board:SudokuBoard, row:int, col:int):
        sudokuView = SudokuView()
        # sudokuView.display(board)
        self.count += 1
        # if self.count > 965:
        #     print("")

        if board.is_complete():
            return board

        unusedValues = self.get_unused(board, row)
        emptyCellsInRow = board.get_empty_in_row(row)
        for i in range(0, len(unusedValues)):
            for j in range(0, len(emptyCellsInRow)):
                emptyCellsInRow[j].value = unusedValues[i]
                if self.valid_move(board):
                    if len(emptyCellsInRow) == 1:
                        sudokuView.display(board)
                        col = 0
                        row += 1
                    result = self.back_track(board, row, col+1)
                    if result is not None and self.valid_move(result):
                        return result

                emptyCellsInRow[j].value = " "

        return None

    def valid_move(self, board:SudokuBoard):
        for i in range(0, 9):
            if self.all_different(board.get_row(i)) == False:
                return False

        for i in range(0, 9):
            if self.all_different(board.get_column(i)) == False:
                return False

        if self.all_different(board.cells) == False:
            return False

        return True

    def all_different(self, lst:list):
        seen = []
        for i in range(0, len(lst)):
            #ignore empty cells
            if lst[i] == " ":
                continue

            if lst[i] in seen:
                return False
            else:
                seen.append(lst[i])

        return True

    def get_unused(self, board:SudokuBoard, row:int):
        domain = ["1","2","3","4","5","6","7","8","9"]
        boardRow = board.get_row(row)
        results = []
        for i in range(0, 9):
            if domain[i] not in boardRow:
                results.append(domain[i])

        return results

    def has_goal(self, board:Grid, team:str):
        return False