from TikTakToe.tiktaktoe import TikTakToe
from TikTakToe.minimax import MiniMax
import random
import matplotlib.pyplot as plt
import numpy as np
from anytree import RenderTree
from pprint import pprint


def human_play(board):
    print("\n")
    print(board)
    print("\n")

    player_pos_str = input("Type move x, y: ")
    x = int(player_pos_str[0])
    y = int(player_pos_str[-1])
    return x, y


def bot_random(board):
    t = TikTakToe(board)
    pos = random.choice(t.possible_moves)
    return pos


t = TikTakToe()
for i in range(200):
    m = MiniMax(game=t)
    print(f"{i}: {m.root.rating} (Nodes: {len(m.root.descendants)})")
