import unittest

from player_terminal import TerminalPlayer


class TestTerminalPlayer(unittest.TestCase):
    def setUp(self):
        self.player = TerminalPlayer()

    def tearDown(self):
        self.player = None

if __name__ == '__main__':
    unittest.main()
