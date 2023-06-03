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
    def getCell(self, row:int, column:int):
        for i in range(0,len(self.cells)):
            if self.cells[i].xPos == row and self.cells[i].yPos == column:
                return self.cells[i]

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
        list = []
        for i in range(0, self.columns):
            cell = self.getCell(self.convert(row), i)
            for j in range(0, cell.columns):
                x = self.convert_row(row)
                list.append(cell.getCell(cell.rows-x-1, j).value)

        return list

    # retuns a list of all values in a given column
    # @param column: the column to get values from
    # returns: list of values in given column
    def get_column(self, column:int):
        list = []
        for i in range(0, self.rows):
            cell = self.getCell(i, self.convert(column))
            for j in range(0, cell.rows):
                list.append(cell.getCell(cell.rows -1-j, self.convert_row(column)).value)

        return list

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
