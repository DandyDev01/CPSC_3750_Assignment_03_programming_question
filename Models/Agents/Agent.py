from Models.Grid import Grid
from Models.SudokuBoard import SudokuBoard
from Views.SudokuView import SudokuView

class Agent:

    def make_move(self, board:SudokuBoard):
        return self.back_tracking_search(board)

    def back_tracking_search(self, board:SudokuBoard):
        return self.back_track(board)

    def back_track(self, board:SudokuBoard):
        if board.is_complete():
            return board

        empty = board.get_empty()
        for i in range(0, len(empty)):
            domainOfCell, cell = self.get_cell_with_smallest_domain(board)

            if len(domainOfCell) == 0:
                return None
            
            grid = board.get_grid_with_cell(cell)
            
            for j in range(0, len(domainOfCell)):
                cell.value = domainOfCell[j]
                # sudokuView = SudokuView()
                # sudokuView.display(board)
                if self.valid_move(board, grid):
                    result = self.back_track(board)
                    if result is not None and self.valid_move(result, grid):
                        return result
            
            cell.value = " "          
        return None

    # gets the cell on the baord that has the smallest domain
    # @param board: the board to get the cell from
    # @returns: domain and cell with said domain respectivly
    def get_cell_with_smallest_domain(self, board:SudokuBoard):
        pair = [0,0]
        domain = []
        shortestLength = 100
        for i in range(0, 9):
            for j in range(0, 9):
                if board.get_cell(i,j).value != " ":
                    continue

                temp = self.most_constrained_variable_values(board, i, j)
                if len(temp) < shortestLength and len(temp) > 0:
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

    # makes sure the board is in a valid form
    # @param board: the board to check
    # @param grid: cell on the board that was changed
    # @returns weather or not the move was valid
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

    # CSP function, makes sure all values in list are the same
    # @param lst: list to make sure all values are unique
    # @returns weather or not all values in given list are unique
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

    # gets all the unused values in the domain of a row
    # @param board: the current board
    # @param row: the row to get unused values for
    def get_unused_in_row(self, board:SudokuBoard, row:int) -> list[str]:
        domain = ["1","2","3","4","5","6","7","8","9"]
        boardRow = board.get_row(row)
        results = []
        for i in range(0, 9):
            if domain[i] not in boardRow:
                results.append(domain[i])

        return results

    # gets all the unused values in the domain of a column
    # @param board: the current board
    # @param col: the column to get unused values for
    def get_unused_in_column(self, board:SudokuBoard, col:int) ->list[str]:
        domain = ["1","2","3","4","5","6","7","8","9"]
        boardCol = board.get_column(col)
        results = []
        for i in range(0, 9):
            if domain[i] not in boardCol:
                results.append(domain[i])

        return results

    # gets all the unused values in the domain of a cell
    # @param board: the current board
    # @param col: the column of the cell on the board
    # @param row: the row of the cell on the board
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