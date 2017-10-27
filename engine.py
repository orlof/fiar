from player import Player


EVEN = "x"
ODD = "o"
X_DIMENSION = 15
Y_DIMENSION = 15


def is_even(value):
    return value % 2 == 0


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
        return [cell.mark for cell in self.__cells]

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


class Engine(object):
    def __init__(self, player1, player2):
        self.__players = (player1, player2)
        self.__board = Board()
        self.__round = 0
        self.__running = False

    def _get_player(self):
        if is_even(self.__round):
            return (self.__players[0], EVEN)
        else:
            return (self.__players[1], ODD)

    def run(self):
        print "Starting"
        self.__running = True
        while self.__running:
            print self.__board
            player, mark = self._get_player()
            player.get_next_move(self.__board, mark)


def main():
    player1 = Player()
    player2 = Player()
    engine = Engine(player1, player2)
    engine.run()

if __name__ == '__main__':
    main()
