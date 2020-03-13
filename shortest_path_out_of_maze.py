import unittest

"""
You can move right or down. Find the shortest path out, if one exists.
0 0 0 0 0
0-1-1-1-1
0 0 0 0 0
"""

board = [
    [0,  0],
    [-1,  0]
]


# Dynamic recurisve solution
def quickest_out(board: list) -> int:

    def _validate_exit(board):
        if board[len(board) - 1][len(board[0]) - 1] == 0:
            return 0
        else:
            return float('-inf')

    def _min_distance(board):
        return len(board) + len(board[0]) - 2

    def _get_key(row, col):
        if row in range(0, len(board)) and col in range(0, len(board[0])):
            if board[row][col] == 0:
                return(row, col)
        return 'wall'

    steps_to_finish = {'wall': float('-inf'),
                       (len(board)-1, len(board[0])-1): _validate_exit(board)}

    def _traverse_board(row, col):
        key = _get_key(row, col)

        if key not in steps_to_finish:
            right = _traverse_board(row, col + 1)
            down = _traverse_board(row + 1, col)
            steps_to_finish[key] = 1 + max(right, down)

        return steps_to_finish[key]

    farthest_progress = _traverse_board(0, 0)
    if farthest_progress == _min_distance(board):
        return farthest_progress
    return -1


class TestSteps(unittest.TestCase):

    def test_invalid_exit(self):
        board = [
            [0,  0, 0,  0, -1],
            [0, -1, 0,  0, -1],
            [0,  0, 0,  0,  0],
            [0,  0, 0, -1, 0],
            [0,  0, 0, -1,  -1]
        ]
        self.assertEqual(quickest_out(board), -1)

    def test_invalid_path(self):
        board = [
            [0,  0, 0,  0, -1],
            [0, -1, 0,  0, -1],
            [0,  0, 0,  0,  0],
            [0,  0, 0, -1, -1],
            [0,  0, 0, -1,  0]
        ]
        self.assertEqual(quickest_out(board), -1)

    def test_9_valid(self):
        board = [
            [0,  0, 0,  0,  0, 0],
            [0, -1, 0,  0, -1, 0],
            [0,  0, -1, 0,  0, 0],
            [0,  0, 0,  0, -1, 0],
            [0,  0, 0,  0,  0, 0]
        ]
        self.assertEqual(quickest_out(board), 9)


if __name__ == "__main__":
    unittest.main()
