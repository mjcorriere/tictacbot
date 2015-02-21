from board_view import BoardView
import Tkinter as tk


class TKBoardView(BoardView):
    """Docstring"""

    def __init__(self, parent):
        """Docstring"""
        self.parent = parent
        self.board = None
        self.controller = None
        self.grid = []

    def set_controller(self, controller):
        """Docstring"""
        self.controller = controller

    def set_board(self, board):
        """Docstring"""
        self.board = board
        self._setup_board()

    def _setup_board(self):
        """Docstring"""
        grid_length = self.board.width * self.board.width
        sticky_value = tk.N + tk.S + tk.E + tk.W

        for _ in xrange(grid_length):
            self.grid.append(tk.Button(self.parent))

        for i, button in enumerate(self.grid):
            width = self.board.width
            r = i / width
            c = i % width

            button.grid(row=r, column=c, sticky=sticky_value)
            button.configure(command=lambda r=r, c=c:
                self.controller.on_cell_select(r+1, c+1))
            button.configure(text='-')

    def set_x(self, r, c):
        i = self.board.width * r + c
        self.grid[i].configure(text='X')

    def set_o(self, r, c):
        i = self.board.width * r + c
        self.grid[i].configure(text='O')

    def draw(self):
        pass

    def set_turn(self, token):
        pass

    def show_invalid_cell_msg(self):
        pass

    def show_victory_msg(self, victor):
        pass

    def show_stalemate_msg(self):
        pass

