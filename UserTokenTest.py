import unittest
from user_tokens import UserTokens as user
class UserTokenTest(unittest.TestCase):


    def test_available(self):
        self.assertEqual(user.available, -1,
                         'incorrect default available space')

    def test_X(self):
        self.assertEqual(user.X, 1,
                         'incorrect default available space')

    def test_O(self):
        self.assertEqual(user.O, 0,
                         'incorrect default available space')

if __name__ == '__main__':
    unittest.main()
