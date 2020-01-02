import unittest
import math


class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def sum(self, numbers):  # Take in an array of nums
        sum = 0
        for i in numbers:
            sum += i
        return sum

    def max(self, numbers):  # Find max of list of nums
        return max(numbers)

    def mod(self, x, y):
        return x % y

    def square(self, x):
        return x**2

    def square_root(self, x):
        return math.sqrt(x)


class TestCalculator(unittest.TestCase):

    def test_add_zeroes(self):
        x = 0
        y = 0
        ans = 0
        self.assertEqual(Calculator().add(x, y), ans)

    def test_add_simple(self):
        x = 1
        y = 1
        ans = 2
        self.assertEqual(Calculator().add(x, y), ans)

    def test_add_five_five(self):
        x = 5
        y = 5
        ans = 10
        self.assertEqual(Calculator().add(x, y), ans)

    def test_subtract_five_five(self):
        x = 5
        y = 5
        ans = 0
        self.assertEqual(Calculator().subtract(x, y), ans)

    def test_subtract_8_10(self):
        x = 8
        y = 10
        ans = -2
        self.assertEqual(Calculator().subtract(x, y), ans)

    def test_multiply_five_five(self):
        x = 5
        y = 5
        ans = 25
        self.assertEqual(Calculator().multiply(x, y), ans)

    def test_multiply_ten_zero(self):
        x = 10
        y = 0
        ans = 0
        self.assertEqual(Calculator().multiply(x, y), ans)

    def test_divide_50_4(self):
        x = 50
        y = 4
        ans = 12.5
        self.assertEqual(Calculator().divide(x, y), ans)

    def test_divide_20_5(self):
        x = 20
        y = 5
        ans = 4
        self.assertEqual(Calculator().divide(x, y), ans)

    def test_sum_minus_11519(self):
        nums = [-1, -1, -5, -1, -9]
        ans = -17
        self.assertEqual(Calculator().sum(nums), ans)

    def test_sum_8892310(self):
        nums = [8, 8, 9, 2, 3, 1, 0]
        ans = 31
        self.assertEqual(Calculator().sum(nums), ans)

    def test_sum_mixed_3149(self):
        nums = [3, 1, 4, -9]
        ans = -1
        self.assertEqual(Calculator().sum(nums), ans)

    def test_max_1469(self):
        nums = [1, 4, 6, 9]
        ans = 9
        self.assertEqual(Calculator().max(nums), ans)

    def test_max_01000139(self):
        nums = [0, 1000, 13, -9]
        ans = 1000
        self.assertEqual(Calculator().max(nums), ans)

    def test_mod_10_2(self):
        x = 10
        y = 2
        ans = 0
        self.assertEqual(Calculator().mod(x, y), ans)

    def test_mod_4_3(self):
        x = 4
        y = 3
        ans = 1
        self.assertEqual(Calculator().mod(x, y), ans)

    def test_mod_1000_977(self):
        x = 1000
        y = 977
        ans = 23
        self.assertEqual(Calculator().mod(x, y), ans)

    def test_square_50(self):
        x = 50
        ans = 2500
        self.assertEqual(Calculator().square(x), ans)

    def test_square_10(self):
        x = -10
        ans = 100
        self.assertEqual(Calculator().square(x), ans)

    def test_square_root_25(self):
        x = 25
        ans = 5
        self.assertEqual(Calculator().square_root(x), ans)

    def test_square_root_49(self):
        x = 49
        ans = 7
        self.assertEqual(Calculator().square_root(x), ans)


if __name__ == "__main__":
    unittest.main()
