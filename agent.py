import random
from user_tokens import UserTokens as user

class Agent(object):

    def __init__(self, user_token):
        '''
            Implementation of reinforced learning
        '''

        # A dictionary mapped as state => value
        self.move_values = {}

        # Random Rate: How often the agent will explore
        self.epsilon = .5

        self.moves_taken = 0

        # Discount Factor
        self.gamma = .9

        # Define what token this agent plays as
        self.token = user_token

        self.winning_value = 3
        self.available_value = .1
        self.draw_value = -1
        self.losing_value = -2

        # Keep track of last state the agent saw
        self.last_state = None
        self.last_value = 0



    def set_learn_rate(self, rate):
        '''
            Public setter for learn rate
        '''
        self.epsilon = rate

    def choose_random(self, board):
        '''
            random choice n board
        '''
        spaces = board.available_spaces()
        return random.choice(spaces)

    def set_user(self, user):
        '''
            sets the user token
        '''
        self.token = user

    def get_value_of_board(self, board):
        '''
            Get the vale of the move
        '''
        tokenized = board.tokenize()
        if not tokenized in self.move_values:
            self.add_key(board, tokenized)
        return self.move_values[tokenized]

    def add_key(self, board, key):
        '''
            check the move status
        '''
        game_status = board.game_status()

        if game_status == self.token:
            self.move_values[key] = self.winning_value
        elif game_status == user.available:
            self.move_values[key] = self.available_value
        elif game_status == user.draw:
            self.move_values[key] = self.draw_value
        else:
            self.move_values[key] = self.losing_value

    def next_move(self, board):
        '''
            Decide the net move base on reinforcement learning
        '''
        # if self.moves_taken % 200 == 0:
        #     self.epsilon *= .9

        # Keep track of state before
        self.last_state = board.tokenize()
        self.last_value = self.get_value_of_board(board)

        # Uses epsilon to choose if it will explore or not
        if random.random() <= self.epsilon:
            return self.choose_random(board)

        # Learning move
        else:
            highest_move = -1
            highest_value_of_move = -100000

            available_spaces = board.available_spaces()

            original_board = board.tokenize()


            # Goes through each available space and checks the value
            for i in range(len(available_spaces)):
                board.take_space(self.token, available_spaces[i])
                value = self.get_value_of_board(board)

                # If the value is higher than the current highest,
                # set new highest
                if value > highest_value_of_move:
                    highest_move = available_spaces[i]
                    highest_value_of_move = value

                # Return the board to the original
                board.set_board_from_string(original_board)

            # Based on the next move, and value, adjust the current value
            if self.last_state is not None:
                self.move_values[self.last_state] += self.gamma * (highest_value_of_move - self.last_value)

            self.moves_taken += 1
            return highest_move
