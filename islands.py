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


class World:
    def __init__(self, board):
        self.board = board
        self.memoize = set()
        self.count = 0
        self._island_count(0, 0)

    def key_gen(self, row, col):
        if row in range(0, len(self.board)) and col in range(0, len(self.board[0])):
            return (row, col)
        return "stop"

    def _assimilate(self, row, col):
        key = self.key_gen(row, col)
        if key == 'stop':
            return
        if key not in self.memoize and self.board[row][col]:
            self.memoize.add(key)
            self._assimilate(row + 1, col)
            self._assimilate(row, col + 1)

    def _island_count(self, row, col):
        if row == len(self.board):
            return

        key = self.key_gen(row, col)
        if key == 'stop':
            return self._island_count(row + 1, 0)

        if key not in self.memoize and self.board[row][col]:
            self.count += 1
            self._assimilate(row, col)

        return self._island_count(row, col + 1)


print(World(board).count)
