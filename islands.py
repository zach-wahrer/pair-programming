"""
Given a 2d grid map of '1's(land) and '0's(water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all
surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011
-
Output: 3
"""

board = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]


def island_count(board):

    def key_gen(row, col):
        if row in range(0, len(board)) and col in range(0, len(board[0])):
            return (row, col)
        return "stop"

    def _assimilate(row, col):
        key = key_gen(row, col)
        if key == 'stop':
            return
        if key not in memoize and board[row][col]:
            memoize[key] = True
            _assimilate(row + 1, col)
            _assimilate(row, col + 1)

    memoize = {}

    def _island_count(row, col, count):
        if row == len(board):
            return count

        key = key_gen(row, col)
        if key == 'stop':
            return _island_count(row + 1, 0, count)

        if key not in memoize and board[row][col]:
            count += 1
            _assimilate(row, col)

        return _island_count(row, col + 1, count)

    return _island_count(0, 0, 0)


print(island_count(board))
