import unittest

from RandomPlayer import RandomPlayer

SYMBOL = "X"
BOARD_EMPTY = list((15*15) * " ")
BOARD_FULL = list((15*15) * SYMBOL)

class TestRandomPlay(unittest.TestCase):
    def setUp(self):
        self.player = RandomPlayer()

    def tearDown(self):
        self.player = None

    def test_move(self):
        board = BOARD_EMPTY
        for r in xrange(15*15):
            x, y = self.player.get_move(SYMBOL, "".join(board))
            self.assertTrue(0 <= x <= 15 and 0 <= y <= 15)
            board[15*y+x] = SYMBOL

        self.assertEqual(board, BOARD_FULL)

    def test_board_full(self):
        with self.assertRaises(ValueError) as context:
            self.player.get_move(SYMBOL, BOARD_FULL)

        self.assertTrue('Board is full' in context.exception)


if __name__ == '__main__':
    unittest.main()
