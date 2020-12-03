from typing import List, Dict, Callable, Tuple


class Solution:
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
