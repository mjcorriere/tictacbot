from board_view import BoardView
import os


class ASCIIBoardView(BoardView):

    def __init__(self, board=None):
        self.board = board
        self.invalid_cell_msg = 'Cell occupied. Please choose another'
        self.turn_msg = 'Current player:'
        self.turn_token = '-'
        self.invalid_cell_selected = False

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

        if self.invalid_cell_selected:
            print self.invalid_cell_msg
            self.invalid_cell_selected = False

        print self.turn_msg, self.turn_token

    def set_turn(self, token):
        self.turn_token = token

    def show_invalid_cell_msg(self):
        self.invalid_cell_selected = True

