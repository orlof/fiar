SYMBOLS = "XO"


class Player(object):
    def get_next_move(self, player, board):
        raise NotImplemented("Interface not implemented")

    def get_free_positions(self, board):
        free_positions = []
        for y in xrange(15):
            for x in xrange(15):
                if board[15*y+x] not in SYMBOLS:
                    free_positions.append((x, y))

        return free_positions
