import unittest
from player_matti_basic_ai import PlayerMattiBasicAI
from board import Board

SYMBOL = "x"


class TestMattiBasicAI(unittest.TestCase):
    def setUp(self):
        self.sut = PlayerMattiBasicAI()
        self.board = Board()

    def test_first_move(self):
        cell = self.sut.next_move(SYMBOL, self.board)
        self.assertEqual(7, cell.x)
        self.assertEqual(7, cell.y)
