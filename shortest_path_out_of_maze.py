"""
You can move right or down. Find the shortest path out, if one exists.
0 0 0 0 0
0-1-1-1-1
0 0 0 0 0
"""

board = [
    [0,   0, 0,  0, -1],
    [-1, -1, 0,  0, -1],
    [-1, -1, 0,  0,  0],
    [-1,  0, -1, 0,  0]
]


# Brute Force solution
def steps_out(board: list) -> int:

    log = {}

    def _logger(key):
        if key not in log:
            log[key] = 0
            print("New key")
        else:
            log[key] += 1
            print(key, "count", log[key])

    def _inbounds(row, col):
        return row in range(0, len(board)) and col in range(0, len(board[0]))

    def _on_exit(row, col):
        return row == len(board) - 1 and col == len(board[0]) - 1

    def _traverse_board(row, col, count):
        _logger((row, col))
        if _inbounds(row, col):
            if board[row][col] == 0:
                if _on_exit(row, col):
                    return count

                return min(_traverse_board(row + 1, col, count + 1),
                           _traverse_board(row, col + 1, count + 1))

        return float('inf')

    moves = _traverse_board(0, 0, 0)
    return -1 if type(moves) == float else moves


print(steps_out(board))
