import pdb
from ttt2 import Board
from agent import Agent
from RandomPlayer import RandomPlayer
from user_tokens import UserTokens as user
from helper import Helper
from manual import Manual
import matplotlib.pyplot as plt


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


def play_games(a1, a2, count, verbose=False, figure_name = 'default.png'):

    stats = {
        user.X: 0,
        user.O: 0,
        user.draw: 0
    }
    output_x = []
    output_y = []
    output_d = []
    for i in range(count):
        board = play_game(a1,a2, verbose)

        stats[board.game_status()] += 1

        if i % 10 == 0:
            print("output x")
            output_x.append(stats[user.X])
            output_y.append(stats[user.O])
            output_d.append(stats[user.draw])

    l1, = plt.plot(output_x, label='X Wins', linewidth=2)
    l2, = plt.plot(output_y, label='Y Wins', linewidth=2)
    ld, = plt.plot(output_d, label='draws', linewidth=2)
    plt.legend(handles=[l1,l2,ld])
    plt.ylabel('Tic Tac Toe Results')
    plt.savefig(figure_name)
    return stats

def print_stats(stats):
    print("X: {}".format(stats[user.X]))
    print("O: {}".format(stats[user.O]))
    print("D: {}".format(stats[user.draw]))

def create_bar_graph(stats, filename):
    fig, ax = plt.subplots()
    width = 1/1.5
    y = [stats[user.X],stats[user.O],stats[user.draw]]
    x = range(3)
    b1 = ax.bar(0, [stats[user.X]], width, color='b')
    b2 = ax.bar(1, [stats[user.O]], width, color='r')
    b3 = ax.bar(2, [stats[user.draw]], width, color='g')

    plt.xlabel('Player')
    plt.ylabel('Games Won')
    plt.title('Tic Tac Toe Results')
    plt.xticks(x, ('X', 'O', 'Draw'))
    plt.legend()

    plt.savefig(filename)

a1 = Agent(user.X)
a2 = RandomPlayer(user.O)
a3 = Agent(user.X)

a4 = RandomPlayer(user.X)
a5 = Agent(user.O)

manual = Manual(user.X)
stats = play_games(a1, a2, 2000, figure_name = 'AgentX_RandY.png')
create_bar_graph(stats, 'agent_rand.png')
print_stats(stats)

# print_stats(play_games(a1, a5, 20000))
# print_stats(play_games(a4, a5, 20000))

a1.set_learn_rate(0)
a5.set_learn_rate(0)

# print_stats(play_games(a1, a5, 3, True))
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
