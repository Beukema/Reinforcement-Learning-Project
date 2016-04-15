#!/usr/local/bin/python3
import unittest
import numpy as np
from ttt import Board

class BoardTest(unittest.TestCase):

    def setUp(self):
        self.Board = Board()

    def test_board(self):
        self.assertEqual(self.Board.Board.all(), np.matrix('-1 -1 -1; -1 -1 -1; -1 -1 -1').all(),
                         'incorrect default board setup')

    def test_available_spaces(self):
        self.assertEqual(self.Board.available_spaces(), [0,1,2,3,4,5,6,7,8],
                         'incorrect available_spaces')

    def test_open_space(self):
        self.assertEqual(self.Board.open_space(3), True,
                         'incorrect available_spaces')

    def test_take_space(self):
        self.Board.take_space(0, 0)
        self.assertEqual(self.Board.Board.all(), np.matrix('0 -1 -1; -1 -1 -1; -1 -1 -1').all(),
                         'incorrect default board setup')

    def test_reset_game(self):
        self.Board.reset_game()
        self.assertEqual(self.Board.Board.all(), np.matrix('-1 -1 -1; -1 -1 -1; -1 -1 -1').all(),
                         'incorrect default board setup')

    def test_game_status(self):
        self.Board.Board = np.matrix('0 0 0; -1 -1 -1; -1 -1 -1')
        status = self.Board.game_status()
        self.assertEqual(0,status)

        self.Board.Board = np.matrix('-1 -1 0; -1 -1 0; -1 -1 0')
        status = self.Board.game_status()
        self.assertEqual(0,status)

        self.Board.Board = np.matrix('1 1 1; -1 -1 -1; -1 -1 -1')
        status = self.Board.game_status()
        self.assertEqual(1,status)

        self.Board.Board = np.matrix('0 -1 -1; -1 0 -1; -1 -1 0')
        status = self.Board.game_status()
        self.assertEqual(0,status)

        self.Board.Board = np.matrix('-1 -1 0; -1 0 0; -1 -1 0')
        status = self.Board.game_status()
        self.assertEqual(0,status)
        # self.assertEqual(self.Board.Board.all(), np.matrix('-1 -1 -1; -1 -1 -1; -1 -1 -1').all(),
        #                  'incorrect default board setup')
        self.Board.Board = np.matrix('-1 -1 -1; -1 -1 -1; -1 -1 -1')

if __name__ == '__main__':
    unittest.main()
