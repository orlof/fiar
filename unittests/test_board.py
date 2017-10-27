import unittest
from engine import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.sut = Board()

    def test_get_board(self):
        expected_board = "".join(["-" for _ in range(0, 15*15)])
        board = self.sut.get_board()
        self.assertEqual(expected_board, board)

    def test_update_board(self):
        self.sut.update((0, 0), "x")
        self.assertEqual("x", self.sut.get_board()[0])
