import numpy as np


class TikTakToe:
    empty = np.zeros((3, 3), dtype=np.int8)

    def __init__(self, board=None, player=1):
        if board is None:
            self.board = TikTakToe.empty
        elif self._check_board_valid(board):
            self.board = board

        if type(player) is int:
            if player in [-1, 1]:  # Player 1 is 1 and player 2 is -1
                self.player = int(player)
            else:
                raise ValueError("Player must be 1 or -1")
        else:
            raise TypeError(f"Player must be type int, not {type(player)}")

    def mark(self, pos, inplace=False):
        if self.winner is None:
            if self.board[pos] == 0:
                try:
                    if inplace:
                        self.board[pos] = self.player

                        # Other player's turn now
                        self.player *= -1
                    else:
                        b = self.board.copy()
                        b[pos] = self.player

                        p = self.player * -1

                        return TikTakToe(board=b, player=p)

                except IndexError:
                    raise IndexError(f"{pos} is outside board")
            else:
                raise IndexError(f"Board already marked at {pos}")

    @property
    def winner(self):
        """Returns winner of game
        1 : Player 1 has won
        -1 : PLayer 2 has won
        0 : Draw
        None: No winner yet"""

        # check rows
        if any(abs(self.board.sum(axis=1)) == 3):
            s = self.board.sum(axis=1)
            return s[abs(s) == 3][0] // 3

        # check columns
        if any(abs(self.board.sum(axis=0)) == 3):
            s = self.board.sum(axis=0)
            return s[abs(s) == 3][0] // 3

        # check diagonal 0
        elif abs(np.diag(self.board).sum()) == 3:
            return np.diag(self.board).sum() // 3

        # check other diagonal
        elif abs(np.diag(np.fliplr(self.board)).sum()) == 3:
            return np.diag(np.fliplr(self.board)).sum() // 3

        # draw if all positions filled but still no winner
        elif not (self.board == 0).any():
            return 0

        # None is returned automatically if no other condition has been met

    @property
    def possible_moves(self):
        return tuple(zip(*np.where(self.board == 0)))

    @staticmethod
    def _check_board_valid(board):
        if type(board) is np.ndarray:
            if board.shape == (3, 3):
                if np.logical_or(abs(board) == 1, board == 0).all():
                    return True
                else:
                    raise ValueError("Board must contain only 1, -1 and 0")
            else:
                raise ValueError(f"Board must have shape (3, 3), not {board.shape}")
        else:
            raise TypeError(f"Board must be ndarray, not {type(board)}")

    def __repr__(self):
        return str(self.board)
