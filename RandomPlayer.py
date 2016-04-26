from random import choice
from Player import Player

# Implementation of random player
class RandomPlayer(Player):

    def __init__(self, token):
        self.token = token

	# The random next move
    def next_move(self, board):
        return choice(board.available_spaces())

    def end_game(self, board):
        pass

if __name__ == '__main__':
    b= Board()

    r = RandomPlayer()
    for f in range(5):
        print(r.next_move(b))
