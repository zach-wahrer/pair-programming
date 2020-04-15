import unittest


class regex:
    def string_match(expression: str, string: str) -> bool:
        if '.' in expression and len(expression) <= len(string):
            str_chars = [char for char in string]
            exp_chars = [char for char in expression]

            for str_idx, str_char in enumerate(str_chars):
                if str_char == exp_chars[0] or exp_chars[0] == '.':
                    exp_idx = 1
                    iter_str_idx = str_idx
                    while exp_idx < len(exp_chars):
                        if exp_chars[exp_idx] != '.' and str_chars[str_idx] != exp_chars[exp_idx]:
                            break
                        exp_idx += 1
                        iter_str_idx += 1
                    else:
                        return True
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

    def test_wildcard_true(self):
        self.assertTrue(regex.string_match('.', 'zzz'))

    def test_adv_wildcard_wilda_true(self):
        self.assertTrue(regex.string_match('.a.', 'zaz'))

    def test_adv_wildcard_123z_true(self):
        self.assertTrue(regex.string_match('...z', '123z'))

    def test_adv_wildcard_123a_wild_false(self):
        self.assertFalse(regex.string_match('123.', '123'))

    def test_adv_wildcard_z_false(self):
        self.assertFalse(regex.string_match('.z', 'z'))

    def test_adv_wildcard_too_short_false(self):
        self.assertFalse(regex.string_match('...', '12'))

    def test_adv_wildcard_2112_false(self):
        self.assertFalse(regex.string_match('12..', '2112'))


if __name__ == "__main__":
    unittest.main()
