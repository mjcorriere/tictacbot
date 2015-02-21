from board import Board
from board_controller import BoardController
from tk_board_view import TKBoardView

import Tkinter as tk


class TicTacToe(object):
    """A game of TicTacToe"""

    def __init__(self, master):
        """
        Initializes the model, view, and controller in anticipation
        of a new game of TTT
        """
        self.master = master
        self.master.pack_propagate(0)

        self.frame = tk.Frame(master, bg='blue', width=500, height=500)

        self.frame.columnconfigure(0, weight=1, uniform="wtf")
        self.frame.columnconfigure(1, weight=1, uniform="wtf")
        self.frame.columnconfigure(2, weight=1, uniform="wtf")

        self.frame.rowconfigure(0, weight=1, uniform="wtf")
        self.frame.rowconfigure(1, weight=1, uniform="wtf")
        self.frame.rowconfigure(2, weight=1, uniform="wtf")

        self.board = Board()
        self.board_view = TKBoardView(self.frame)
        self.board_controller = BoardController()

        self.board_controller.set_board(self.board)
        self.board_controller.set_view(self.board_view)

        self.board_view.set_controller(self.board_controller)
        self.board_view.set_board(self.board)

        self.frame.pack(fill=tk.BOTH, expand=tk.YES)

    def main(self):
        """Begins the game of TTT and fires the main game loop"""
        self.board_controller.start_game()
        self.master.mainloop()

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
    root = tk.Tk()
    ttt = TicTacToe(root)
    ttt.main()
