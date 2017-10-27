import unittest

from Board import Board
from TerminalPlayer import TerminalPlayer

SYMBOL = "X"


def empty():
    return list((15*15) * " ")


class TestTerminalPlayer(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def tearDown(self):
        self.board = None

    def test_parse_coord(self):
        b = empty()
        b[0] = "X"
        b[1] = "X"
        b[2] = "X"
        b[3] = "X"
        b[4] = "X"

        self.assertEqual(self.board.check_winner(b), "X")

    def test_parse_coord(self):
        b = empty()

        self.assertEqual(self.board.check_winner(b), None)


if __name__ == '__main__':
    unittest.main()
