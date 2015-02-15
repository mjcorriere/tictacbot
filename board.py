
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

    def __repr__(self):
        representation = []
        for i, s in enumerate(self.board):
            if i % self.width == 2:
                representation.extend(list(s + '\n'))
            else:
                representation.extend(s)
        return ''.join(representation)

