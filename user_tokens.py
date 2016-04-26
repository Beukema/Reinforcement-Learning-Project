#!/usr/local/bin/python3
from enum import IntEnum

# Represent the tokens for a board
class UserTokens(IntEnum):

    available = -1
    O = 0
    X = 1
    draw = 2
