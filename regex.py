import unittest


class regex:
    def string_match(expression: str, string: str) -> bool:
        if '.' in expression:
            return True if string else False
        return True if expression in string else False


class TestRegex(unittest.TestCase):
    def test_basic_true(self):
        self.assertTrue(regex.string_match('a', 'aaa'))

    def test_basic_false(self):
        self.assertFalse(regex.string_match('a', 'bbb'))

    def test_wildcard_true(self):
        self.assertTrue(regex.string_match('.', 'aaa'))

    def test_wildcard_false(self):
        self.assertFalse(regex.string_match('.', ''))


if __name__ == "__main__":
    unittest.main()
