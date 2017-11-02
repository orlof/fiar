import random

import keras
import numpy
import os
from keras.layers import Dense, Flatten, Conv2D
from keras.models import Sequential

from board import EMPTY, X_DIMENSION, Y_DIMENSION
from player import Player
from player_random import RandomPlayer

DEBUG = True


class AiBerit(RandomPlayer):
    def __init__(self):
        super().__init__()
        self.model = None

    def start_game(self, my_symbol):
        super().start_game(my_symbol)
        self.filename = "ai_berit.h5"

    def end_game(self, is_winner, board):
        board_matrix = [self._get_board_as_tf_input(board)]
        x_train = numpy.array(board_matrix).astype('float32')

        if is_winner:
            y_train = [1.0]
        else:
            y_train = [0.0]
        y_train = numpy.array(y_train).astype('float32')

        print("Training to: %r" % y_train)

        model = self.init_model()
        model.fit(x=x_train, y=y_train, epochs=2, batch_size=1)

        model.save_weights(self.filename)

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
