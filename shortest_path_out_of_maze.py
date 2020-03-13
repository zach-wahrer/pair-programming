import unittest

"""
You can move right or down. Find the shortest path out, if one exists.
0 0 0 0 0
0-1-1-1-1
0 0 0 0 0
"""

board = [
    [0,  0, 0,  0, -1],
    [0, -1, 0,  0, -1],
    [0,  0, 0,  0,  0],
    [0,  0, 0,  0,  0],
    [0,  0, 0, -1,  0]
]


# Dynamic recurisve solution
def steps_out(board: list) -> int:

    seen = set()

    def _visited(key):
        if key not in seen:
            seen.add(key)
            return False
        return True

    def _inbounds(row, col):
        return row in range(0, len(board)) and col in range(0, len(board[0]))

    def _on_exit(row, col):
        return row == len(board) - 1 and col == len(board[0]) - 1

    def _traverse_board(row, col, count):
        if _inbounds(row, col) and not _visited((row, col)):
            if board[row][col] == 0:
                if _on_exit(row, col):
                    return count

                return min(_traverse_board(row + 1, col, count + 1),
                           _traverse_board(row, col + 1, count + 1))

        return float('inf')

    moves = _traverse_board(0, 0, 0)
    return -1 if type(moves) == float else moves


class TestSteps(unittest.TestCase):

    def test_easy_8(self):
        board = [
            [0,  0, 0,  0, -1],
            [0, -1, 0,  0, -1],
            [0,  0, 0,  0,  0],
            [0,  0, 0,  0,  0],
            [0,  0, 0, -1,  0]
        ]
        self.assertEqual(steps_out(board), 8)

    def test_hard_9(self):
        board = [
            [0,  0, 0,  0,  0, 0],
            [0, -1, 0,  0, -1, 0],
            [0,  0, -1, 0,  0, 0],
            [0,  0, 0,  0, -1, 0],
            [0,  0, 0,  0,  0, 0]
        ]
        self.assertEqual(steps_out(board), 9)


if __name__ == "__main__":
    unittest.main()
