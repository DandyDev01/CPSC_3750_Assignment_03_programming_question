from Models.Cell import Cell

class Grid:
    EMPTY = " "

    def __init__(self, initialState:list, rows:int, columns:int, xPos:int, yPos:int):
        self.xPos = xPos
        self.yPos = yPos
        self.rows = rows
        self.columns = columns
        self.cells = []
        self.SIZE = rows * columns
        k = 0
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                self.cells.append(Cell(i, j, initialState[k]))
                k = k + 1

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
    
    # finds the empty cells
    # @returns: the empty cells
    def get_empty_cells(self):
        emptyCells = []
        for i in range(0, self.SIZE):
            if self.cells[i].value == self.EMPTY:
                emptyCells.append(self.cells[i])
        
        return emptyCells
    
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
            list.append(self.getCell(row, i).value)

        return list

    # retuns a list of all values in a given column
    # @param column: the column to get values from
    # returns: list of values in given column
    def get_column(self, column:int):
        list = []
        for i in range(0, self.rows):
            list.append(self.getCell(i, column))

        return list

    # creates and returns a collection of the values in the same sequence
    #@ returns: collection of the values in the grid
    def get_values(self):
        values = []
        for i in range(0, self.SIZE):
            values.append(self.cells[i].value)

        return values