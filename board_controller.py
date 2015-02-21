

class BoardController(object):
    """A controller for a TicTacToe board"""

    def __init__(self):
        """Initializes a new board controller with a board and view"""

        self.current_turn = None
        self.board = None
        self.view = None
        self.winner = None

    def set_board(self, board):
        """Docstring"""
        self.board = board

    def set_view(self, view):
        """Docstring"""
        self.view = view

    def start_game(self):
        """Begins a new game of TicTacToe"""

        self.current_turn = 'x'
        self.view.set_turn(self.current_turn)
        self.board.reset()

    def on_cell_select(self, r, c):
        """Determines what action to take when a board cell is selected."""

        if self.current_turn == 'x':
            if self.board.add_x(r, c):
                self.view.set_x(r - 1, c - 1)
                self.current_turn = 'o'
                self.view.set_turn('o')
            else:
                self.view.show_invalid_cell_msg()
        elif self.current_turn == 'o':
            if self.board.add_o(r, c):
                self.view.set_o(r - 1, c - 1)
                self.current_turn = 'x'
                self.view.set_turn('x')
            else:
                self.view.show_invalid_cell_msg()

        winner = self.board.check_for_win()

        if winner:
            self.view.show_victory_msg(winner)

        elif self.board.check_for_stalemate():
            self.view.show_stalemate_msg()
