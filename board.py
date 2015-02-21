
class Board(object):

    def __init__(self, width=3):
        """
        Initializes a square width x width tic tac toe board with all cells
        empty.
        """

        self.width = width
        self.board = ['-'] * (self.width * self.width)

    def reset(self):
        """Resets the board to empty cells."""
        self.__init__()

    def add_x(self, r, c):
        """
        One-valued row and column to assign an x to. Returns false if
        the cell is already occupied.
        """
        result = False
        index = (r - 1) * self.width + c - 1
        if self.board[index] == '-':
            self.board[index] = 'x'
            result = True

        return result

    def add_o(self, r, c):
        """
        One-valued row and column to assign an o to. Returns false if
        the cell is already occupied
        """

        result = False
        index = (r - 1) * self.width + c - 1
        if self.board[index] == '-':
            self.board[index] = 'o'
            result = True

        return result

    def to_string(self):
        """
        Returns a 9 character string representing the board state.
        A '-' represents an empty cell. 'x' and 'o' represent the obvious.
        """

        return ''.join(self.board)

    def check_for_win(self):
        """
        Checks to see if either player has won. Returns the token of the
        winning player, or None if no one has won.
        """
        # TODO: have check_for_win and check_for_stalemate return similar types
        # TODO: Move code back to the board model.
        width = self.width
        board = self.to_string()
        winner = None

        for i in xrange(width):
            # Horizontals
            # '@@@------'
            # '---@@@---'
            # '------@@@'
            if board[0 + i * width] == \
                    board[1 + i * width] == \
                    board[2 + i * width] and board[0 + i * width] != '-':
                winner = board[0 + i * width]
                break

            # Verticals
            # '@--@--@--'
            # '-@--@--@-'
            # '--@--@--@'
            elif board[0 + i] == \
                    board[1 * width + i] == \
                    board[2 * width + i] and board[0 + i] != '-':
                winner = board[0 + i]
                break

        # Diagonals
        # '@---@---@'
        # '--@-@-@--'
        # TODO: Write in terms of board.width.
        if board[0] == board[4] == board[8] and board[0] != '-':
            winner = board[0]

        elif board[2] == board[4] == board[6] and board[2] != '-':
            winner = board[2]

        return winner

    def check_for_stalemate(self):
        """
        Checks to see if there is a stalemate. Returns True if a stalemate
        is detected, False otherwise.
        """
        # TODO: Move this to the board model.
        result = False
        if '-' not in self.to_string():
            result = True
        return result

    def __repr__(self):
        representation = []
        for i, s in enumerate(self.board):
            if i % self.width == 2:
                representation.extend(list(s + '\n'))
            else:
                representation.extend(s)
        return ''.join(representation)

