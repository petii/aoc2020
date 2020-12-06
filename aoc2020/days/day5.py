from typing import List

def seatId(bsp: str) -> int:
    return 4

class Solution:
    input : List[str]
    def __init__(self, input: List[str]) -> None:
        self.input = input

    def part1(self) -> int:
        return max(map(seatId, self.input))
