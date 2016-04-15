#!/usr/local/bin/python3
import numpy as np
from user_tokens import UserTokens as user

class Board(object):

    def __init__(self):
        self.Board = None
        self._create_board_()

    def game_status(self):
        pass

    def take_space(self, user, space):
        pass

    def open_space(self, space):
        pass

    def reset_game(self):
        self._create_board_()

    def available_spaces(self):
        count = 0
        spaces = []
        board = self.Board.flatten()
        for space in np.nditer(board):
            print(space)
            if space == -1:
                spaces.append(count)
            count += 1

        return spaces


    def _create_board_(self):
        self.Board = np.matrix([[user.available, user.available, user.available],
            [user.available, user.available, user.available],
            [user.available, user.available, user.available]])

        print(self.Board)

if __name__ == '__main__':
    b = Board()
    s = b.available_spaces()
    print(s.all())
