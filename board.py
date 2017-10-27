X_DIMENSION = 15
Y_DIMENSION = 15


def print_x_column(cell):
    if cell.x == 0:
        return "|"
    return ""


def print_y_column():
    printout = ""
    for x in range(X_DIMENSION * 2):
        printout += "-"
    return printout


def print_line_change(cell):
    if cell.x == 14:
        return "\n"
    else:
        return " "


class Cell(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = "-"


class Board(object):
    def __init__(self):
        self.__cells = list()
        self.__populate()

    def __populate(self):
        for y in range(0, Y_DIMENSION):
            for x in range(0, X_DIMENSION):
                self.__cells.append(Cell(x, y))

    def get_board(self):
        return "".join([cell.symbol for cell in self.__cells])

    def __find_cell(self, x, y):
        for cell in self.__cells:
            if cell.x == x and cell.y == y:
                return cell

    def update(self, coordinate, symbol):
        cell = self.__find_cell(coordinate[0], coordinate[1])
        cell.symbol = symbol

    def check_win_conditions(self, symbol):
        for y in xrange(15):
            for x in xrange(15):
                if (self.__check(symbol, x, y, 0, -1) or
                        self.__check(symbol, x, y, 1, -1) or
                        self.__check(symbol, x, y, 0,  1) or
                        self.__check(symbol, x, y, 1,  0) or
                        self.__check(symbol, x, y, 1,  1)):
                    return True
        return False

    def __check(self, symbol, x, y, dx, dy):
        if not (0 <= (x + 5*dx) <= 15) or not (0 <= (y + 5*dy) <= 15):
            return False
        for d in xrange(0, 5):
            if self.__find_cell(y+d*dy, x + d*dx).symbol != symbol:
                return False
        return True

    def __str__(self):
        printout = ""
        for cell in self.__cells:
            printout += print_x_column(cell)
            printout += cell.symbol
            printout += print_line_change(cell)
        print_y_column()
        return printout
