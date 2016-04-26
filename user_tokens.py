#!/usr/local/bin/python3
from enum import IntEnum

class UserTokens(IntEnum):
    '''
        Represent the tokens for a board
    '''
    available = -1
    O = 0
    X = 1
    draw = 2
