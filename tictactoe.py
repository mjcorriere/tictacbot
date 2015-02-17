from board import Board
from board_controller import BoardController
from ascii_board_view import ASCIIBoardView


class TicTacToe(object):
    """A game of TicTacToe"""

    def __init__(self):
        """
        Initializes the model, view, and controller in anticipation
        of a new game of TTT
        """
        self.board = Board()
        self.board_view = ASCIIBoardView(self.board)
        self.board_controller = BoardController(self.board, self.board_view)

    def main(self):
        """Begins the game of TTT and fires the main game loop"""
        print 'Welcome to Triple T'

        while True:

            cmd = self._menu_prompt()

            if cmd == 'q':
                break
            elif cmd == 's':
                self._play()

    def _play(self):
        """
        The main game loop. Runs indefinitely until the user quits, or the
        end of the game has been reached.
        """

        self.board_controller.start_game()
        self.board_view.draw()

        playing = True
        while playing:

            self._handle_input()
            self.board_view.draw()

            if self._check_for_end():
                playing = False

    def _check_for_end(self):
        """
        Checks to see if the game has ended either by victory or stalemate.
        If either is detected, it displays the correct message and returns
        True.
        """

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
        """
        Prompts the user to start the game or quit. Loops indefinitely
        until a valid selection is made.
        """
        # TODO: Move this to the view.

        cmd = ''
        while True:
            cmd = raw_input('(s)tart or (q)uit: ')
            if cmd == 's' or cmd == 'q':
                break

        return cmd

    def _handle_input(self):
        """
        Handles user input and routes it to the correct controller function.
        """

        print 'Enter row, column (rc):',

        rc = raw_input()
        r = int(rc[0])
        c = int(rc[1])

        self.board_controller.on_cell_select(r, c)

if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.main()

