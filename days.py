from pprint import pprint
from typing import List, Dict, Callable, Tuple


class Day1:
    input: List[int]

    def __init__(self, input: List[int]):
        self.input = input

    def _part1(self, input: List[int], sum: int) -> Tuple[int, int, int]:
        for index in range(0, len(input) - 1):
            current = input[index]
            rest: List[int] = input[index + 1:]
            result = next((x for x in rest if x == sum - current), None)
            if result != None:
                return (current, result, current * result)

    def part1(self) -> Tuple[int, int, int]:
        return self._part1(self.input, 2020)

    def part2(self) -> int:
        for index in range(0, len(self.input) - 2):
            current = self.input[index]
            rest: List[int] = self.input[index + 1:]
            result = self._part1(rest, 2020 - current)
            if result != None:
                return (current, result[0], result[1], result[2] * current)


class Day2:
    input: List[str]

    def __init__(self, input):
        self.input = input

    def part1(self) -> int:
        return len(list(filter(self.match, self.input)))

    def part2(self) -> int:
        return len(list(filter(self.match2, self.input)))

    def match(self, line) -> bool:
        policy = self.policy(line)
        password = self.password(line)
        count = password.count(policy['char'])
        if count >= policy['min'] and count <= policy['max']:
            return True
        return False

    def match2(self, line) -> bool:
        policy = self.policy(line)
        password = self.password(line)
        pos1 = policy['min'] - 1
        pos2 = policy['max']
        sub = password[pos1:pos2]
        chars = sub[::len(sub) - 1]
        if chars.count(policy['char']) == 1:
            return True
        return False

    def policy(self, line: str) -> Dict:
        policyPart = line.split(': ')[0].split(' ')
        character = policyPart[1]
        occurences = list(map(int, policyPart[0].split('-')))
        return {'char': character, 'min': occurences[0], 'max': occurences[1]}

    def password(self, line: str) -> str:
        return line.split(': ')[1]


def daySelector(day: int, fileContents: str):
    if day == 1:
        input = list(
            map(int, filter(lambda x: x != '', fileContents.split('\n'))))
        day = Day1(input)
        print('Solving day1 puzzle with the following input:', *input[:10],
              '...', input[-1])
        pt1 = day.part1()
        pt2 = day.part2()
        print('  Part One: ', f'{pt1[0]} x {pt1[1]} = {pt1[2]}')
        print('  Part Two: ', f'{pt2[0]} x {pt2[1]} x {pt2[2]} = {pt2[3]}')
    if day == 2:
        input = list(filter(lambda x: x != '', fileContents.split('\n')))
        day = Day2(input)
        print('Solving day2 puzzle with the following input:', *input[:2],
              '...', input[-1])
        pt1 = day.part1()
        pt2 = day.part2()
        print('  Part One: ', pt1)
        print('  Part Two: ', pt2)
