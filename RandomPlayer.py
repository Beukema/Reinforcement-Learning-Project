from random import choice
from Player import Player
# from ttt import Board

class RandomPlayer(Player):
'''
    Implementation of random player
'''
    def __init__(self, token):
        self.token = token

    def next_move(self, board):
        '''
            The random next move
        '''
        return choice(board.available_spaces())

    def end_game(self, board):
        pass

if __name__ == '__main__':
    b= Board()

    r = RandomPlayer()
    for f in range(5):
        print(r.next_move(b))
