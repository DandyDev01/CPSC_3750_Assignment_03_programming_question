from Models.Grid import Grid
from Models.Node import Node

class Tree:
    def __init__(self, root:Node):
        self.root = root

    def add_child(self, child:Node, parent:Node):
        parent.add_child(child)
        child.parent = parent

    def clear(self):
        self.root.children.clear()