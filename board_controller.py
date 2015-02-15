

class BoardController(object):

    def __init__(self, board):
        """Docstring"""
        self.current_turn = None
        self.board = board
        self.winner = None

    def start_game(self):
        """Docstring"""
        self.current_turn = 'x'
        self.board.reset()

    def on_cell_select(self, r, c):
        """Docstring"""
        if self.current_turn == 'x':
            if self.board.add_x(r, c):
                self.current_turn = 'o'
        elif self.current_turn == 'o':
            if self.board.add_o(r, c):
                self.current_turn = 'x'

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
                    board[2 + i * width]:
                self.winner = board[0 + i * width]
                break

            # Verticals
            # '@--@--@--'
            # '-@--@--@-'
            # '--@--@--@'
            elif board[0 + i] == \
                    board[1 * width + i] == \
                    board[2 * width + i]:
                self.winner = board[0 + i]
                break

        # Diagonals
        # '@---@---@'
        # '--@-@-@--'
        # TODO: Write in terms of board.width
        if board[0] == board[4] == board[8]:
            self.winner = board[0]

        elif board[2] == board[4] == board[6]:
            self.winner = board[2]

        if self.winner == '-':
            self.winner = None

        return self.winner                
