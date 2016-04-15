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

if __name__ == '__main__':
    unittest.main()
