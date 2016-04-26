class Manual(object):
    '''
        Playing the game verse the learner
    '''
    def __init__(self, token):
        self.token = token

    def next_move(self, board):
        '''
            Waits for input from user.
        '''
        need_move = True
        move = -1

        print(board.print_board())
        while need_move:

            move = int(input("Where would you like to play? "))

            if move in board.available_spaces():
                need_move = False
            else:
                print("That space is not available")

        return move

    def end_game(self, board):
        pass
