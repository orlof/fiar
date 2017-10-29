from player import Player


class TerminalPlayer(Player):
    def next_move(self, symbol, board):
        free = board.get_free_cells()
        if not free:
            raise ValueError("Board is full")

        while True:
            print("Give 'x,y' for next '%s': " % symbol)
            pos = input("> ")
            x, y = self.parse_pos(pos)
            if (x, y) in free:
                return x, y

            print("Illegal position")

    @staticmethod
    def parse_pos(token):
        try:
            pos = tuple(map(int, token.split(",")))
            if len(pos) == 2:
                return pos
        except ValueError:
            pass

        return None
