import unittest
from sumDigitString import *

class TestSumDigitStrings(unittest.TestCase):
    # tests a string with no number in it
    def test_nonumber(self):
        self.assertEqual(sumDigitString("abc"), 0)
    
    # tests a string with number 123 in it and checks if it equals to 6
    def test_withnumber(self):
        self.assertEqual(sumDigitString("abc123"), 6)

    # tests a hex number in abc123 it. Checks if number in it adds up to 33
    def test_hexnumber(self):
        self.assertEqual(sumDigitString("-x", "abc123"), 33)

    # tests a file input that has "He2ll4o" in it. Check if it equals to 6
    def test_file(self):
        self.assertEqual(sumDigitString("-f", "files.txt"), 6)

    # tests a invalid input. Check if it equals to None
    def test_invalid(self):
        self.assertEqual(sumDigitString(123), None)


if __name__ == "__main__":
    unittest.main()