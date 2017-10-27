import random

SYMBOLS = "XO"

class RandomPlayer(object):
    def get_move(self, player, board):
        free = self.get_free_positions(board)
        if not free:
            raise ValueError("Board is full")

        return random.choice(free)

    def get_free_positions(self, board):
        free_positions = []
        for y in xrange(15):
            for x in xrange(15):
                if board[15*y+x] not in SYMBOLS:
                    free_positions.append((x, y))

        return free_positions
