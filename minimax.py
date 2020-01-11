from TikTakToe.tiktaktoe import TikTakToe
import random
import numpy as np
from anytree import Node, RenderTree, AsciiStyle, LevelOrderIter


class MiniMax:
    def __init__(self, game=None, board=None, player=1):
        if isinstance(game, TikTakToe):
            self.game = game
        else:
            self.game = TikTakToe(board=board, player=player)

        self.me = self.game.player  # which player am I
        self.root = Node("root", game=self.game)
        self.make_tree()

    def make_tree(self):
        for node in LevelOrderIter(self.root, maxlevel=8):
            name_dict = {
                0: "draw",
                self.me: "win",
                -1 * self.me: "loss"
            }

            if node.game.winner is None:
                for pos in node.game.possible_moves:
                    Node(name=str(pos), parent=node, game=node.game.mark(pos))
            else:
                node.name = name_dict[node.game.winner]
                node.rating = node.game.winner

        # print(RenderTree(self.root).by_attr("name"))


if __name__ == "__main__":
    pass
