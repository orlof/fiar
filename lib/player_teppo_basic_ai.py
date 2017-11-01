from board import E, SE, S, SW
from player import Player


class PlayerTeppoBasicAI(Player):
    def next_move(self, symbol, board):
        value, cell = max([(self.get_cell_value(board, cell), cell) for cell in board.get_free_cells()])


    def get_cell_value(self, board, cell):
        self.get_cell_value_for_direction(board, cell, E)
        self.get_cell_value_for_direction(board, cell, SE)
        self.get_cell_value_for_direction(board, cell, S)
        self.get_cell_value_for_direction(board, cell, SW)

    def get_line(self, board, cell, direction):
        line = []
        for d in range(-5, 6):
            if d == 0: continue
            other = board.cell_in(cell.x - d * direction.dx, cell.y - d * direction.dy)
            line.append(other.symbol if other else None)
        return line

    def get_cell_value_for_direction(self, board, cell, direction, my_symbol):
        line = self.get_line(board, cell, direction)
        return max(self.get_line_value(line, (my_symbol, True)) + 2, self.get_line_value(line, (my_symbol, False)))

    def get_line_value(self, line, symbol):
