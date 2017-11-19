import unittest
from basic_computer_player import PlayerBasicComputer
from board import Board, EVEN


class TestBasicComputerPlayer(unittest.TestCase):
    def setUp(self):
        self.sut = PlayerBasicComputer()
        self.board = Board()

    def test_first_move(self):
        self.sut.start_game(EVEN)
        cell = self.sut.next_move(self.board)
        self.assertEqual(7, cell.x)
        self.assertEqual(7, cell.y)
