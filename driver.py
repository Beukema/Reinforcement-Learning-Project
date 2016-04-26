import pdb
from ttt2 import Board
from agent2 import Agent
from RandomPlayer import RandomPlayer
from user_tokens import UserTokens as user
# from helper import Helper
from manual import Manual
import matplotlib.pyplot as plt


def play_game(a1, a2, verbose=False):
    '''
        This method plays a game and checks for a winner
    '''
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

    a1.end_game(board)
    a2.end_game(board)

    return board


def play_games(a1, a2, count, verbose=False, figure_name = 'default.png'):
    '''
        The method plays many games and displays graphs of the different
        winners.
    '''


    stats = {
        user.X: 0,
        user.O: 0,
        user.draw: 0
    }
    output_x = []
    output_y = []
    output_d = []
    poutput_x = []
    poutput_y = []
    poutput_d = []

    for i in range(count):
        board = play_game(a1,a2, verbose)

        stats[board.game_status()] += 1

        if i % 10 == 0:

            output_x.append(stats[user.X])
            output_y.append(stats[user.O])
            output_d.append(stats[user.draw])
            total = stats[user.X] + stats[user.O] + stats[user.draw]
            print(stats[user.X]/total)
            poutput_x.append(stats[user.X]/total)
            poutput_y.append(stats[user.O]/total)
            poutput_d.append(stats[user.draw]/total)

    # l1, = plt.plot(output_x, label='X Wins', linewidth=2)
    # l2, = plt.plot(output_y, label='Y Wins', linewidth=2)
    # ld, = plt.plot(output_d, label='draws', linewidth=2)
    # plt.legend(handles=[l1,l2,ld])
    # plt.ylabel('Tic Tac Toe Results')
    # plt.savefig(figure_name)

    pl1, = plt.plot(poutput_x, label='X', linewidth=2)
    pl2, = plt.plot(poutput_y, label='Y', linewidth=2)
    pld, = plt.plot(poutput_d, label='draws', linewidth=2)
    plt.legend(handles=[pl1,pl2,pld])
    plt.ylabel('Tic Tac Toe Win Percentages')
    plt.savefig('percentage' + figure_name)
    return stats

def print_stats(stats):
    '''
        This method prints the players statistics
    '''
    print("X: {}".format(stats[user.X]))
    print("O: {}".format(stats[user.O]))
    print("D: {}".format(stats[user.draw]))

def create_bar_graph(stats, filename):
    '''
        This method creats the bar graph showing the results for X, O, draw
    '''
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
a3 = Agent(user.O)

a4 = RandomPlayer(user.X)
a5 = Agent(user.O)

manual = Manual(user.O)
stats = play_games(a1, a2, 100000, figure_name = 'AgentX_RandY.png')
create_bar_graph(stats, 'agent_rand.png')
print_stats(stats)

a1.set_learn_rate(0)

stats = play_games(a4, a3, 100000, figure_name = 'AgentX_RandY2.png')
create_bar_graph(stats, 'agent_rand2.png')
print_stats(stats)

a3.set_learn_rate(0)

stats = play_games(a1, a3, 10000, figure_name = 'AgentX_RandY3.png')
create_bar_graph(stats, 'agent_rand3.png')
print_stats(stats)



# print_stats(play_games(a1, a5, 20000))
# print_stats(play_games(a4, a5, 20000))

# a1.set_learn_rate(0.05)
#
#
# stats = play_games(a1, a2, 10000, figure_name = 'AgentX_RandY2.png')
# create_bar_graph(stats, 'agent_rand2.png')
# print_stats(stats)

# a5.set_learn_rate(0)



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
