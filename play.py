from TicTacToe.tictactoe import TicTacToe
from TicTacToe.minimax import MiniMax
import random
import matplotlib.pyplot as plt
import sys
import numpy as np
from anytree import RenderTree
from pprint import pprint
import time


def human_player(board):
    print("\n")
    print(board)
    print("\n")

    player_pos_str = input("Type move x, y: ")
    x = int(player_pos_str[0])
    y = int(player_pos_str[-1])
    return x, y


def bot_random(board):
    t = TicTacToe(board)
    pos = random.choice(t.zero_positions)
    return pos


def bot_minimax(board):
    global m
    if not isinstance(m, MiniMax):
        m = MiniMax()

    print(f"Rating: {m.rate(TicTacToe(board))}")

    pos = m.best_move(board)
    return pos


def play_game(bot1, bot2):
    t = TicTacToe()
    while t.winner is None:
        if t.player == 1:
            pos = bot1(t.board)
        else:
            pos = bot2(t.board)
        t.mark(pos)
    return t.winner


wins = []
m = MiniMax()
print(m.rate(TicTacToe()))

play_game(human_player, bot_minimax)

for i in range(100):
    w = play_game(bot_random, bot_minimax)
    wins.append(w)

plt.hist(wins)
plt.show()
