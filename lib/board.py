X_DIMENSION = 15
Y_DIMENSION = 15


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
        return True if self.symbol == "-" else False


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

    def find_cell(self, x, y):
        for cell in self.__cells:
            if cell.x == x and cell.y == y:
                return cell

    @staticmethod
    def get_board_range():
        return X_DIMENSION * Y_DIMENSION

    def check_win_conditions(self, symbol):
        for y in xrange(15):
            for x in xrange(15):
                if (self.__check(symbol, x, y, 0, -1) or
                        self.__check(symbol, x, y, 0,  1) or
                        self.__check(symbol, x, y, 1,  0) or
                        self.__check(symbol, x, y, 1,  1) or
                        self.__check(symbol, x, y, 1, -1) or
                        self.__check(symbol, x, y, -1, 1)):
                    return True
        return False

    def __check(self, symbol, x, y, dx, dy):
        if not (0 <= (x + 5*dx) <= 15) or not (0 <= (y + 5*dy) <= 15):
            return False
        for d in xrange(0, 5):
            if self.find_cell(y+d*dy, x + d*dx).symbol != symbol:
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
        for y in xrange(Y_DIMENSION):
            for x in xrange(X_DIMENSION):
                if (self[(x, y)].symbol != other[(x, y)].symbol):
                    return False
        return True
