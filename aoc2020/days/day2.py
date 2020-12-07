from typing import List, Dict, Callable, Tuple


class Solution:
    input: List[str]

    def __init__(self, input: List[str]):
        self.input = input

    def part1(self) -> int:
        return len(list(filter(self.match, self.input)))

    def part2(self) -> int:
        return len(list(filter(self.match2, self.input)))

    def match(self, line: str) -> bool:
        policy = self.policy(line)
        password = self.password(line)
        count = password.count(policy['char'])
        if count >= policy['min'] and count <= policy['max']:
            return True
        return False

    def match2(self, line: str) -> bool:
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
