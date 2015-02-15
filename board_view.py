from abc import ABCMeta, abstractmethod


class BoardView(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def announce_winner(self, winner):
        pass

    @abstractmethod
    def announce_turn(self, turn):
        pass
