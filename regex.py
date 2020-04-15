import unittest


class regex:
    def string_match(expression: str, string: str) -> bool:
        if '.' in expression and len(expression) <= len(string):
            string = [char for char in string]
            expression = [char for char in expression]

            for index, string_char in enumerate(string):
                if string_char == expression[0] or expression[0] == '.':
                    e_idx = 1
                    s_idx = index + 1

                    while e_idx < len(expression):
                        if expression[e_idx] != '.' and expression[e_idx] != string[s_idx]:
                            break
                        e_idx += 1
                        s_idx += 1
                    else:
                        return True
            return False

        elif len(expression) >= len(string):
            return False

        else:
            return True if expression in string else False


class TestRegex(unittest.TestCase):

    # Passing
    def test_basic_true(self):
        self.assertTrue(regex.string_match('a', 'aaa'))

    def test_basic2_true(self):
        self.assertTrue(regex.string_match('1', '212'))

    def test_basic_false(self):
        self.assertFalse(regex.string_match('a', 'bbb'))

    def test_wildcard_false(self):
        self.assertFalse(regex.string_match('.', ''))

    def test_adv_wildcard_a_true(self):
        self.assertTrue(regex.string_match('a.', 'ab'))

    def test_adv_wildcard_aa_true(self):
        self.assertTrue(regex.string_match('a.a.', 'abab'))

    def test_wildcard_single_true(self):
        self.assertTrue(regex.string_match('.', 'zzz'))

    def test_adv_wildcard_middle_a_true(self):
        self.assertTrue(regex.string_match('.a.', 'zaz'))

    def test_adv_wildcard_123z_true(self):
        self.assertTrue(regex.string_match('...z', '123z'))

    def test_adv_wildcard_too_short_z_false(self):
        self.assertFalse(regex.string_match('.z', 'z'))

    def test_adv_wildcard_too_short_12_false(self):
        self.assertFalse(regex.string_match('...', '12'))

    def test_adv_wildcard_21cd_false(self):
        self.assertFalse(regex.string_match('12..', '21cd'))


if __name__ == "__main__":
    unittest.main()
