from player import Player
from board import X_DIMENSION, Y_DIMENSION
from collections import namedtuple

WeightedCell = namedtuple('WeightedCell', ['cell', 'weight'])

ADJACENT_CELLS_WEIGHT = 10


def location(cell):
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


def find_cells_in_row(board, cell, symbol, dx, dy):
    cells = 0
    for d in range(1, 5):
        if (not (0 <= (cell.x + d*dx) <= 14) or
                not (0 <= (cell.y + d*dy) <= 14)):
            return cells
        if board.find_cell(cell.x+d*dx, cell.y + d*dy).symbol != symbol:
            return cells
        else:
            cells += 1
    return cells


def friendly_cells(board, cell, symbol):
    cells_in_row = list()
    cells_in_row.append(find_cells_in_row(board, cell, symbol, 0, 1))
    cells_in_row.append(find_cells_in_row(board, cell, symbol, 0, -1))
    cells_in_row.append(find_cells_in_row(board, cell, symbol, 1, 0))
    cells_in_row.append(find_cells_in_row(board, cell, symbol, -1, 0))
    cells_in_row.append(find_cells_in_row(board, cell, symbol, -1, -1))
    cells_in_row.append(find_cells_in_row(board, cell, symbol, 1, -1))
    cells_in_row.append(find_cells_in_row(board, cell, symbol, 1, 1))
    cells_in_row.append(find_cells_in_row(board, cell, symbol, -1, 1))
    return max(cells_in_row) * ADJACENT_CELLS_WEIGHT


def calculate_weight_for_cells(board, free_cells, symbol):
    weighted_cells = list()
    for cell in free_cells:
        weight = location(cell)
        weight += friendly_cells(board, cell, symbol)
        weighted_cells.append(WeightedCell(cell, weight))
    return weighted_cells


class PlayerMattiBasicAI(Player):
    def next_move(self, symbol, board):
        free_cells = board.get_free_cells()
        if not free_cells:
            raise ValueError("Board is full")
        weighted_cells = calculate_weight_for_cells(board, free_cells, symbol)
        sorted_cells = sorted(weighted_cells, key=lambda x: x.weight,
                              reverse=True)
        return sorted_cells[0].cell
