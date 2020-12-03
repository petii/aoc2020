from functools import reduce
from typing import Callable, Dict, List, Tuple


class Solution:
    input: List[str]
    width: int

    def __init__(self, input: List[str]):
        self.input = input
        self.width = len(input[0])

    def path(self, left, down) -> str:
        line = "".join([
            self.input[i * down][(i * left) % self.width]
            for i in range(0,
                           len(self.input) // down)
        ])
        return line

    def part1(self) -> Tuple[int, str]:
        line = self.path(3, 1)
        return (line.count('#'), line)

    def part2(self) -> int:
        pathConfig = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        paths = map(lambda pair: self.path(*pair), pathConfig)
        return reduce(lambda a, b: a * b,
                      map(lambda path: path.count('#'), paths))
