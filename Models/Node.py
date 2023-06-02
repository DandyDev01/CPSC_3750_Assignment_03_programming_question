from Models.Grid import Grid

class Node:
    def __init__ (self, grid:Grid):
        self.grid = grid
        self.score = 0
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self