
from Models.Agents.Agent import Agent
from Models.Cell import Cell
from Models.Grid import Grid
from Views.GridView import GridView
from Views.StartView import StartView

class MainController:

    coords = ["0,0", "0,1", "0,2", "1,0", "1,1", "1,2", "2,0", "2,1", "2,2"]

    def __init__ (self, startView:StartView, gridView:GridView, grid:Grid, agentX:Agent):
        self.startView = startView
        self.gridView = gridView
        self.agentX = agentX
        self.defaultStartState = grid

    # starts the program
    def run(self):
        return self.agentX.make_move(self.defaultStartState)

    # verify the user input for a move is allowed
    def varify_coords(self, coords:str, gameState:Grid):
        coords = coords.replace(" ", "").strip()
        
        if len(coords) < 3:
            return False

        try:
            int(coords[0])
            int(coords[2])
        except ValueError or IndexError:
            return False

        if int(coords[0]) >= 0 and int(coords[0]) <= 2 and int(coords[2]) >=0 and int(coords[2]) <= 2:
            cell = self.get_xy(coords)
            cell = gameState.getCell(cell.xPos, cell.yPos)
            if cell.value == 'o' or cell.value == 'x':
                return False
            else: 
                return True

        return False

    # extract coordinates from user input
    def get_xy(self, coords:str):
        coords = coords.replace(" ", "")
        cell = Cell(int(coords[0]), int(coords[2]), " ")
        return cell

    # have user input desired play
    def get_player_move(self, gameState:Grid):
        coords = self.startView.get_input("Enter coorinates for move:")
        while self.varify_coords(coords, gameState) == False:
            self.startView.print_message("invalid formant or occupid cell. Try again")
            coords = self.startView.get_input("Enter coorinate for move:")
        
        return self.get_xy(coords)


