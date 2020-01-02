import unittest


class Board:
    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def make_move(self, row, col, player_char):
        pass

    def game_over(self):
        player_chars = ["x", "o"]
        for char in player_chars:
            if self.is_horizontal(char) or \
                    self.is_vertical(char) or \
                    self.is_diagonal(char):
                print(char, "won.")
                return True
            elif self.is_draw():
                print("Draw game.")
                return True
        return False

    def is_draw(self):
        row_filled = 0
        for row in self.board:
            if sum([1 for val in row if val is not None]) == 3:
                row_filled += 1
        if row_filled == 3:
            return True
        return False

    def three_matching_char(self, characters, player_char):
        if sum([1 for val in characters if val == player_char]) == 3:
            return True
        return False

    def is_horizontal(self, player_char):
        for row in self.board:
            if self.three_matching_char(row, player_char):
                return True
        return False

    def is_vertical(self, player_char):
        for col1, col2, col3 in zip(self.board[0],
                                    self.board[1], self.board[2]):
            column = [col1, col2, col3]
            if self.three_matching_char(column, player_char):
                return True
        return False

    def is_diagonal(self, player_char):
        diagonal1 = [self.board[0][0], self.board[1][1], self.board[2][2]]
        diagonal2 = [self.board[0][2], self.board[1][1], self.board[2][0]]
        return self.three_matching_char(diagonal1, player_char) or \
            self.three_matching_char(diagonal2, player_char)


class TestBoard(unittest.TestCase):

    def test_x_horizontal(self):
        board0 = Board()
        board0.board = [
            ["x", "x", "x"]
        ]
        self.assertTrue(board0.game_over())

    def test_draw_game(self):
        board0 = Board()
        board0.board = [
            ["x", "o", "x"],
            ["o", "x", "x"],
            ["o", "x", "o"]
        ]
        self.assertTrue(board0.game_over())

    # Add testing for other cases


unittest.main()
