from board import Board
from board_controller import BoardController
from ascii_board_view import ASCIIBoardView


class TicTacToe(object):
    """Docstring"""

    def __init__(self):
        """Docstring"""
        self.board = Board()
        self.board_view = ASCIIBoardView(self.board)
        self.board_controller = BoardController(self.board, self.board_view)

    def main(self):
        """Docstring"""
        print 'Welcome to Triple T'

        while True:

            cmd = self._menu_prompt()

            if cmd == 'q':
                break
            elif cmd == 's':
                self._play()

    def _play(self):
        """Docstring"""

        self.board_controller.start_game()
        self.board_view.draw()

        playing = True
        while playing:

            self.handle_input()
            self.board_view.draw()

            if self.check_for_end():
                playing = False

    def check_for_end(self):
        """Docstring"""

        result = False
        winner = self.board_controller.check_for_win()
        stalemate = self.board_controller.check_for_stalemate()

        if winner is not None:
            print 'CONGRATS TO', winner
            result = True

        if stalemate:
            print 'Its a tie!'
            result = True

        return result

    def _menu_prompt(self):
        """Docstring"""

        cmd = ''
        while True:
            cmd = raw_input('(s)tart or (q)uit: ')
            if cmd == 's' or cmd == 'q':
                break

        return cmd

    def handle_input(self):
        """Docstring"""

        current_turn = self.board_controller.current_turn
        print 'Enter row, column (rc):',

        rc = raw_input()
        r = int(rc[0])
        c = int(rc[1])

        self.board_controller.on_cell_select(r, c)

if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.main()

