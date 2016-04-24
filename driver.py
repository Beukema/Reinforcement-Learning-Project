import pdb
from ttt2 import Board
from agent import Agent
from RandomPlayer import RandomPlayer
from user_tokens import UserTokens as user
from helper import Helper
from manual import Manual



def play_game(a1, a2, verbose=False):
    board = Board()
    players = [a1,a2]
    turns = 0

    while board.game_status() is user.available:
        player = players[turns % 2]
        board.take_space(player.token, player.next_move(board))
        turns += 1
        if verbose:
            print(board.print_board())
            print("\n\n")
            pdb.set_trace()

    return board


def play_games(a1, a2, count, verbose=False):

    stats = {
        user.X: 0,
        user.O: 0,
        user.draw: 0
    }

    for i in range(count):
        board = play_game(a1,a2, verbose)

        stats[board.game_status()] += 1

    return stats

def print_stats(stats):
    print("X: {}".format(stats[user.X]))
    print("O: {}".format(stats[user.O]))
    print("D: {}".format(stats[user.draw]))

a1 = Agent(user.X)
a2 = RandomPlayer(user.O)
a3 = Agent(user.X)

a4 = RandomPlayer(user.X)
a5 = Agent(user.O)

manual = Manual(user.X)

# print_stats(play_games(a1, a2, 2000))

print_stats(play_games(a1, a5, 20000))
print_stats(play_games(a4, a5, 20000))

a1.set_learn_rate(0)
a5.set_learn_rate(0)

print_stats(play_games(a1, a5, 3, True))
# print_stats(play_games(manual, a5, 3))

# print_stats(play_games(a4, a5, 1000))
# print_stats(play_games(a4, a5, 3000))
# print_stats(play_games(a4, a5, 3000))



# stats = play_games(a4, a2, 10)
# print("X: {}".format(stats[user.X]))
# print("O: {}".format(stats[user.O]))
# print("D: {}".format(stats[user.draw]))

# stats = play_games(a1,a2, 1000)
#
# print("Agent1, X goes first")
# print("X: {}".format(stats[user.X]))
# print("O: {}".format(stats[user.O]))
# print("D: {}".format(stats[user.draw]))
#
# stats = play_games(a1,a2, 1000)
#
# print("Agent1, X goes first")
# print("X: {}".format(stats[user.X]))
# print("O: {}".format(stats[user.O]))
# print("D: {}".format(stats[user.draw]))
#
#
# stats = play_games(a2,a1, 1000)
#
# print("Agent1, X goes second")
# print("X: {}".format(stats[user.X]))
# print("O: {}".format(stats[user.O]))
# print("D: {}".format(stats[user.draw]))
#
#
# stats = play_games(a3,a2, 1000)
#
# print("Agent2, X goes first")
# print("X: {}".format(stats[user.X]))
# print("O: {}".format(stats[user.O]))
# print("D: {}".format(stats[user.draw]))
#
#
# stats = play_games(a2,a3, 1000)
#
# print("Agent2, X goes second")
# print("X: {}".format(stats[user.X]))
# print("O: {}".format(stats[user.O]))
# print("D: {}".format(stats[user.draw]))
#
# a3.set_user(user.O)
#
# stats = play_games(a1,a3, 1000)
# print("Agents head up, X goes first (agent 1)")
# print("X: {}".format(stats[user.X]))
# print("O: {}".format(stats[user.O]))
# print("D: {}".format(stats[user.draw]))
#
# stats = play_games(a3,a1, 1000)
# print("Agents head up, X goes second (agent 1)")
# print("X: {}".format(stats[user.X]))
# print("O: {}".format(stats[user.O]))
# print("D: {}".format(stats[user.draw]))
# pdb.set_trace()
