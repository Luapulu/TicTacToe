import numpy as np


class TikTakToe:
    def __init__(self, board=None):
        if board is None:
            self.board = np.zeros((3, 3), dtype=np.int8)
        elif self._check_board_valid(board):
            self.board = board.astype(dtype=np.int8)

    def mark(self, pos, inplace=True):
        if self.winner is None:
            if pos in self.zero_positions:
                if inplace:
                    self.board[pos] = self.player
                else:
                    b = self.board.copy()
                    b[pos] = self.player

                    return TikTakToe(board=b)
            elif 0 > pos[0] or pos[0] >= 3 or 0 > pos[1] or pos[1] >= 3:
                raise IndexError(f"{pos} is outside board")
            else:
                raise IndexError(f"board marked at {pos} already")

    def un_mark(self, pos, inplace=True):
        if pos in self.possible_undos:
            if inplace:
                self.board[pos] = 0
            else:
                b = self.board.copy()
                b[pos] = 0

                return TikTakToe(board=b)
        elif 0 > pos[0] or pos[0] >= 3 or 0 > pos[1] or pos[1] >= 3:
            raise IndexError(f"{pos} is outside board")
        else:
            raise IndexError(f"Player {-1 * self.player} cannot un-mark board at {pos}")

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
    def zero_positions(self):
        return tuple(zip(*np.where(self.board == 0)))

    @property
    def possible_undos(self):
        return tuple(zip(*np.where(self.board == -1 * self.player)))

    @property
    def player(self):
        try:
            sum_turn_dict = {
                0: 1,
                1: -1
            }
            return sum_turn_dict[self.board.sum()]
        except KeyError:
            raise ValueError("Invalid board: cannot determine whose turn it is")

    @staticmethod
    def _check_board_valid(board):
        if type(board) is np.ndarray:
            if board.shape == (3, 3):
                if np.logical_or(abs(board) == 1, board == 0).all():
                    if board.sum() in [0, 1]:
                        return True
                    else:
                        raise ValueError("Invalid board: cannot determine whose turn it is")
                else:
                    raise ValueError("Board must contain only 1, -1 and 0")
            else:
                raise ValueError(f"Board must have shape (3, 3), not {board.shape}")
        else:
            raise TypeError(f"Board must be ndarray, not {type(board)}")

    def __repr__(self):
        return self.board.__repr__()

    def __str__(self):
        return str(self.board)

