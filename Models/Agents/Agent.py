from Models.Grid import Grid
from Models.SudokuBoard import SudokuBoard
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
        return self.back_track(board)

    def back_track(self, board:SudokuBoard):
        sudokuView = SudokuView()
        if board.is_complete():
            return board

        empty = board.get_empty()
        for i in range(0, len(empty)):
            domainOfCell, cell = self.get_cell_with_smallest_domain(board)
            grid = board.get_grid_with_cell(cell)
            print("domain size:" + str(len(domainOfCell)))
            for j in range(0, len(domainOfCell)):
                cell.value = domainOfCell[j]
                if self.valid_move(board, grid):
                    result = self.back_track(board)
                    sudokuView.display(board)
                    if result is not None and self.valid_move(result):
                        return result

            return None

    def get_cell_with_smallest_domain(self, board:SudokuBoard):
        pair = [0, 0]
        domain = self.most_constrained_variable_values(board, pair[0], pair[1])
        shortestLength = len(domain)
        for i in range(0, 9):
            for j in range(0, 9):
                if board.get_cell(i,j).value != " ":
                    continue

                temp = self.most_constrained_variable_values(board, i, j)
                if len(temp) < shortestLength:
                    pair[0] = i
                    pair[1] = j
                    domain = temp
                    shortestLength = len(self.most_constrained_variable_values(board, pair[0], pair[1]))

        return domain, board.get_cell(pair[0], pair[1])

    def get_col(self, gridPos:int, cellPos:int) -> int:
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

    def valid_move(self, board:SudokuBoard, grid:Grid) -> bool:
        for i in range(0, 9):
            if self.all_different(board.get_row(i)) == False:
                return False

        for i in range(0, 9):
            if self.all_different(board.get_column(i)) == False:
                return False

        if self.all_different(grid.cells) == False:
            return False

        return True

    def all_different(self, lst:list) -> bool:
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

    def get_unused_in_row(self, board:SudokuBoard, row:int) -> list[str]:
        domain = ["1","2","3","4","5","6","7","8","9"]
        boardRow = board.get_row(row)
        results = []
        for i in range(0, 9):
            if domain[i] not in boardRow:
                results.append(domain[i])

        return results

    def get_unused_in_column(self, board:SudokuBoard, col:int) ->list[str]:
        domain = ["1","2","3","4","5","6","7","8","9"]
        boardCol = board.get_column(col)
        results = []
        for i in range(0, 9):
            if domain[i] not in boardCol:
                results.append(domain[i])

        return results

    def get_unused_in_cell(self, board:SudokuBoard, row:int, col:int) -> list[str]:
        grid = board.get_grid(row, col)
        domain = ["1","2","3","4","5","6","7","8","9"]
        results = []
        for i in range(0, 9):
            if domain[i] not in grid.get_values():
                results.append(domain[i])

        return results

    def most_constrained_variable_values(self, board:SudokuBoard, row:int, col:int) -> list[str]:
        rowSet = set(self.get_unused_in_row(board, row))
        colSet = set(self.get_unused_in_column(board, col))
        cellSet = set(self.get_unused_in_cell(board, board.convert(row), board.convert(col)))
        intersection = rowSet.intersection(colSet).intersection(cellSet)

        return list(intersection)