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

    def test_win_condition_horizontal_xmin_ymin(self):
        self.sut.update((0, 0), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((1, 0), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((2, 0), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((3, 0), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((4, 0), "x")
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_horizontal_xmax_ymin(self):
        self.sut.update((10, 0), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((11, 0), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((12, 0), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((13, 0), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((14, 0), "x")
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_horizontal_xmin_ymax(self):
        self.sut.update((0, 14), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((1, 14), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((2, 14), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((3, 14), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((4, 14), "x")
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_horizontal_xmax_ymax(self):
        self.sut.update((10, 14), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((11, 14), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((12, 14), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((13, 14), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((14, 14), "x")
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_vertical_xmin_ymin(self):
        self.sut.update((0, 1), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((0, 2), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((0, 3), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((0, 4), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((0, 5), "x")
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_vertical_xmin_ymax(self):
        self.sut.update((0, 10), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((0, 11), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((0, 12), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((0, 13), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((0, 14), "x")
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_vertical_xmax_ymin(self):
        self.sut.update((14, 1), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((14, 2), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((14, 3), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((14, 4), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((14, 5), "x")
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_vertical_xmax_ymax(self):
        self.sut.update((14, 10), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((14, 11), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((14, 12), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((14, 13), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((14, 14), "x")
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_diagonal_nw(self):
        self.sut.update((0, 0), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((1, 1), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((2, 2), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((3, 3), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((4, 4), "x")
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_diagonal_ne(self):
        self.sut.update((14, 0), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((13, 1), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((12, 2), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((11, 3), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((10, 4), "x")
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_diagonal_sw(self):
        self.sut.update((0, 14), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((1, 13), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((2, 12), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((3, 11), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((4, 10), "x")
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_diagonal_se(self):
        self.sut.update((14, 14), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((13, 13), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((12, 12), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((11, 11), "x")
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.update((10, 10), "x")
        self.assertTrue(self.sut.check_win_conditions("x"))
