from typing import List

import pprint


def summarizeGroupAny(group: List[str]) -> int:
    return len(set(''.join(group)))


def summarizeGroupEvery(group: List[str]) -> int:
    questions = {x: False for x in set(''.join(group))}
    for q in questions.keys():
        questions[q] = all([x.find(q) >= 0 for x in group])
    return len([y for y in questions.values() if y])


class Solution:
    input: List[List[str]]

    def __init__(self, input: List[str]) -> None:
        self.input = [[member for member in group.split('\n') if member != '']
                      for group in input]

    def part1(self) -> int:
        return sum([summarizeGroupAny(g) for g in self.input])

    def part2(self) -> int:
        return sum([summarizeGroupEvery(g) for g in self.input])