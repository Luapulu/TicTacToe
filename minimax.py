from TicTacToe.tictactoe import TicTacToe
import numpy as np


class MiniMax:
    def __init__(self):
        self.rate_dict = {}
        self.optimal = {
            1: max,
            -1: min
        }
        self.positions_evaluated = 0
        self.branch_difficulty_weighting = 0.1

    def rate(self, game):
        if str(game) in self.rate_dict:
            value = self.rate_dict[str(game)]
        elif game.winner is not None:
            value = game.winner * (len(game.zero_positions) + 1)
        else:
            ratings = []
            for pos in game.zero_positions:
                game.mark(pos)
                r = self.rate(game=game)
                game.un_mark(pos)

                ratings.append(r)

            value = self.optimal[game.player](ratings)

            branch_difficulty = sum(x * game.player < 0 for x in ratings) / len(ratings)
            value -= game.player * self.branch_difficulty_weighting * branch_difficulty

        self.rate_dict[str(game)] = value

        # Use symmetry (flip and three rotations)
        self.rate_dict[str(np.rot90(game.board, k=1))] = value
        self.rate_dict[str(np.rot90(game.board, k=2))] = value
        self.rate_dict[str(np.rot90(game.board, k=3))] = value

        flipped_board = game.board.T
        self.rate_dict[str(flipped_board)] = value
        self.rate_dict[str(np.rot90(flipped_board, k=1))] = value
        self.rate_dict[str(np.rot90(flipped_board, k=2))] = value
        self.rate_dict[str(np.rot90(flipped_board, k=3))] = value

        self.positions_evaluated += 1
        return value

    def best_move(self, board):
        game = TicTacToe(board)
        pos_list = [(pos, self.rate(game.mark(pos, inplace=False))) for pos in game.zero_positions]
        return self.optimal[game.player](pos_list, key=lambda tup: tup[1])[0]


if __name__ == "__main__":
    pass
