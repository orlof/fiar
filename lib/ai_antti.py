import random

import keras
import numpy
import os
from keras.layers import Dense, Flatten, Conv2D
from keras.models import Sequential

from board import EMPTY, X_DIMENSION, Y_DIMENSION
from player import Player


class AiAntti(Player):
    def __init__(self):
        super().__init__()
        self.history = []
        self.model = None

    def start_game(self, my_symbol):
        self.my_symbol = my_symbol
        self.init_model("ai_antti_%s.h5" % my_symbol)

    def end_game(self, is_winner, board):
        x_train = numpy.array(self.history).astype('float32')

        if is_winner:
            y_train = [1.0] * len(self.history)
        else:
            y_train = [0.0] * len(self.history)
        y_train = numpy.array(y_train).astype('float32')

        self.model.fit(x=x_train, y=y_train, batch_size=1)

        self.model.save_weights("ai_antti_%s.h5" % self.my_symbol)

    def next_move(self, board):
        if board.is_empty():
            return board.cell_in(X_DIMENSION / 2, Y_DIMENSION / 2)

        self.history.append(self._get_board_as_tf_input(board))

        # predict winning chance for each possible position
        probs = []
        free_cells = board.get_free_cells()
        for cell in free_cells:
            cell.symbol = self.my_symbol
            x = [self._get_board_as_tf_input(board)]
            x = numpy.array(x).astype('float32')
            probs.append(self.model.predict(x, batch_size=1))
            cell.symbol = EMPTY

        return random.choices(free_cells, weights=probs, k=1)[0]

    def init_model(self, filename):
        input_shape = (15, 15, 2)

        model = Sequential()
        model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1),
                         activation='relu',
                         input_shape=input_shape))
        model.add(Flatten())
        model.add(Dense(1000, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        model.compile(loss=keras.losses.binary_crossentropy,
                      optimizer=keras.optimizers.Adam())

        if os.path.exists(filename):
            model.load_weights(filename)

        self.model = model

    def _get_board_as_tf_input(self, board):
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
                    if symbol == self.my_symbol:
                        row.append([1.0, 0.0])
                    else:
                        row.append([0.0, 1.0])
            main.append(row)

        return main
