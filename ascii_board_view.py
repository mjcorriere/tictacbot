from board_view import BoardView
import os


class ASCIIBoardView(BoardView):

    def __init__(self, board=None):
        self.board = board

    def set_board(self, board):
        self.board = board

    def draw(self):
        representation = []
        string = self.board.to_string()
        for i, c in enumerate(string):
            if i % 3 == 2:
                representation.extend(list(c + '\n'))
            else:
                representation.extend(c)
        clear_command = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear_command)
        print ''.join(representation)

    def announce_turn(self, turn):
        pass

    def announce_winner(self, winner):
        pass
