
class Board(object):

    def __init__(self):
        self.width = 3
        self.board = ['-'] * (self.width * self.width)

    def reset(self):
        self.__init__()

    def add_x(self, r, c):
        """One-valued row and column to assign an x to"""
        result = False
        index = (r - 1) * self.width + c - 1
        if self.board[index] == '-':
            self.board[index] = 'x'
            result = True

        return result

    def add_o(self, r, c):
        """One-valued row and column to assign an o to"""
        result = False
        index = (r - 1) * self.width + c - 1
        if self.board[index] == '-':
            self.board[index] = 'o'
            result = True

        return result

    def to_string(self):
        return ''.join(self.board)

    def __repr__(self):
        representation = []
        for i, s in enumerate(self.board):
            if i % self.width == 2:
                representation.extend(list(s + '\n'))
            else:
                representation.extend(s)
        return ''.join(representation)

