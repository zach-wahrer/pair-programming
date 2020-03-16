import unittest

"""
You can move right or down. Find the path with the most diamonds.
0  1 0
0 -1 0
1  1 0
"""


# Dynamic recurisve solution
class GetMaxDiamonds:
    def __init__(self, board):
        self.board = board
        self.exit = board[len(board) - 1][len(board[0]) - 1]
        self.row_len = len(board)
        self.col_len = len(board[0])
        self.memoize = {'wall': float('-inf'),
                        (len(self.board)-1, len(self.board[0])-1): self._exit_value()}

    def get(self):
        max_diamonds = self._get_diamonds(0, 0)
        return max_diamonds if max_diamonds != float('-inf') else -1

    def _exit_value(self):
        if self.exit == -1:
            return float('-inf')
        return self.exit

    def _key_gen(self, row, col):
        if row in range(self.row_len) and col in range(self.col_len):
            if self.board[row][col] != -1:
                return (row, col)
        return 'wall'

    def _get_diamonds(self, row, col):
        key = self._key_gen(row, col)

        if key not in self.memoize:
            down = self._get_diamonds(row + 1, col)
            right = self._get_diamonds(row, col + 1)

            if self.board[row][col] == 1:
                self.memoize[key] = 1 + max(down, right)
            else:
                self.memoize[key] = max(down, right)

        return self.memoize[key]


class TestGetMostDiamonds(unittest.TestCase):

    def test_easy_2(self):
        board = [
            [0,  1, 0],
            [0, -1, 0],
            [1,  1, 0]
        ]
        self.assertEqual(GetMaxDiamonds(board).get(), 2)

    def test_deep_5(self):
        board = [
            [0,  1, 0],
            [0, -1, 0],
            [1,  1, 0],
            [1,  1, 0],
            [1,  1, 0],
            [1,  1, 0]
        ]
        self.assertEqual(GetMaxDiamonds(board).get(), 5)

    def test_no_exit(self):
        board = [
            [0,  1, 0],
            [0, -1, 0],
            [1,  1, -1]
        ]
        self.assertEqual(GetMaxDiamonds(board).get(), -1)

    def test_exit_diamond(self):
        board = [
            [0,  1, 1],
            [0, -1, 1],
            [1,  1, 1]
        ]
        self.assertEqual(GetMaxDiamonds(board).get(), 4)


if __name__ == "__main__":
    unittest.main()
