class Player(object):
    def __init__(self):
        super().__init__()
        self.my_symbol = None

    def next_move(self, board):
        raise NotImplemented("Interface not implemented")

    def start_game(self, player):
        self.my_symbol = player

    def end_game(self, winner, board):
        pass
