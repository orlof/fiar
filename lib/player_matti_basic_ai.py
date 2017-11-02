from player import Player
from board import X_DIMENSION, Y_DIMENSION
from collections import namedtuple

WeightedCell = namedtuple('WeightedCell', ['cell', 'weight'])

ADJACENT_CELLS_WEIGHT = 10
SYMBOLS = ("X", "O")


def get_other_symbol(symbol):
    if symbol == SYMBOLS[0]:
        return SYMBOLS[1]
    return SYMBOLS[0]


class LocationWeightCalculator(object):
    @classmethod
    def get_weight(cls, cell):
        weight = 0
        if cell.x <= X_DIMENSION / 2:
            weight += cell.x
        else:
            weight += X_DIMENSION - cell.x
        if cell.y <= Y_DIMENSION / 2:
            weight += cell.y
        else:
            weight += Y_DIMENSION - cell.y
        return weight


class AdjancentCellsCalculator(object):
    def calculate_weight(self):
        raise NotImplementedError("Calculate weight not implemented")

    @classmethod
    def get_weight(cls, cell, board, symbol):
        cells_in_row = list()
        cells_in_row.append(cls.nesw_diagonal_cells(board, cell, symbol))
        cells_in_row.append(cls.nwse_diagonal_cells(board, cell, symbol))
        cells_in_row.append(cls.horizontal_cells(board, cell, symbol))
        cells_in_row.append(cls.vertical_cells(board, cell, symbol))
        return cls.calculate_weight(max(cells_in_row))

    @classmethod
    def nesw_diagonal_cells(cls, board, cell, symbol):
        cells_in_row = cls.find_cells_in_row(board, cell, symbol, -1, -1)
        cells_in_row += cls.find_cells_in_row(board, cell, symbol, 1, 1)
        return cells_in_row

    @classmethod
    def nwse_diagonal_cells(cls, board, cell, symbol):
        cells_in_row = cls.find_cells_in_row(board, cell, symbol, 1, -1)
        cells_in_row += cls.find_cells_in_row(board, cell, symbol, -1, 1)
        return cells_in_row

    @classmethod
    def horizontal_cells(cls, board, cell, symbol):
        cells_in_row = cls.find_cells_in_row(board, cell, symbol, 0, 1)
        cells_in_row += cls.find_cells_in_row(board, cell, symbol, 0, -1)
        return cells_in_row

    @classmethod
    def vertical_cells(cls, board, cell, symbol):
        cells_in_row = cls.find_cells_in_row(board, cell, symbol, 1, 9)
        cells_in_row += cls.find_cells_in_row(board, cell, symbol, -1, 0)
        return cells_in_row

    @classmethod
    def find_cells_in_row(cls, cell, board, symbol, dx, dy):
        cells = 0
        for d in range(1, 5):
            if (not (0 <= (cell.x + d*dx) <= 14) or
                    not (0 <= (cell.y + d*dy) <= 14)):
                return cells
            if board.cell_in(cell.x+d*dx, cell.y + d*dy).symbol != symbol:
                return cells
            else:
                cells += 1
        return cells


class AttackWeightCalculator(AdjancentCellsCalculator):
    @classmethod
    def calculate_weight(cls, cells):
        return cells * ADJACENT_CELLS_WEIGHT


class DefenceWeightCalculator(AdjancentCellsCalculator):
    @classmethod
    def calculate_weight(cls, cells):
        if cells < 3:
            multiplier = ADJACENT_CELLS_WEIGHT - 5
        if cells == 3:
            multiplier = ADJACENT_CELLS_WEIGHT + 1
        if cells > 3:
            multiplier = ADJACENT_CELLS_WEIGHT + 5
        return cells * multiplier


class PlayerMattiBasicAI(Player):
    def __init__(self):
        super().__init__()
        self._locationWeightCalc = LocationWeightCalculator()
        self._attackWeightCalc = AttackWeightCalculator()
        self._defenceWeightCalc = DefenceWeightCalculator()

    def calculate_weight_for_cells(self, board, free_cells, symbol):
        other_symbol = get_other_symbol(symbol)
        weighted_cells = list()
        for cell in free_cells:
            weight = self._locationWeightCalc.get_weight(cell)
            weight += self._attackWeightCalc.get_weight(board, cell, symbol)
            weight += self._defenceWeightCalc.get_weight(board,
                                                         cell, other_symbol)
            weighted_cells.append(WeightedCell(cell, weight))
        return weighted_cells

    def next_move(self, board):
        free_cells = board.get_free_cells()
        if not free_cells:
            raise ValueError("Board is full")
        weighted_cells = self.calculate_weight_for_cells(
                board, free_cells, self.my_symbol)
        sorted_cells = sorted(weighted_cells, key=lambda x: x.weight,
                              reverse=True)
        return sorted_cells[0].cell
