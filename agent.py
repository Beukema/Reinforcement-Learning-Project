import random

class Agent(object):

    def __init__(self, user_token):

        # A dictionary mapped as state => value
        move_values = {}

        # Random Rate: How often the agent will explore
        self.epsilon = .7

        # Discount Factor
        self.gamma = .9

        # Define what token this agent plays as
        self.token = user_token

    def make_move(self, board):
        spaces = board.available_spaces
        
        return random.choice(spaces)
