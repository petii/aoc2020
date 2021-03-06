from pprint import pprint
from typing import Callable, Dict

from days import *

_dayDict: Dict[str, Callable] = {}


def registerday(function: Callable) -> Callable:
    _dayDict[function.__name__] = function
    return function


@registerday
def _day_1(contents: str) -> None:
    input = list(map(int, filter(lambda x: x != '', contents.split('\n'))))
    solver = day1.Solution(input)
    print('Solving day1 puzzle with the following input:', *input[:10], '...',
          input[-1])
    pt1 = solver.part1()
    pt2 = solver.part2()
    print('  Part One: ', f'{pt1[0]} x {pt1[1]} = {pt1[2]}')
    print('  Part Two: ', f'{pt2[0]} x {pt2[1]} x {pt2[2]} = {pt2[3]}')


@registerday
def _day_2(contents: str) -> None:
    input = list(filter(lambda x: x != '', contents.split('\n')))
    solver = day2.Solution(input)
    print('Solving day2 puzzle with the following input:', *input[:2], '...',
          input[-1])
    pt1 = solver.part1()
    pt2 = solver.part2()
    print('  Part One: ', pt1)
    print('  Part Two: ', pt2)


@registerday
def _day_3(contents: str) -> None:
    input = list(filter(lambda x: x != '', contents.split('\n')))
    solver = day3.Solution(input)
    print('Solving day3 puzzle with the following input:',
          *input[:8],
          '             ...',
          *input[-3:],
          sep="\n    ")
    pt1 = solver.part1()
    pt2 = solver.part2()
    print('  Part One: ', pt1[0])
    print('  Part Two: ', pt2)


@registerday
def _day_4(contents: str) -> None:
    input = contents.split('\n\n')
    solver = day4.Solution(input)
    print('Solving day4 puzzle')
    print('  Part One: ', solver.part1())


@registerday
def _day_5(contents: str) -> None:
    input = list(filter(lambda x: x != '', contents.split('\n')))
    solver = day5.Solution(input)
    print('Solving day5 puzzle')
    print('  Part One: ', solver.part1())
    print('  Part Two: ', solver.part2())


@registerday
def _day_6(contents: str) -> None:
    input = contents.split('\n\n')
    solver = day6.Solution(input)
    print('Solving day6 puzzle')
    print('  Part One: ', solver.part1())
    print('  Part Two: ', solver.part2())


@registerday
def _day_7(contents: str) -> None:
    input = list(filter(lambda x: x != '', contents.split('\n')))
    solver = day7.Solution(input)
    print('Solving day7 puzzle')
    print('  Part One: ', solver.part1())
    print('  Part Two: ', solver.part2())


@registerday
def _day_8(contents: str) -> None:
    input = list(filter(lambda x: x != '', contents.split('\n')))
    print('Solving day8 puzzle')
    print('  Part One: ', day8.part1(input))
    print('  Part Two: ', day8.part2(input))


def daySelector(day: int, fileContents: str) -> None:
    _dayDict[f'_day_{day}'](fileContents)
