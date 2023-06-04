from Controllers.MainController import MainController
from Models.Agents.Agent import Agent
from Models.Grid import Grid
from Models.SudokuBoard import SudokuBoard
from Views.GridView import GridView
from Views.StartView import StartView
from Views.SudokuView import SudokuView

# grid1State = [" ", " ", "1", "9", " ", " ", " ", " ", "3"]
# grid2State = ["8", " ", "6", "3", " ", "4", " ", "2", " "]
# grid3State = ["4", " ", " ", " ", " ", "1", "6", " ", " "]
# grid4State = [" ", " ", "6", "7", " ", " ", " ", " ", "8"]
# grid5State = ["7", " ", "8", " ", " ", " ", "1", " ", "2"]
# grid6State = ["2", " ", " ", " ", " ", "8", "9", " ", " "]
# grid7State = [" ", " ", "5", "8", " ", " ", " ", " ", "2"]
# grid8State = [" ", "1", " ", "2", " ", "3", "6", " ", "9"]
# grid9State = ["3", " ", " ", " ", " ", "9", "5", " ", " "]

grid1State = ["2", " ", "1", "9", " ", " ", "4", "8", "3"]
grid2State = ["8", " ", "6", "3", "4", "5", " ", "2", " "]
grid3State = ["4", " ", "3", " ", "2", "1", "6", "5", " "]
grid4State = ["1", "3", "6", "7", "2", "9", "5", "4", "8"]
grid5State = ["7", "9", "8", "5", "6", "4", "1", " ", "2"]
grid6State = ["2", "4", " ", "1", "3", "8", "9", " ", " "]
grid7State = ["6", " ", "5", "8", " ", "4", "3", "7", "2"]
grid8State = ["4", "1", " ", "2", " ", "3", "6", "8", "9"]
grid9State = ["3", " ", "2", " ", " ", "9", "5", " ", " "]

grid = Grid(grid1State, 3, 3, 0, 0)
grid2 = Grid(grid2State, 3, 3, 0, 1)
grid3 = Grid(grid3State, 3, 3, 0, 2)
grid4 = Grid(grid4State, 3, 3, 1, 0)
grid5 = Grid(grid5State, 3, 3, 1, 1)
grid6 = Grid(grid6State, 3, 3, 1, 2)
grid7 = Grid(grid7State, 3, 3, 2, 0)
grid8 = Grid(grid8State, 3, 3, 2, 1)
grid9 = Grid(grid9State, 3, 3, 2, 2)

grids = [grid, grid2, grid3, grid4, grid5, grid6, grid7, grid8, grid9]

sudokuBoard = SudokuBoard(grids, 3, 3)

agentX = Agent()
startView = StartView()
sudokuView = SudokuView()
mainController = MainController(startView, sudokuView, sudokuBoard, agentX)

cells = sudokuBoard.get_empty_in_row(0)
for i in range(0, len(cells)):
    print(cells[i].value, end="")

mainController.run()

# [ ][ ][3]

# [9][ ][ ]

# [ ][ ][1]

#205