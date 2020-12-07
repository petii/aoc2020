from typing import List
from collections import deque


def seatId(bsp: str) -> int:
    rowMap = {'F': '0', 'B': '1'}
    colMap = {'L': '0', 'R': '1'}
    rowSpec, colSpec = bsp[:7], bsp[7:]
    assert (len(colSpec) == 3)
    row = int(''.join(map(lambda c: rowMap[c], rowSpec)), 2)
    col = int(''.join(map(lambda c: colMap[c], colSpec)), 2)
    return row * 8 + col


class Solution:
    input: List[str]

    def __init__(self, input: List[str]) -> None:
        self.input = input

    def part1(self) -> int:
        return max(map(seatId, self.input))

    def part2(self) -> int:
        ids = set(map(seatId, self.input))
        deq = deque(ids)
        deq.rotate(-1)
        neighbourPairs = zip(ids, deq)
        neighbours = list(filter(lambda x: x[1] - x[0] > 1, neighbourPairs))[0]
        return (neighbours[0] + neighbours[1]) // 2
