import unittest

from aoc2020.days import day1, day2, day3, day4, day5

from test import testinputs


class TestDay1(unittest.TestCase):
    day = day1.Solution(testinputs.day1input)

    def test_pt1(self) -> None:
        expected = 514579
        result = self.day.part1()[2]
        self.assertEqual(expected, result)

    def test_pt2(self) -> None:
        expected = 241861950
        result = self.day.part2()[3]
        self.assertEqual(expected, result)


class TestDay2(unittest.TestCase):
    day = day2.Solution(testinputs.day2input)

    def test_pt1(self) -> None:
        expected = 2
        result = self.day.part1()
        self.assertEqual(expected, result)

    def test_pt2(self) -> None:
        expected = 1
        result = self.day.part2()
        self.assertEqual(expected, result)


class TestDay3(unittest.TestCase):
    day = day3.Solution(testinputs.day3input)

    def test_pt1(self) -> None:
        expected = 7
        result = self.day.part1()[0]
        self.assertEqual(expected, result)

    def test_pt2(self) -> None:
        expected = 336
        result = self.day.part2()
        self.assertEqual(expected, result)


class TestDay4(unittest.TestCase):
    input = testinputs.day4input + testinputs.day4valid + testinputs.day4invalid
    day = day4.Solution(input)

    def test_pt1(self) -> None:
        expected = 2 + len(testinputs.day4valid) + len(testinputs.day4invalid)
        result = self.day.part1()
        self.assertEqual(expected, result)

    def test_pt2(self) -> None:
        expected = 2 + len(testinputs.day4valid)
        result = self.day.part2()
        self.assertEqual(expected, result)


class TestDay5(unittest.TestCase):
    day = day5.Solution(testinputs.day5input)

    def test_seatId(self):
        for input, expected in testinputs.day5pairs:
            self.assertEqual(expected, day5.seatId(input))

    def test_pt1(self) -> None:
        expected = 820
        result = self.day.part1()
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
