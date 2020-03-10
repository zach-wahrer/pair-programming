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

    def _inbounds(row, col):
        return row in range(0, len(board)) and col in range(0, len(board[0]))

    def _on_exit(row, col):
        return row == len(board) - 1 and col == len(board[0]) - 1

    possible_paths = []

    def _traverse_board(row, col, count, possible_paths):

        if _inbounds(row, col):
            if board[row][col] == 0:
                if _on_exit(row, col):
                    possible_paths.append(count)
                else:
                    _traverse_board(row + 1, col, count + 1, possible_paths)
                    _traverse_board(row, col + 1, count + 1, possible_paths)

    _traverse_board(0, 0, 0, possible_paths)

    if possible_paths:
        return min(possible_paths)
    return -1


print(steps_out(board))
