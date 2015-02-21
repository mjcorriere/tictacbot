

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

    def check_for_win(self):
        """
        Checks to see if either player has won. Returns the token of the
        winning player, or None if no one has won.
        """
        # TODO: have check_for_win and check_for_stalemate return similar types
        # TODO: Move code back to the board model.
        width = self.board.width
        board = self.board.to_string()

        for i in xrange(width):
            # Horizontals
            # '@@@------'
            # '---@@@---'
            # '------@@@'
            if board[0 + i * width] == \
                    board[1 + i * width] == \
                    board[2 + i * width] and board[0 + i * width] != '-':
                self.winner = board[0 + i * width]
                break

            # Verticals
            # '@--@--@--'
            # '-@--@--@-'
            # '--@--@--@'
            elif board[0 + i] == \
                    board[1 * width + i] == \
                    board[2 * width + i] and board[0 + i * width] != '-':
                self.winner = board[0 + i]
                break

        # Diagonals
        # '@---@---@'
        # '--@-@-@--'
        # TODO: Write in terms of board.width.
        if board[0] == board[4] == board[8] and board[0] != '-':
            self.winner = board[0]

        elif board[2] == board[4] == board[6] and board[2] != '-':
            self.winner = board[2]

        if self.winner is not None:
            self.view.show_victory_msg(self.winner)

        return self.winner

    def check_for_stalemate(self):
        """
        Checks to see if there is a stalemate. Returns True if a stalemate
        is detected, False otherwise.
        """
        # TODO: Move this to the board model.
        result = False
        if '-' not in self.board.to_string():
            self.view.show_stalemate_msg()
            return True
        return result