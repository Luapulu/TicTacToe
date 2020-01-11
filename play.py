from TikTakToe.tiktaktoe import TikTakToe
from TikTakToe.minimax import MiniMax
import random
import matplotlib.pyplot as plt
import numpy as np


def human_play(board):
    print("\n")
    print(board)
    print("\n")

    player_pos_str = input("Type move x, y: ")
    x = int(player_pos_str[0])
    y = int(player_pos_str[-1])
    return x, y


def random_test_bot():
    n = 1000
    wins = np.zeros(n)
    for i in range(n):
        t = TikTakToe()
        while t.winner is None:
            p = random.choice(t.possible_moves)
            t.mark(p)
        wins[i] = t.winner

    plt.hist(wins)
    plt.show()


t = TikTakToe()
for _ in range(1):
    p = random.choice(t.possible_moves)
    t.mark(p)

m = MiniMax()

print(f"\nI am player {m.me}")
print(f"Turn: player {m.root.game.player}\n")
print(m.root.game)

for i in range(1000):
    m_test = MiniMax()
    if not (m_test.root.game.board == TikTakToe.empty).all():
        raise KeyboardInterrupt(f"Not the same:\n{m_test.root.game.board}")
    else:
        print(i)
