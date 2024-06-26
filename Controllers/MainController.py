
from Models.Agents.Agent import Agent
from Models.SudokuBoard import SudokuBoard
from Views.StartView import StartView
from Views.SudokuView import SudokuView

class MainController:

    def __init__ (self, startView:StartView, sudokuView:SudokuView, board:SudokuBoard, agentX:Agent):
        self.startView = startView
        self.sudokuView = sudokuView
        self.agentX = agentX
        self.defaultStartState = board

    # starts the program
    def run(self):
        self.sudokuView.display(self.defaultStartState)

        result =  self.agentX.make_move(self.defaultStartState)

        if result is None:
            self.startView.print_message("no solution found")
            return

        self.sudokuView.display(result)


