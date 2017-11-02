import collections

SYMBOLS = "XO"
EVEN = SYMBOLS[0]
ODD = SYMBOLS[1]
EMPTY = "-"

X_DIMENSION = 15
Y_DIMENSION = 15

Direction = collections.namedtuple("Direction", ['dx', 'dy'])
N = Direction(0, -1)
NE = Direction(1, -1)
E = Direction(1, 0)
SE = Direction(1, 1)
S = Direction(0, 1)
SW = Direction(-1, 1)
W = Direction(-1, 0)
NW = Direction(-1, -1)

DIRECTIONS = (N, NE, E, SE, S, SW, W, NW)



def print_y_column(cell):
    if cell.x == 0:
        return "|"
    return ""


def print_line_change(cell):
    if cell.x == 14:
        return "|\n"
    else:
        return " "


class Cell(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = "-"

    def is_free(self):
        return self.symbol == "-"

    def __eq__(self, other):
        return (self.x == other.x and
                self.y == other.y)

    def __str__(self):
        return "Cell: (%d, %d) %s" % (self.x, self.y, self.symbol)


class Board(object):
    def __init__(self):
        self.__cells = list()
        self.__populate()

    def __populate(self):
        for y in range(0, Y_DIMENSION):
            for x in range(0, X_DIMENSION):
                self.__cells.append(Cell(x, y))

    def get_free_cells(self):
        return [cell for cell in self.__cells if cell.is_free()]

    def cell_in(self, x, y):
        if 0 <= x <= X_DIMENSION and 0 <= y <= Y_DIMENSION:
            for cell in self.__cells:
                if cell.x == x and cell.y == y:
                    return cell

        return None

    def is_empty(self):
        return len(self.get_free_cells()) == self.get_board_range()

    @staticmethod
    def get_board_range():
        return X_DIMENSION * Y_DIMENSION

    def check_win_conditions(self):
        for y in range(Y_DIMENSION):
            for x in range(X_DIMENSION):
                symbol = self.cell_in(x, y).symbol

                if symbol != EMPTY and \
                        any(self.__check(
                            symbol, x, y, direction.dx, direction.dy)
                            for direction in DIRECTIONS):
                    return symbol

        return None

    def __check(self, symbol, x, y, dx, dy):
        for d in range(0, 5):
            cell = self.cell_in(x + d * dx, y + d * dy)
            if cell is None or cell.symbol != symbol:
                return False

        return True

    def __str__(self):
        printout = ""
        for cell in self.__cells:
            printout += print_y_column(cell)
            printout += cell.symbol
            printout += print_line_change(cell)
        return printout

    def __iter__(self):
        return iter(self.__cells)

    def __getitem__(self, coordinate):
        index = coordinate[0] + (coordinate[1] * Y_DIMENSION)
        return self.__cells[index]

    def __eq__(self, other):
        for y in range(Y_DIMENSION):
            for x in range(X_DIMENSION):
                if self[(x, y)].symbol != other[(x, y)].symbol:
                    return False
        return True
