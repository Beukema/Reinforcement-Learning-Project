import random
from user_tokens import UserTokens as user

class Agent(object):

    def __init__(self, user_token):

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

        self.move_record = []



    def set_learn_rate(self, rate):
        self.epsilon = rate

    def choose_random(self, board):
        spaces = board.available_spaces()
        return random.choice(spaces)

    def set_user(self, user):
        self.token = user

    def get_value_of_board(self, board):
        tokenized = board.tokenize()
        return self.get_value_of_board_from_state(tokenized, board)

    def get_value_of_board_from_state(self, state, board):
        if not state in self.move_values:
            self.add_key(board, state)
        return self.move_values[state]

    def add_key(self, board, key):
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

        if self.moves_taken % 1000 == 0:
            self.epsilon *= .9

        # Keep track of state before
        self.last_state = board.tokenize()
        self.last_value = self.get_value_of_board(board)
        chosen_move = -1
        chosen_state = None
        chosen_value = 0
        original_board = board.tokenize()

        # Uses epsilon to choose if it will explore or not
        if random.random() <= self.epsilon:
            chosen_move = self.choose_random(board)

            board.take_space(self.token, chosen_move)
            chosen_state = board.tokenize()
            chosen_value = self.get_value_of_board(board)

            board.set_board_from_string(original_board)

        # Learning move
        else:
            highest_move = -1
            highest_value_of_move = -100000
            highest_state = None

            available_spaces = board.available_spaces()

            # Goes through each available space and checks the value
            for i in range(len(available_spaces)):
                board.take_space(self.token, available_spaces[i])
                value = self.get_value_of_board(board)

                # If the value is higher than the current highest,
                # set new highest
                if value > highest_value_of_move:
                    highest_move = available_spaces[i]
                    highest_value_of_move = value
                    highest_state = board.tokenize()

                # Return the board to the original
                board.set_board_from_string(original_board)

            chosen_state = highest_state
            chosen_move = highest_move
            chosen_value = highest_value_of_move

        # Keep record of every move the agent makes
        self.move_record.append(chosen_state)

        return chosen_move

    # If the over, trigger back propogation of reward
    def end_game(self, board):
        value = self.get_value_of_board(board)
        self.move_values[self.move_record[-1]] = value
        self.back_propogate()
        self.move_record = []

    def back_propogate(self):

        last_value = 0
        for i in range(len(self.move_record) - 1):
            current_key = self.move_record.pop()
            current_value = self.move_values[current_key]

            self.move_values[self.move_record[-1]] += self.gamma * (current_value - self.move_values[self.move_record[-1]])
