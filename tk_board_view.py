from board_view import BoardView
import Tkinter as tk

class TKBoardView(BoardView):
    """Docstring"""

    def __init__(self, board, parent):

        self.board = board
        self.parent = parent
        self.setup_board()

    def setup_board(self):

        self.grid = [
            tk.Button(self.parent).grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W),
            tk.Button(self.parent).grid(row=0, column=1, sticky=tk.N+tk.S+tk.E+tk.W),
            tk.Button(self.parent).grid(row=0, column=2, sticky=tk.N+tk.S+tk.E+tk.W),
            tk.Button(self.parent).grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W),
            tk.Button(self.parent).grid(row=1, column=1, sticky=tk.N+tk.S+tk.E+tk.W),
            tk.Button(self.parent).grid(row=1, column=2, sticky=tk.N+tk.S+tk.E+tk.W),
            tk.Button(self.parent).grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W),
            tk.Button(self.parent).grid(row=2, column=1, sticky=tk.N+tk.S+tk.E+tk.W),
            tk.Button(self.parent).grid(row=2, column=2, sticky=tk.N+tk.S+tk.E+tk.W)
        ]

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

