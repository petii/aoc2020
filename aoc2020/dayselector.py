from pprint import pprint

from .days import day1, day2, day3


def daySelector(day: int, fileContents: str):
    if day == 1:
        input = list(
            map(int, filter(lambda x: x != '', fileContents.split('\n'))))
        solver = day1.Solution(input)
        print('Solving day1 puzzle with the following input:', *input[:10],
              '...', input[-1])
        pt1 = solver.part1()
        pt2 = solver.part2()
        print('  Part One: ', f'{pt1[0]} x {pt1[1]} = {pt1[2]}')
        print('  Part Two: ', f'{pt2[0]} x {pt2[1]} x {pt2[2]} = {pt2[3]}')
    if day == 2:
        input = list(filter(lambda x: x != '', fileContents.split('\n')))
        solver = day2.Solution(input)
        print('Solving day2 puzzle with the following input:', *input[:2],
              '...', input[-1])
        pt1 = solver.part1()
        pt2 = solver.part2()
        print('  Part One: ', pt1)
        print('  Part Two: ', pt2)
    if day == 3:
        input = list(filter(lambda x: x != '', fileContents.split('\n')))
        solver = day3.Solution(input)
        print('Solving day3 puzzle with the following input:', *input[:8],
              '             ...', *input[-3:], sep="\n    ")
        pt1 = solver.part1()
        # pt2 = solver.part2()
        print('  Part One: ', pt1[0])
        # print('  Part Two: ', pt2)