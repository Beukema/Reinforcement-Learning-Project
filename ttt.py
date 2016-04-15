#!/usr/local/bin/python3
import numpy as np
from user_tokens import UserTokens as user

class Board(object):

    def __init__(self):
        self.Board = None
        self._create_board_()

    def game_status(self):
        board = np.array(self.Board)
        for r in range(3):
            row = board[r]
            column = board[:,r]
            if np.all(row == user.X):
                return user.X
            if np.all(row == user.O):
                return user.O
            if np.all(column == user.X):
                return user.X
            if np.all(column == user.O):
                return user.O

        diagonal = np.diagonal(board)


        if np.all(diagonal == user.O):
            return user.O

        if np.all(diagonal == user.X):
            return user.X

        board_flip =  np.fliplr(board)
        reverse_diagonal = np.diagonal(board_flip)

        if np.all(reverse_diagonal == user.O):
            return user.O

        if np.all(reverse_diagonal == user.X):
            return user.X

        return user.available


    def take_space(self, user, space):
        board = np.array(self.Board).flatten()
        board[space] = user
        self.Board = board.reshape(3,3)

    def open_space(self, space):
        board = np.array(self.Board).flatten().tolist()
        return user.available == board[space]

    def reset_game(self):
        self._create_board_()

    def available_spaces(self):
        count = 0
        spaces = []
        board = self.Board.flatten()
        for space in np.nditer(board):
            if space == -1:
                spaces.append(count)
            count += 1

        return spaces


    def _create_board_(self):
        self.Board = np.matrix([[user.available, user.available, user.available],
            [user.available, user.available, user.available],
            [user.available, user.available, user.available]])
