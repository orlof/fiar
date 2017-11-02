import unittest

from board import Board, EVEN
from player_random import RandomPlayer

SYMBOL = "X"


def get_full_board(symbol):
    board = Board()
    for cell in board:
        cell.symbol = symbol
    return board


class TestRandomPlayer(unittest.TestCase):
    def setUp(self):
        self.player = RandomPlayer()
        self.player.start_game(EVEN)

    def tearDown(self):
        self.player = None

    def test_move(self):
        board = Board()
        for r in range(board.get_board_range()):
            cell = self.player.next_move(board)
            self.assertTrue(0 <= cell.x <= 15 and 0 <= cell.y <= 15)
            cell.symbol = EVEN

        full_board = get_full_board(EVEN)
        self.assertEqual(board, full_board)

    def test_board_full(self):
        with self.assertRaises(ValueError):
            self.player.next_move(get_full_board(EVEN))


if __name__ == '__main__':
    unittest.main()
