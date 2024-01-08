import unittest

from main import is_palindrome

class PalindromeTest(unittest.TestCase):
    
    def test_is_palindrome_ok(self):
        for s in ["a", "aa", "aba", "abba", "abcba"]:
            self.assertTrue(is_palindrome(s))
    
    def test_is_palindrome_no(self):
        for s in ["ab", "abc", "abab", "abca", "abbc", "abcb"]:
            self.assertFalse(is_palindrome(s))

    # def test_is_palindrome_raise_typeerror(self):
    #     for i in [3.14, 1, [1, 2, 3]]:
    #         with self.assertRaises(TypeError):
    #             is_palindrome(i)


if __name__ == "__main__":
    unittest.main()