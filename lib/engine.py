from player_random import RandomPlayer
from player_matti_basic_ai import PlayerMattiBasicAI

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
        print self.__board
        while self.__running:
            player, symbol = self._get_player()
            cell = player.next_move(symbol, self.__board)
            cell.symbol = symbol
            print self.__board
            if self.__board.check_win_conditions(symbol):
                print "Winner: %s at round: %d" % (symbol, self.__round)
                self.__running = False
            self.__round += 1


def main():
    player1 = PlayerMattiBasicAI()
    player2 = RandomPlayer()
    engine = Engine(player1, player2)
    engine.run()

if __name__ == '__main__':
    main()
