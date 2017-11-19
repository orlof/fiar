import keras
import numpy


class Player(object):
    def __init__(self):
        super().__init__()
        self.my_symbol = None

    def next_move(self, board):
        raise NotImplemented("Interface not implemented")

    def start_game(self, player):
        self.my_symbol = player

    def end_game(self, is_winner, board):
        pass

    def save_result_for_player(self, board, symbol, is_winner):
        board_matrix = [self._get_board_as_tf_input(board, symbol)]
        x_train = numpy.array(board_matrix).astype('float32')

        if is_winner:
            y_train = [1.0]
        else:
            y_train = [0.0]
        y_train = numpy.array(y_train).astype('float32')

        self.save_result(x_train, y_train)

    def save_result(self, x_train, y_train):
        print("Training to: %r" % y_train)

        model = self.init_model()
        model.fit(x=x_train, y=y_train, epochs=2, batch_size=1)

        model.save_weights(self.filename)
