import unittest
from engine import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.sut = Board()

    def test_win_condition_horizontal_xmin_ymin(self):
        self.sut.find_cell(0, 0).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(1, 0).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(2, 0).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(3, 0).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(4, 0).symbol = "x"
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_horizontal_xmax_ymin(self):
        self.sut.find_cell(10, 0).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(11, 0).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(12, 0).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(13, 0).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(14, 0).symbol = "x"
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_horizontal_xmin_ymax(self):
        self.sut.find_cell(0, 14).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(1, 14).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(2, 14).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(3, 14).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(4, 14).symbol = "x"
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_horizontal_xmax_ymax(self):
        self.sut.find_cell(10, 14).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(11, 14).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(12, 14).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(13, 14).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(14, 14).symbol = "x"
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_vertical_xmin_ymin(self):
        self.sut.find_cell(0, 1).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(0, 2).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(0, 3).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(0, 4).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(0, 5).symbol = "x"
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_vertical_xmin_ymax(self):
        self.sut.find_cell(0, 10).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(0, 11).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(0, 12).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(0, 13).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(0, 14).symbol = "x"
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_vertical_xmax_ymin(self):
        self.sut.find_cell(14, 1).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(14, 2).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(14, 3).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(14, 4).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(14, 5).symbol = "x"
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_vertical_xmax_ymax(self):
        self.sut.find_cell(14, 10).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(14, 11).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(14, 12).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(14, 13).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(14, 14).symbol = "x"
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_diagonal_nw(self):
        self.sut.find_cell(0, 0).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(1, 1).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(2, 2).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(3, 3).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(4, 4).symbol = "x"
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_diagonal_ne(self):
        self.sut.find_cell(14, 0).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(13, 1).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(12, 2).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(11, 3).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(10, 4).symbol = "x"
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_diagonal_sw(self):
        self.sut.find_cell(0, 14).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(1, 13).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(2, 12).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(3, 11).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(4, 10).symbol = "x"
        self.assertTrue(self.sut.check_win_conditions("x"))

    def test_win_condition_diagonal_se(self):
        self.sut.find_cell(14, 14).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(13, 13).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(12, 12).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(11, 11).symbol = "x"
        self.assertFalse(self.sut.check_win_conditions("x"))
        self.sut.find_cell(10, 10).symbol = "x"
        self.assertTrue(self.sut.check_win_conditions("x"))
