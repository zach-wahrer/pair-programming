import unittest

"""
You can move right or down. Find the path with the most diamonds.
0  1 0
0 -1 0
1  1 0
"""


# Dynamic recurisve solution
def most_diamonds(board: list) -> int:

    def _exit_value(board):
        exit = board[len(board) - 1][len(board[0]) - 1]
        if exit == -1:
            return float('-inf')
        return exit

    def _key_gen(row, col):
        if row in range(len(board)) and col in range(len(board[0])):
            if board[row][col] != -1:
                return (row, col)
        return 'wall'

    memoize = {'wall': float('-inf'), (len(board)-1, len(board[0])-1): _exit_value(board)}

    def _get_diamonds(row, col):
        key = _key_gen(row, col)

        if key not in memoize:
            down = _get_diamonds(row + 1, col)
            right = _get_diamonds(row, col + 1)

            if board[row][col] == 1:
                memoize[key] = 1 + max(down, right)
            else:
                memoize[key] = max(down, right)

        return memoize[key]

    max_diamonds = _get_diamonds(0, 0)
    return max_diamonds if max_diamonds != float('-inf') else -1


class TestGetMostDiamonds(unittest.TestCase):

    def test_easy_2(self):
        board = [
            [0,  1, 0],
            [0, -1, 0],
            [1,  1, 0]
        ]
        self.assertEqual(most_diamonds(board), 2)

    def test_deep_5(self):
        board = [
            [0,  1, 0],
            [0, -1, 0],
            [1,  1, 0],
            [1,  1, 0],
            [1,  1, 0],
            [1,  1, 0]
        ]
        self.assertEqual(most_diamonds(board), 5)

    def test_no_exit(self):
        board = [
            [0,  1, 0],
            [0, -1, 0],
            [1,  1, -1]
        ]
        self.assertEqual(most_diamonds(board), -1)

    def test_exit_diamond(self):
        board = [
            [0,  1, 1],
            [0, -1, 1],
            [1,  1, 1]
        ]
        self.assertEqual(most_diamonds(board), 4)


if __name__ == "__main__":
    unittest.main()
