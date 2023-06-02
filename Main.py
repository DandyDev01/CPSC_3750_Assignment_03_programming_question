from Controllers.MainController import MainController
from Models.Agents.Agent import Agent
from Views.GridView import GridView
from Views.StartView import StartView

initialState = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

agentX = Agent("x")
agentO = Agent("o")
startView = StartView()
gridView = GridView()
mainController = MainController(startView, gridView, initialState, agentX, agentO)

mainController.run()

# [o][x][x]

# [x][o][x]

# [o][x][o]1
