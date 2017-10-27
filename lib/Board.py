from RandomPlayer import SYMBOLS


class Board(object):
    def check_winner(self, board):
        board = list(board)

        for y in xrange(15):
            for x in xrange(15):
                symbol = board[15*y+x]
                if symbol in SYMBOLS:
                    if (self.check(board, symbol, x, y, 0, -1) or self.check(board, symbol, x, y, 1, -1) or
                        self.check(board, symbol, x, y, 0,  1) or self.check(board, symbol, x, y, 0,  1)):
                        return symbol

        return None

    def check(self, board, symbol, x, y, dx, dy):
        if not (0 <= (x + 5*dx) <= 15) or not (0 <= (y + 5*dy) <= 15):
            return False

        for d in xrange(1, 5):
            if board[15*((y+d*dy)) + x + d*dx] != symbol:
                return False

        return True
