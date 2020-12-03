import unittest

import days

class TestDays(unittest.TestCase):
    def test_day1(self):
        input = list(map(int,"1721 979 366 299 675 1456".split(' ')))
        expected = 514579
        result = days.day1(input)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
