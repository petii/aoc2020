import unittest

from aoc2020.days import day1, day2, day3, day4


class TestDay1(unittest.TestCase):
    input = list(map(int, "1721 979 366 299 675 1456".split(' ')))
    day = day1.Solution(input)

    def test_pt1(self) -> None:
        expected = 514579
        result = self.day.part1()[2]
        self.assertEqual(expected, result)

    def test_pt2(self) -> None:
        expected = 241861950
        result = self.day.part2()[3]
        self.assertEqual(expected, result)


class TestDay2(unittest.TestCase):
    input = list(
        map(
            lambda line: line.strip(), """1-3 a: abcde
                                          1-3 b: cdefg
                                          2-9 c: ccccccccc""".split('\n')))
    day = day2.Solution(input)

    def test_pt1(self) -> None:
        expected = 2
        result = self.day.part1()
        self.assertEqual(expected, result)

    def test_pt2(self) -> None:
        expected = 1
        result = self.day.part2()
        self.assertEqual(expected, result)


class TestDay3(unittest.TestCase):
    input = list(
        map(
            lambda line: line.strip(), """..##.......
                                          #...#...#..
                                          .#....#..#.
                                          ..#.#...#.#
                                          .#...##..#.
                                          ..#.##.....
                                          .#.#.#....#
                                          .#........#
                                          #.##...#...
                                          #...##....#
                                          .#..#...#.#""".split('\n')))
    day = day3.Solution(input)

    def test_pt1(self) -> None:
        expected = 7
        result = self.day.part1()[0]
        self.assertEqual(expected, result)

    def test_pt2(self) -> None:
        expected = 336
        result = self.day.part2()
        self.assertEqual(expected, result)


day4input: str = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


class TestDay4(unittest.TestCase):
    day = day4.Solution(day4input.split('\n\n'))

    def test_pt1(self) -> None:
        expected = 2
        result = self.day.part1()
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
