import unittest

import days

class TestDay1(unittest.TestCase):
    input = list(map(int,"1721 979 366 299 675 1456".split(' ')))
    day = days.Day1(input)

    def test_pt1(self):
        expected = 514579
        result = self.day.part1()[2]
        self.assertEqual(expected, result)

    def test_pt2(self):
        expected =241861950
        result = self.day.part2()[3]
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
