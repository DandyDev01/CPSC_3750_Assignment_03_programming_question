from Models.Grid import Grid


class GridView:
    def display(self, grid:Grid):
        for i in range(0, grid.rows):
            for j in range(0, grid.columns):
                value = str(grid.getCell(grid.rows - 1- i, j).value)
                if grid.columns - j == 1:
                    print("[" + value + "]", end="")
                    print("\n")
                else:
                    print("[" + value + "]", end="")

        print("=====================")