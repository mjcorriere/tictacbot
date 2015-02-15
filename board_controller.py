

class BoardController(object):
    """Docstring"""

    def __init__(self, board, view):
        """Docstring"""
        self.current_turn = None
        self.board = board
        self.view = view
        self.winner = None

    def start_game(self):
        """Docstring"""
        self.current_turn = 'x'
        self.view.set_turn(self.current_turn)
        self.board.reset()

    def on_cell_select(self, r, c):
        """Docstring"""
        if self.current_turn == 'x':
            if self.board.add_x(r, c):
                self.current_turn = 'o'
                self.view.set_turn('o')
            else:
                self.view.show_invalid_cell_msg()
        elif self.current_turn == 'o':
            if self.board.add_o(r, c):
                self.current_turn = 'x'
                self.view.set_turn('x')
            else:
                self.view.show_invalid_cell_msg()

    def check_for_win(self):
        """Docstring"""
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
        # TODO: Write in terms of board.width
        if board[0] == board[4] == board[8] and board[0] != '-':
            self.winner = board[0]

        elif board[2] == board[4] == board[6] and board[2] != '-':
            self.winner = board[2]

        return self.winner                

    def check_for_stalemate(self):
        """Docstring"""

        result = False
        if '-' not in self.board.to_string():
            return True
        return result