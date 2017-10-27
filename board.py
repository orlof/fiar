X_DIMENSION = 15
Y_DIMENSION = 15


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

    def update(self, move, mark):
        cell = self._find_cell(move[0], move[1])
        cell.mark = mark

    def __str__(self):
        printout = ""
        for cell in self.__cells:
            if cell.x == 0:
                printout += "|"
            printout += cell.mark
            if cell.x == 14:
                printout += "\n"
            else:
                printout += " "
        for x in range(X_DIMENSION * 2):
            printout += "-"
        return printout


