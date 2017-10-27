import random


class RandomPlayer(object):
    def get_move(self, player, board):
        free_positions = []
        for y in xrange(15):
            for x in xrange(15):
                if board[15*y+x] == ' ':
                    free_positions.append((x, y))

        if free_positions:
            return random.choice(free_positions)

        raise ValueError("Board is full")

