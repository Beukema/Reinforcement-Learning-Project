#!/usr/local/bin/python3
import numpy as np
from user_tokens import UserTokens as user

class Helper():
'''
    Static helper functions
'''
    @staticmethod
    def board_status(b):
        '''
            Checks for a winner of the game.
        '''
        board = np.array(b)
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
