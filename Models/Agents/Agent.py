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
        return self.back_track(board, 0)

    def back_track(self, board:SudokuBoard, row:int):
        # print(self.get_unused_in_row(board, 0))
        # print(self.get_unused_in_column(board, 0))
        # print(self.get_unused_in_cell(board, board.convert(0), board.convert(0)))
        # print(self.most_constrained_variable_values(board, 0, 0))
        sudokuView = SudokuView()
        # sudokuView.display(board)
        self.count += 1
        # if self.count > 965:
        #     print("")

        if board.is_complete():
            return board

        # unusedValues = self.most_constrained_variable_values(board, row, 0)
        emptyCellsInRow = board.get_empty_in_row(row)
        
        if len(emptyCellsInRow) == 0:
                # sudokuView.display(board)
                return self.back_track(board, row + 1)

        if board.get_cell(0, 7).value == "5" and board.get_cell(0, 8).value == "7":
            print()

        for i in range(0, len(emptyCellsInRow)):
            grid = board.get_grid_with_cell(row, emptyCellsInRow[i])
            col = self.get_col(grid.yPos, emptyCellsInRow[i].yPos)
            domainOfCell = self.most_constrained_variable_values(board, row, col)
            for j in range(0, len(domainOfCell)):
                emptyCellsInRow[i].value = domainOfCell[j]
                if self.valid_move(board, grid):
                    result = self.back_track(board, row)
                    sudokuView.display(board)
                    if result is not None and self.valid_move(result):
                        return result

                emptyCellsInRow[i].value = " "

        return None

        # for i in range(0, len(unusedValues)):
        #     for j in range(0, len(emptyCellsInRow)):
        #         emptyCellsInRow[j].value = unusedValues[i]
        #         if self.valid_move(board):
        #             if len(emptyCellsInRow) == 0:
        #                 sudokuView.display(board)
        #                 row += 1
        #             result = self.back_track(board, row, col+1)
        #             if result is not None and self.valid_move(result):
        #                 return result

        #         emptyCellsInRow[j].value = " "

        # return None

    def get_col(self, gridPos:int, cellPos:int):
        if gridPos == 0 and cellPos == 0:
            return 0
        elif gridPos == 0 and cellPos == 1:
            return 1
        elif gridPos == 0 and cellPos == 2:
            return 2
        elif gridPos == 1 and cellPos == 0:
            return 3
        elif gridPos == 1 and cellPos == 1:
            return 4
        elif gridPos == 1 and cellPos == 2:
            return 5
        elif gridPos == 2 and cellPos == 0:
            return 6
        elif gridPos == 2 and cellPos == 1:
            return 7
        elif gridPos == 2 and cellPos == 2:
            return 8

    def valid_move(self, board:SudokuBoard, grid:Grid):
        for i in range(0, 9):
            if self.all_different(board.get_row(i)) == False:
                return False

        for i in range(0, 9):
            if self.all_different(board.get_column(i)) == False:
                return False

        if self.all_different(grid.cells) == False:
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

    def get_unused_in_row(self, board:SudokuBoard, row:int):
        domain = ["1","2","3","4","5","6","7","8","9"]
        boardRow = board.get_row(row)
        results = []
        for i in range(0, 9):
            if domain[i] not in boardRow:
                results.append(domain[i])

        return results

    def get_unused_in_column(self, board:SudokuBoard, col:int):
        domain = ["1","2","3","4","5","6","7","8","9"]
        boardCol = board.get_column(col)
        results = []
        for i in range(0, 9):
            if domain[i] not in boardCol:
                results.append(domain[i])

        return results

    def get_unused_in_cell(self, board:SudokuBoard, row:int, col:int):
        grid = board.get_grid(row, col)
        domain = ["1","2","3","4","5","6","7","8","9"]
        results = []
        for i in range(0, 9):
            if domain[i] not in grid.get_values():
                results.append(domain[i])

        return results


    def most_constrained_variable_values(self, board:SudokuBoard, row:int, col:int):
        rowSet = set(self.get_unused_in_row(board, row))
        colSet = set(self.get_unused_in_column(board, col))
        cellSet = set(self.get_unused_in_cell(board, board.convert(row), board.convert(col)))
        intersection = rowSet.intersection(colSet).intersection(cellSet)

        return list(intersection)