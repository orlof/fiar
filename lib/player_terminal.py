from player import Player
from board import Cell


class TerminalPlayer(Player):
    def next_move(self, board):
        free = board.get_free_cells()
        if not free:
            raise ValueError("Board is full")

        while True:
            print("Give 'x,y' for next '%s': " % self.my_symbol)
            pos = input("> ")
            cell = self.parse_pos(pos)
            for free_cell in free:
                if cell == free_cell:
                    return free_cell

            print("Illegal position")

    @staticmethod
    def parse_pos(token):
        try:
            cell = Cell(token[0], token[1])
            return cell
        except ValueError:
            pass

        return None
