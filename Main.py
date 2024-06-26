from Controllers.MainController import MainController
from Models.Agents.Agent import Agent
from Models.Grid import Grid
from Models.SudokuBoard import SudokuBoard
from Views.StartView import StartView
from Views.SudokuView import SudokuView

# grid1State = [" ", " ", "1", 
#               "9", " ", " ", 
#               " ", " ", "3"]
# grid2State = ["8", " ", "6", 
#               "3", " ", "5",
#               " ", "2", " "]
# grid3State = ["4", " ", " ",
#               " ", " ", "1",  
#               "6", " ", " "]
# grid4State = [" ", " ", "6", 
#               "7", " ", " ", 
#               " ", " ", "8"]
# grid5State = ["7", " ", "8", 
#               " ", " ", " ", 
#               "1", " ", "2"]
# grid6State = ["2", " ", " ", 
#               " ", " ", "8", 
#               "9", " ", " "]
# grid7State = [" ", " ", "5", 
#               "8", " ", " ", 
#               " ", " ", "2"]
# grid8State = [" ", "1", " ", 
#               "2", " ", "3", 
#               "6", " ", "9"]
# grid9State = ["3", " ", " ", 
#               " ", " ", "9", 
#               "5", " ", " "]

# grid1State = [" ", " ", " ", 
#               "2", " ", " ", 
#               " ", " ", "7"]
# grid2State = [" ", " ", "7", 
#               " ", "6", " ",
#               "4", "9", "1"]
# grid3State = [" ", "1", " ",
#               "3", " ", "9",  
#               "6", " ", "5"]
# grid4State = [" ", " ", "6", 
#               " ", " ", "3", 
#               " ", "5", "8"]
# grid5State = ["2", " ", " ", 
#               " ", " ", " ", 
#               "6", " ", " "]
# grid6State = ["1", "8", "7", 
#               " ", "9", " ", 
#               " ", " ", "4"]
# grid7State = ["8", "1", " ", 
#               "6", "7", " ", 
#               "9", " ", "4"]
# grid8State = [" ", "4", "5", 
#               "8", "3", " ", 
#               " ", "7", " "]
# grid9State = [" ", " ", " ", 
#               " ", " ", " ", 
#               " ", " ", "2"]

grid1State = ["1", "9", " ", 
              "6", "8", " ", 
              " ", " ", " "]

grid2State = [" ", " ", "4", 
              " ", "7", " ", 
              "2", "6", " "]

grid3State = ["5", " ", " ", 
              " ", "9", " ", 
              "7", " ", "1"]

grid4State = [" ", "5", " ", 
              " ", " ", "4", 
              "8", "2", " "]

grid5State = [" ", " ", "3", 
              "6", " ", "2", 
              "1", " ", " "]

grid6State = [" ", "2", "8", 
              "9", " ", " ", 
              " ", "4", " "]

grid7State = ["7", " ", "3", 
              " ", "4", " ", 
              " ", " ", "9"]

grid8State = [" ", "1", "8", 
              " ", "5", " ", 
              "3", " ", " "]

grid9State = [" ", " ", " ", 
              " ", "3", "6", 
              " ", "7", "4"]


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

mainController.run()

# [ ][ ][3]

# [9][ ][ ]

# [ ][ ][1]

#205