import unittest

from aoc2020.days import *

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

    def test_seatId(self) -> None:
        for input, expected in testinputs.day5pairs:
            self.assertEqual(expected, day5.seatId(input))

    def test_pt1(self) -> None:
        expected = 820
        result = self.day.part1()
        self.assertEqual(expected, result)


class TestDay6(unittest.TestCase):
    day = day6.Solution(testinputs.day6input)

    def test_summarizeGroupAny(self) -> None:
        for input, expected in testinputs.day6anypairs:
            self.assertEqual(expected, day6.summarizeGroupAny(input))

    def test_summarizeGroupEvery(self) -> None:
        for input, expected in testinputs.day6everypairs:
            self.assertEqual(expected, day6.summarizeGroupEvery(input))

    def test_pt1(self) -> None:
        expected = 11
        result = self.day.part1()
        self.assertEqual(expected, result)

    def test_pt2(self) -> None:
        expected = 6
        result = self.day.part2()
        self.assertEqual(expected, result)


class TestDay7(unittest.TestCase):
    def test_pt1(self) -> None:
        day = day7.Solution(testinputs.day7input)
        expected = 4
        result = day.part1()
        self.assertEqual(expected, result)

    def test_pt2(self) -> None:
        for input, expected in zip(
            [testinputs.day7input, testinputs.day7input2], [32, 126]):
            day = day7.Solution(input)
            result = day.part2()
            self.assertEqual(expected, result)


class TestDay8(unittest.TestCase):
    def test_pt1(self) -> None:
        expected = 5
        result = day8.part1(testinputs.day8input)
        self.assertEqual(expected, result)

    def test_pt2(self) -> None:
        expected = 8
        result = day8.part2(testinputs.day8input)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
