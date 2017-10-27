from player import Player


class TerminalPlayer(Player):
    def get_next_move(self, player, board):
        free = self.get_free_positions(board)
        if not free:
            raise ValueError("Board is full")

        while True:
            print "Give 'x,y' for next '%s': " % player
            pos = raw_input("> ")
            x, y = self.parse_pos(pos)
            if (x, y) in free:
                return x, y

            print "Illegal position"

    @staticmethod
    def parse_pos(token):
        try:
            pos = tuple(map(int, token.split(",")))
            if len(pos) == 2:
                return pos
        except ValueError:
            pass

        return None
