from RandomPlayer import RandomPlayer


class TerminalPlayer(RandomPlayer):
    def get_move(self, player, board):
        free = self.get_free_positions(board)
        if not free:
            raise ValueError("Board is full")


