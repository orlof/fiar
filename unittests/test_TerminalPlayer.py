import unittest

from TerminalPlayer import TerminalPlayer

SYMBOL = "X"
BOARD_EMPTY = list((15*15) * "-")
BOARD_FULL = list((15*15) * SYMBOL)

class TestTerminalPlayer(unittest.TestCase):
    def setUp(self):
        self.player = TerminalPlayer()

    def tearDown(self):
        self.player = None

    def test_parse_coord(self):
        self.assertEqual(self.player.parse_pos(" 1  , 2 "),(1,2))

    def test_parse_text(self):
        self.assertEqual(self.player.parse_pos("xyz"), None)

    def test_parse_single_token(self):
        self.assertEqual(self.player.parse_pos("1"), None)

if __name__ == '__main__':
    unittest.main()
