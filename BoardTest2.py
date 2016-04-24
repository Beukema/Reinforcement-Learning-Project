import unittest
from ttt2 import Board

class BoardTest(unittest.TestCase):

    def setUp(self):
        self.Board = Board()

    def test_available_spaces(self):
        self.Board.Board = [[0,0,0],[-1,-1,-1],[-1,-1,-1]]
        spaces = self.Board.available_spaces()
        self.assertEqual([3,4,5,6,7,8], spaces)

    def test_game_stats(self):
        self.Board.Board = [[0,0,0],[-1,-1,-1],[-1,-1,-1]]
        status = self.Board.game_status()
        self.assertEqual(0,status)

        self.Board.Board = [[-1,-1,-1],[0,0,0],[-1,-1,-1]]
        status = self.Board.game_status()
        self.assertEqual(0,status)

        self.Board.Board = [[-1,-1,-1],[-1,-1,-1],[0,0,0]]
        status = self.Board.game_status()
        self.assertEqual(0,status)

        self.Board.Board = [[0,-1,-1],[0,-1,-1],[0,-1,-1]]
        status = self.Board.game_status()
        self.assertEqual(0,status)

        self.Board.Board = [[-1,0,-1],[-1,0,-1],[-1,0,-1]]
        status = self.Board.game_status()
        self.assertEqual(0,status)

        self.Board.Board = [[0,-1,-1],[-1,0,-1],[-1,-1,-0]]
        status = self.Board.game_status()
        self.assertEqual(0,status)

    def test_take_space(self):
        self.Board.reset_game()
        self.Board.take_space(0,8)
        space = self.Board.Board[2][2]
        self.assertEqual(0,space)

        self.Board.take_space(1,7)
        space = self.Board.Board[2][1]
        self.assertEqual(1,space)

        self.Board.take_space(0,6)
        space = self.Board.Board[2][0]
        self.assertEqual(0,space)

        self.Board.take_space(1,5)
        space = self.Board.Board[1][2]
        self.assertEqual(1,space)

        self.Board.take_space(0,4)
        space = self.Board.Board[1][1]
        self.assertEqual(0,space)

        self.Board.take_space(1,3)
        space = self.Board.Board[1][0]
        self.assertEqual(1,space)

        self.Board.take_space(0,1)
        space = self.Board.Board[0][1]
        self.assertEqual(0,space)

        self.Board.take_space(1,0)
        space = self.Board.Board[0][0]
        self.assertEqual(1,space)

        self.Board.take_space(1,2)
        space = self.Board.Board[0][2]
        self.assertEqual(1,space)



    def test_tokenizing_and_restoring(self):
        initial = self.Board.tokenize()
        self.Board.set_board_from_string(initial)
        next_token = self.Board.tokenize()
        self.assertEqual(initial, next_token)

        self.Board.Board = [[-1,-1,-1],[-1,-1,-1],[0,0,0]]
        initial = self.Board.tokenize()
        self.Board.set_board_from_string(initial)
        next_token = self.Board.tokenize()
        self.assertEqual(initial, next_token)


if __name__ == '__main__':
    unittest.main()
