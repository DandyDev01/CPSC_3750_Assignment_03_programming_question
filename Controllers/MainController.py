
from Models.Agents.Agent import Agent
from Models.Cell import Cell
from Models.Grid import Grid
from Models.SudokuBoard import SudokuBoard
from Views.GridView import GridView
from Views.StartView import StartView

class MainController:

    def __init__ (self, startView:StartView, gridView:GridView, board:SudokuBoard, agentX:Agent):
        self.startView = startView
        self.gridView = gridView
        self.agentX = agentX
        self.defaultStartState = board

    # starts the program
    def run(self):
        return self.agentX.make_move(self.defaultStartState)


