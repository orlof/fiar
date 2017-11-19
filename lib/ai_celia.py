import keras
import numpy

import os
from keras.layers import Dense, Flatten, Conv2D
from keras.models import Sequential

from board import EMPTY, X_DIMENSION, Y_DIMENSION, other_symbol
from player import Player


DEBUG = False


class AiCelia(Player):
    def __init__(self):
        super().__init__()

    def start_game(self, my_symbol):
        super().start_game(my_symbol)
        self.filename = "ai_celia.h5"
        self.model = self.init_model()

    def end_game(self, is_winner, board):
        self.save_result_for_player(board, self.my_symbol, is_winner)
        self.save_result_for_player(board, other_symbol(self.my_symbol),
                                    not is_winner)
        keras.backend.clear_session()

    def init_model(self):
        model = Sequential()
        model.add(Conv2D(16, kernel_size=(5, 5), strides=(1, 1),
                         activation='relu', input_shape=(15, 15, 2)))
        model.add(Flatten())
        model.add(Dense(1000, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        model.compile(loss=keras.losses.binary_crossentropy,
                      optimizer=keras.optimizers.Adam())

        if os.path.exists(self.filename):
            model.load_weights(self.filename)

        return model

    def next_move(self, board):
        if board.is_empty():
            return board.cell_in(X_DIMENSION // 2, Y_DIMENSION // 2)

        # predict winning chance for each possible position
        probs = []
        free_cells = board.get_free_cells()
        for cell in free_cells:
            cell.symbol = self.my_symbol
            x = [self._get_board_as_tf_input(board, self.my_symbol)]
            x = numpy.array(x).astype('float32')
            probs.append(float(self.model.predict(x, batch_size=1)))
            cell.symbol = EMPTY

        if DEBUG:
            print("Win probability for %s is %f - %f - %f" % (
                self.my_symbol, min(probs), sum(probs) / len(probs),
                max(probs)))
            if len(free_cells) % 25 == 0:
                l = sorted([(p, c) for c, p in zip(free_cells, probs)],
                           reverse=True)
                print("Best option: %f %s" % l[0])
                print("Worst option: %f %s" % l[-1])
                for p, c in l[:5]:
                    c.symbol = "B"
                print(board)
                for p, c in l[:5]:
                    c.symbol = EMPTY
                input("Press Return")

        return max([(p, c) for p, c in zip(probs, free_cells)])[1]

    def _get_board_as_tf_input(self, board, my_symbol):
        # return 3 dimensional python list:
        # board = [row, row..]
        # row = [cell, cell...]
        # cell = [x_channel, o_channel]
        main = []
        for y in range(15):
            row = []
            for x in range(15):
                symbol = board.cell_in(x, y).symbol
                if symbol == EMPTY:
                    row.append([0.0, 0.0])
                else:
                    if symbol == my_symbol:
                        row.append([1.0, 0.0])
                    else:
                        row.append([0.0, 1.0])
            main.append(row)

        return main
