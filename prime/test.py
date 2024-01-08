import unittest

from main import is_prime_v1

class PrimeTest(unittest.TestCase):

    def test_is_prime_ok(self):
        for i in [2, 3, 5, 7, 11, 13, 17, 19]:
            self.assertTrue(is_prime_v1(i))
    
    def test_is_prime_no(self):
        for i in [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]:
            self.assertFalse(is_prime_v1(i))

    def test_is_prime_negative(self):
        for i in [-1, -2, -3, -4, -5]:
            self.assertFalse(is_prime_v1(i))

    def test_is_prime_raise_typeerror(self):
        for i in [3.14, "hello", [1, 2, 3]]:
            with self.assertRaises(TypeError):
                is_prime_v1(i)


if __name__ == "__main__":
    unittest.main()