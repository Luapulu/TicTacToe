from TikTakToe.tiktaktoe import TikTakToe
from random import shuffle
import numpy as np
from anytree import AnyNode, PreOrderIter, PostOrderIter


class MiniMax:
    def __init__(self, game=None):
        if isinstance(game, TikTakToe):
            self.game = game
        else:
            raise TypeError(f"game must be a game of TikTakToe, not {type(game)}")

        self.me = self.game.player  # which player am I
        self.root = AnyNode(pos=None)

        self.rate_dict = {}

        self.root.rating = self.rate(game=self.game, node=self.root)

    def rate(self, game, node):
        try:
            value = self.rate_dict[str(game)]
        except KeyError:
            l = list(game.possible_moves)
            shuffle(l)
            if game.winner is not None:
                value = game.winner

            elif game.player == 1:
                value = -1
                for pos in l:
                    game.mark(pos)
                    r = self.rate(game=game, node=AnyNode(pos=pos, parent=node))
                    game.un_mark(pos)

                    value = max(value, r)

                    if value == 1:
                        break

            else:
                value = 1
                for pos in l:
                    game.mark(pos)
                    r = self.rate(game=game, node=AnyNode(pos=pos, parent=node))
                    game.un_mark(pos)

                    value = min(value, r)

                    if value == -1:
                        break

            self.rate_dict[str(game)] = value

        node.rating = value
        return node.rating


if __name__ == "__main__":
    pass
