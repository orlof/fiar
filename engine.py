from RandomPlayer import RandomPlayer
from TerminalPlayer import TerminalPlayer

from board import Board


EVEN = "x"
ODD = "o"


def is_even(value):
    return value % 2 == 0


class Engine(object):
    def __init__(self, player1, player2):
        self.__players = (player1, player2)
        self.__board = Board()
        self.__round = 0
        self.__running = False

    def _get_player(self):
        if is_even(self.__round):
            return (self.__players[0], EVEN)
        else:
            return (self.__players[1], ODD)

    def run(self):
        print "Starting"
        self.__running = True
        while self.__running:
            print self.__board
            player, mark = self._get_player()
            move = player.get_next_move(self.__board.get_board(), mark)
            self.__board.update(move, mark)


def main():
    player1 = TerminalPlayer()
    player2 = RandomPlayer()
    engine = Engine(player1, player2)
    engine.run()

if __name__ == '__main__':
    main()
