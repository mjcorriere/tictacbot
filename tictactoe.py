from board import Board
from board_controller import BoardController
from ascii_board_view import ASCIIBoardView


class TicTacToe(object):

    def __init__(self):
        self.board = Board()
        self.board_controller = BoardController(self.board)
        self.board_view = ASCIIBoardView(self.board)

    def main(self):

        print 'Welcome to Triple T'

        while True:

            cmd = self.menu_prompt()

            if cmd == 'q':
                break
            elif cmd == 's':
                self.play()

    def play(self):

        self.board_controller.start_game()
        self.board_view.draw()

        playing = True
        while playing:
            self.handle_input()
            self.board_view.draw()
            winner = self.board_controller.check_for_win()

            if winner is not None:
                print 'CONGRATS TO', winner
                playing = False

    def menu_prompt(self):
        cmd = ''
        while True:
            cmd = raw_input('(s)tart or (q)uit: ')
            if cmd == 's' or cmd == 'q':
                break

        return cmd

    def handle_input(self):
        current_turn = self.board_controller.current_turn
        print current_turn, ':',
        rc = raw_input()
        r = int(rc[0])
        c = int(rc[1])
        self.board_controller.on_cell_select(r, c)

if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.main()

