
from copy import deepcopy
from Models.Agents.Agent import Agent
from Models.Cell import Cell
from Models.Grid import Grid
from Views.GridView import GridView
from Views.StartView import StartView

class MainController:

    coords = ["0,0", "0,1", "0,2", "1,0", "1,1", "1,2", "2,0", "2,1", "2,2"]

    def __init__ (self, startView:StartView, gridView:GridView, defaultInitialState:list, agentX:Agent, agentO:Agent):
        self.startView = startView
        self.gridView = gridView
        self.agentX = agentX
        self.agentO = agentO
        self.defaultStartState = Grid(defaultInitialState)

    # starts the program
    def run(self):
        self.startView.print_message("Welcome to Tic-tac-toe.")
        self.startView.print_message("Enter one of the following.")
        self.startView.print_message("1 - for player vs. AI.")
        self.startView.print_message("2 - for AI vs AI")
        playMode = self.startView.get_input("Select play mode.")

        while not(playMode == "1" or playMode == "2"):
            self.startView.print_message(playMode + " is not a valid input, try again")
            self.startView.print_message("1 - for player vs. AI.")
            self.startView.print_message("2 - for AI vs AI")
            playMode = self.startView.get_input("Select play mode.")

        gameState = self.defaultStartState
        
        self.gridView.display(gameState)

        if playMode == "1":
            self.player_vs_AI(gameState)
        elif playMode == "2":
            self.AI_vs_AI(gameState)

    # plays game with user vs. AI
    def player_vs_AI(self, gameState:Grid):
        coordinateGrid = Grid(self.coords)
        self.startView.print_message("Enter coordinates in the form (x, y)")
        self.startView.print_message("You are on team x")
        self.startView.print_message("This is the coorinate grid")
        self.gridView.display(coordinateGrid)

        while len(gameState.get_empty_cells()) > 0:
            cell = self.get_player_move(gameState)
            deepcopy = gameState.copy()
            deepcopy.getCell(cell.xPos, cell.yPos).value = "x"
            gameState = deepcopy
            self.gridView.display(gameState)
            gameState = self.agentO.make_move(gameState)
            self.gridView.display(gameState)

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

    # plays game with AI vs. AI
    def AI_vs_AI(self, gameState:Grid):
        while len(gameState.get_empty_cells()) > 0:
            gameState = self.agentX.make_move(gameState)
            self.gridView.display(gameState)
            gameState = self.agentO.make_move(gameState)
            self.gridView.display(gameState)

    def check_for_winner(self, agentX:Agent, agentO:Agent, gameState:Grid):
        if agentX.has_goal(gameState, agentX.team):
            return True

        if agentO.has_goal(gameState, agentO.team):
            return True

        return False



