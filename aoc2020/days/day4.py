import re
from functools import reduce
from pprint import pprint
from typing import List

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
exceptions = ['cid']


class Solution:
    input: List[List[str]]

    def __init__(self, input: List[str]) -> None:
        self.input = [re.split('[\n ]', x) for x in input]

    def checkPassport(self, data: List[str]) -> bool:
        required = [
            x for x in data if not any(x.find(y) >= 0 for y in exceptions)
        ]
        return all(
            any(req.find(field) >= 0 for req in required)
            for field in set(fields) - set(exceptions))

    def part1(self) -> int:
        return len(list(filter(self.checkPassport, self.input)))
