import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.sut = Board()

    def test_win_condition_horizontal_xmin_ymin(self):
        self.sut.cell_in(0, 0).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(1, 0).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(2, 0).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(3, 0).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(4, 0).symbol = "X"
        self.assertTrue(self.sut.check_win_conditions())

    def test_win_condition_horizontal_xmax_ymin(self):
        self.sut.cell_in(10, 0).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(11, 0).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(12, 0).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(13, 0).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(14, 0).symbol = "X"
        self.assertTrue(self.sut.check_win_conditions())

    def test_win_condition_horizontal_xmin_ymax(self):
        self.sut.cell_in(0, 14).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(1, 14).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(2, 14).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(3, 14).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(4, 14).symbol = "X"
        self.assertTrue(self.sut.check_win_conditions())

    def test_win_condition_horizontal_xmax_ymax(self):
        self.sut.cell_in(10, 14).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(11, 14).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(12, 14).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(13, 14).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(14, 14).symbol = "X"
        self.assertTrue(self.sut.check_win_conditions())

    def test_win_condition_vertical_xmin_ymin(self):
        self.sut.cell_in(0, 1).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(0, 2).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(0, 3).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(0, 4).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(0, 5).symbol = "X"
        self.assertTrue(self.sut.check_win_conditions())

    def test_win_condition_vertical_xmin_ymax(self):
        self.sut.cell_in(0, 10).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(0, 11).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(0, 12).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(0, 13).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(0, 14).symbol = "X"
        self.assertTrue(self.sut.check_win_conditions())

    def test_win_condition_vertical_xmax_ymin(self):
        self.sut.cell_in(14, 1).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(14, 2).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(14, 3).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(14, 4).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(14, 5).symbol = "X"
        self.assertTrue(self.sut.check_win_conditions())

    def test_win_condition_vertical_xmax_ymax(self):
        self.sut.cell_in(14, 10).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(14, 11).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(14, 12).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(14, 13).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(14, 14).symbol = "X"
        self.assertTrue(self.sut.check_win_conditions())

    def test_win_condition_diagonal_nw(self):
        self.sut.cell_in(0, 0).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(1, 1).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(2, 2).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(3, 3).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(4, 4).symbol = "X"
        self.assertTrue(self.sut.check_win_conditions())

    def test_win_condition_diagonal_ne(self):
        self.sut.cell_in(14, 0).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(13, 1).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(12, 2).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(11, 3).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(10, 4).symbol = "X"
        self.assertTrue(self.sut.check_win_conditions())

    def test_win_condition_diagonal_sw(self):
        self.sut.cell_in(0, 14).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(1, 13).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(2, 12).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(3, 11).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(4, 10).symbol = "X"
        self.assertTrue(self.sut.check_win_conditions())

    def test_win_condition_diagonal_se(self):
        self.sut.cell_in(14, 14).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(13, 13).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(12, 12).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(11, 11).symbol = "X"
        self.assertFalse(self.sut.check_win_conditions())
        self.sut.cell_in(10, 10).symbol = "X"
        self.assertTrue(self.sut.check_win_conditions())
