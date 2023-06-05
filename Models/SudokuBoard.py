from Models.Cell import Cell
from Models.Grid import Grid

class SudokuBoard:

    def __init__(self, grids:list, rows:int, columns:int):
        self.rows = rows
        self.columns = columns
        self.cells = grids
        self.SIZE = rows * columns
        k = 0

    # finds the cell at a given row column combination
    # @param row: row of cell wanted
    # @param column: column of cell wanted
    # @returns: cell at specified location
    def get_grid(self, row:int, column:int) -> Grid:
        for i in range(0,len(self.cells)):
            if self.cells[i].xPos == row and self.cells[i].yPos == column:
                return self.cells[i]

    def get_cell(self, row:int, column:int) -> Cell:
        grid = self.get_grid(self.convert(row), self.convert(column))
        return grid.getCell(grid.rows-self.convert_row(row)-1, self.convert_row(column))

    # creates a copy of the grid
    # @returns: new grid with the same cell/value sequence
    def copy(self):
        values = []
        for i in range(0, self.SIZE):
            values.append(self.cells[i].value)

        copy = Grid(values)
        return copy
    
    # finds all the neighbours of the specified cell
    # @param cell: cell to get the neighbours of
    # @returns: collection of neighbours
    def get_cell_neighbours(self, cell:Cell):
        cells = []
        up = self.getCell(cell.xPos + 1, cell.yPos)
        right = self.getCell(cell.xPos, cell.yPos + 1)
        down = self.getCell(cell.xPos - 1, cell.yPos)
        left = self.getCell(cell.xPos, cell.yPos - 1)
        up_right = self.getCell(cell.xPos + 1, cell.yPos + 1)
        down_right = self.getCell(cell.xPos - 1, cell.yPos + 1)
        up_left = self.getCell(cell.xPos - 1, cell.yPos - 1)
        down_left = self.getCell(cell.xPos + 1, cell.yPos - 1)

        if(up != None):
            cells.append(up)

        if(right != None):
            cells.append(right)

        if(down != None):
            cells.append(down)

        if(left != None):
            cells.append(left)

        if(up_right != None):
            cells.append(up_right)

        if(down_right != None):
            cells.append(down_right)

        if(down_left != None):
            cells.append(down_left)

        if(up_left != None):
            cells.append(up_left)

        return cells
    
    # retuns a list of all values in a given row
    # @param row: the row to get values from
    # returns: list of values in given row
    def get_row(self, row:int):
        lst = []
        for i in range(0, self.columns):
            grid = self.get_grid(self.convert(row), i)
            for j in range(0, grid.columns):
                x = self.convert_row(row)
                lst.append(grid.getCell(grid.rows-x-1, j).value)

        return lst

    # retuns a list of all values in a given column
    # @param column: the column to get values from
    # returns: list of values in given column
    def get_column(self, column:int):
        lst = []
        for i in range(0, self.rows):
            grid = self.get_grid(i, self.convert(column))
            for j in range(0, grid.rows):
                lst.append(grid.getCell(grid.rows -1-j, self.convert_row(column)).value)

        return lst

    def get_empty(self) ->list[Cell]:
        empty = []
        for i in range(0, 9):
            for j in range(0, 9):
                if self.cells[i].cells[j].value == " ":
                    empty.append(self.cells[i].cells[j])

        return empty

    def get_grid_with_cell(self, cell:Cell):
        for i in range(0, 9):
            if cell in self.cells[i].cells:
                return self.cells[i]

    def is_complete(self):
        for i in range(0, len(self.cells)):
            if len(self.cells[i].get_empty_cells()) > 0:
                return False
        
        return True

    def convert(self, num:int):
        if num == 0 or num ==1 or num ==2:
            return 0
        elif num == 3 or num ==4 or num ==5:
            return 1
        elif num == 6 or num ==7 or num ==8:
            return 2

    def convert_row(self, num:int):
        if num == 0 or num ==3 or num ==6:
            return 0
        elif num == 1 or num ==4 or num ==7:
            return 1
        elif num == 2 or num ==5 or num ==8:
            return 2
