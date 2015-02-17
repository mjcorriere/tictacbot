from abc import ABCMeta, abstractmethod


class BoardView(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def set_turn(self, token):
        pass

    @abstractmethod
    def show_invalid_cell_msg(self):
        pass

    @abstractmethod
    def show_victory_msg(self, victor):
        pass

    @abstractmethod
    def show_stalemate_msg(self):
        pass
