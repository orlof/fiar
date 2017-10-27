from player import Player

import random


class RandomPlayer(Player):
    def get_next_move(self, player, board):
        free = self.get_free_positions(board)
        if not free:
            raise ValueError("Board is full")

        return random.choice(free)
