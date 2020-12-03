from typing import List, Dict, Callable, Tuple


class Solution:
    input: List[str]
    width: int

    def __init__(self, input: List[str]):
        self.input = input
        self.width = len(input[0])

    def part1(self) -> Tuple[int, str]:
        line = "".join([
            self.input[i][(i * 3) % self.width]
            for i in range(0, len(self.input))
        ])
        return (line.count('#'), line)
