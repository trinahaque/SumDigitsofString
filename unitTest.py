import unittest
from sumDigitString import *

class TestSumDigitStrings(unittest.TestCase):
    # tests a string with no number in it
    def test_nonumber(self):
        self.assertEqual(sumDigitString("abc"), 0)
    
    # tests a string with number in it
    def test_withnumber(self):
        self.assertEqual(sumDigitString("abc123"), 6)

    # tests a hex number in it
    def test_hexnumber(self):
        self.assertEqual(sumDigitString("-x", "abc123"), 33)

    # tests a file input
    def test_file(self):
        self.assertEqual(sumDigitString("-f", "files.txt"), 6)


if __name__ == "__main__":
    unittest.main()