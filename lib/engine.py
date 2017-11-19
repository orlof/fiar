from ai_antti import AiAntti
from ai_berit import AiBerit
from ai_celia import AiCelia
from player_random import RandomPlayer
from player_matti_basic_ai import PlayerMattiBasicAI
import argparse

from board import Board, EVEN, ODD, EMPTY


args = None


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
            return self.__players[0], EVEN
        else:
            return self.__players[1], ODD

    def run(self):
        print("Starting")

        self.__players[0].start_game(EVEN)
        self.__players[1].start_game(ODD)

        if args.view:
            print(self.__board)

        self.__running = True

        while self.__running:
            player, symbol = self._get_player()
            cell = player.next_move(self.__board)
            cell.symbol = symbol

            if args.view:
                print(self.__board)

            if self.__board.check_win_conditions():
                print("Winner: %s at round: %d" % (symbol, self.__round))
                self.__running = False

            self.__round += 1
            if self.__round == self.__board.get_board_range():
                print("Draw at round: %d" % self.__round)
                symbol = EMPTY
                self.__running = False

        if not args.view:
            print(self.__board)

        self.__players[0].end_game(symbol == EVEN, self.__board)
        self.__players[1].end_game(symbol == ODD, self.__board)

        return self.__round, symbol


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rounds", default=1, help="how many rounds to play", type=int)
    parser.add_argument('--no-view', dest='view', action='store_false')
    parser.set_defaults(view=True)

    global args
    args = parser.parse_args()


def main():
    parse_arguments()

    stats = {EVEN: 0, ODD: 0}
    for r in range(args.rounds):
        player1 = PlayerMattiBasicAI()
        player2 = AiCelia()
        # player1 = RandomPlayer()
        # player2 = AiCelia()
        engine = Engine(player1, player2)
        game_len, winner = engine.run()
        stats[winner] = stats[winner]+1

    print(stats)


if __name__ == '__main__':
    main()
