from player import Player

import random


class RandomPlayer(Player):
    def next_move(self, symbol, board):
        free = board.get_free_cells()
        if not free:
            raise ValueError("Board is full")

        return random.choice(free)
