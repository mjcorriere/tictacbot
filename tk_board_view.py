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
        self.status_label = None

    def set_controller(self, controller):
        """Docstring"""
        self.controller = controller

    def set_board(self, board):
        """Docstring"""
        self.board = board
        self._setup_board()

    def _setup_board(self):
        """Docstring"""
        width = self.board.width
        grid_length = width * width
        sticky_value = tk.N + tk.S + tk.E + tk.W

        for _ in xrange(grid_length):
            self.grid.append(tk.Button(self.parent))

        for i, button in enumerate(self.grid):

            r = i / width
            c = i % width

            button.grid(row=r, column=c, sticky=sticky_value)
            button.configure(command=lambda r=r, c=c:
                self.controller.on_cell_select(r+1, c+1))
            button.configure(text='-')

        self.status_label = tk.Label(self.parent, text="OMFG")
        self.status_label.grid(row=width+1, column=0, columnspan=width,
                               sticky=tk.W)

    def set_x(self, r, c):
        i = self.board.width * r + c
        self.grid[i].configure(text='X')

    def set_o(self, r, c):
        i = self.board.width * r + c
        self.grid[i].configure(text='O')

    def draw(self):
        pass

    def set_turn(self, token):
        message = "Turn: " + token
        self.status_label.configure(text=message)

    def show_invalid_cell_msg(self):
        message = "Invalid cell"
        self.status_label.configure(text=message)

    def show_victory_msg(self, victor):
        message = victor + " wins! Congratulations!"
        self.status_label.configure(text=message)

    def show_stalemate_msg(self):
        message = "Draw!"
        self.status_label.configure(text=message)

