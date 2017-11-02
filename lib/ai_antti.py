import random

import keras
import numpy
import os
from keras.layers import Dense, Flatten, Conv2D
from keras.models import Sequential

from board import EMPTY, X_DIMENSION, Y_DIMENSION
from player import Player


DEBUG = True


class AiAntti(Player):
    def __init__(self):
        super().__init__()
        self.history = []
        self.model = None

    def start_game(self, my_symbol):
        super().start_game(my_symbol)
        self.filename = "ai_antti.h5"
        self.init_model()

    def end_game(self, is_winner, board):
        train_history = 10
        # train_history = len(self.history)

        x_train = numpy.array(self.history[-train_history:]).astype('float32')

        if is_winner:
            y_train = [1.0] * train_history
        else:
            y_train = [0.0] * train_history
        y_train = numpy.array(y_train).astype('float32')

        if os.path.exists(self.filename):
            self.model.load_weights(self.filename)

        print("Training to: %r" % y_train)

        self.model.fit(x=x_train, y=y_train, epochs=2, batch_size=1)

        self.model.save_weights(self.filename)

    def next_move(self, board):
        if board.is_empty():
            return board.cell_in(X_DIMENSION // 2, Y_DIMENSION // 2)

        self.history.append(self._get_board_as_tf_input(board))

        # predict winning chance for each possible position
        probs = []
        free_cells = board.get_free_cells()
        for cell in free_cells:
            cell.symbol = self.my_symbol
            x = [self._get_board_as_tf_input(board)]
            x = numpy.array(x).astype('float32')
            probs.append(float(self.model.predict(x, batch_size=1)))
            cell.symbol = EMPTY

        print("Win probability for %s is %f - %f - %f" % (self.my_symbol, min(probs), sum(probs)/len(probs), max(probs)))
        if DEBUG:
            if len(free_cells) % 25 == 0:
                l = sorted([(p, c) for c, p in zip(free_cells, probs)], reverse=True)
                print("Best option: %f %s" % l[0])
                print("Worst option: %f %s" % l[-1])
                for p, c in l[:5]:
                    c.symbol = "B"
                print(board)
                for p, c in l[:5]:
                    c.symbol = EMPTY
                input("Press Return")

        return random.choices(free_cells, weights=probs, k=1)[0]

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
