from Models.SudokuBoard import SudokuBoard

class SudokuView:
    def display(self, board:SudokuBoard):
        for i in range(0, 9):
            print(board.get_row(i))

        print("\n\n")