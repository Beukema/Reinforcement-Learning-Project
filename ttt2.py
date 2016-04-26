from user_tokens import UserTokens as user

class Board(object):
'''
    Removes numpy to increase speed
'''
    def __init__(self):
        self.Board = None
        self._create_board_()

    def tokenize(self):
        board = self.Board

        printout = ""

        for i in range(3):
            for j in range(3):
                if board[i][j] == user.X:
                    printout += "X"
                elif board[i][j] == user.O:
                    printout += "O"
                else:
                    printout += "-"

        return printout



    def set_board_from_string(self, string):

        for i in range(3):
            for j in range(3):
                if string[(i*3) + j] == "X":
                    self.Board[i][j] = user.X
                elif string[(i*3) + j] == "O":
                    self.Board[i][j] = user.O
                else:
                    self.Board[i][j] = user.available


    def print_board(self):
        board = self.Board

        printout = ""

        for i in range(3):
            for j in range(3):
                if board[i][j] == user.X:
                    printout += "X"
                elif board[i][j] == user.O:
                    printout += "O"
                else:
                    printout += " "

                if j is not 2:
                    printout += "|"

            if i is not 2:
                printout += "\n-----\n"

        return printout


    def game_status(self):
        if len(self.available_spaces()) == 0:
            return user.draw

        # Check for rows and columns
        for i in range(3):
            if self.Board[i][0] != user.available and self.Board[i][0] == self.Board[i][1] and self.Board[i][1] == self.Board[i][2]:
                return self.Board[i][0]
            elif self.Board[0][i] != user.available and self.Board[0][i] == self.Board[1][i] and self.Board[1][i] == self.Board[2][i]:
                return self.Board[0][i]

        # Check for diagonals
        if self.Board[0][0] is not user.available and self.Board[0][0] == self.Board[1][1] and self.Board[1][1] == self.Board[2][2]:
            return self.Board[0][0]
        elif self.Board[0][2] is not user.available and self.Board[0][2] == self.Board[1][1] and self.Board[1][1] == self.Board[2][0]:
            return self.Board[0][2]

        return user.available


    def take_space(self, user, space):

        if space >= 0 and space <= 8:
            self.Board[space // 3][space % 3] = user
        else:
            raise ValueError("Space chosen must be between 0 and 8")

    def open_space(self, space):
        return space in self.available_spaces()

    def reset_game(self):
        self._create_board_()

    def available_spaces(self):
        count = 0
        spaces = []

        for i in range(3):
            for j in range(3):
                if self.Board[i][j] == user.available:
                    spaces.append((i*3) + j)

        return spaces


    def _create_board_(self):
        self.Board = [[user.available, user.available, user.available],
            [user.available, user.available, user.available],
            [user.available, user.available, user.available]]
