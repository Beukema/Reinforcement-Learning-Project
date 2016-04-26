import pdb
from ttt2 import Board
from agent2 import Agent
from RandomPlayer import RandomPlayer
from user_tokens import UserTokens as user
from manual import Manual
import matplotlib.pyplot as plt

# This method plays a game and checks for a winner
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

    a1.end_game(board)
    a2.end_game(board)

    return board

# The method plays many games and displays graphs of the different
# winners.
def play_games(a1, a2, count, verbose=False, figure_name = 'default.png'):
    
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

    pl1, = plt.plot(poutput_x, label='X', linewidth=2)
    pl2, = plt.plot(poutput_y, label='Y', linewidth=2)
    pld, = plt.plot(poutput_d, label='draws', linewidth=2)
    plt.legend(handles=[pl1,pl2,pld])
    plt.ylabel('Tic Tac Toe Win Percentages')
    plt.savefig('percentage' + figure_name)
    return stats


# This method prints the players statistics
def print_stats(stats):
    print("X: {}".format(stats[user.X]))
    print("O: {}".format(stats[user.O]))
    print("D: {}".format(stats[user.draw]))


# This method creats the bar graph showing the results for X, O, draw
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
