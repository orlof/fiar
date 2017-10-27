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
        self.mark = "-"


class Board(object):
    def __init__(self):
        self.__cells = list()
        self.__populate()

    def __populate(self):
        for y in range(0, Y_DIMENSION):
            for x in range(0, X_DIMENSION):
                self.__cells.append(Cell(x, y))

    def get_board(self):
        return "".join([cell.mark for cell in self.__cells])

    def _find_cell(self, x, y):
        for cell in self.__cells:
            if cell.x == x and cell.y == y:
                return cell

    def update(self, coordinate, mark):
        cell = self._find_cell(coordinate[0], coordinate[1])
        cell.mark = mark

    def __str__(self):
        printout = ""
        for cell in self.__cells:
            printout += print_x_column(cell)
            printout += cell.mark
            printout += print_line_change(cell)
        print_y_column()
        return printout
