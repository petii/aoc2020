from pprint import pprint
from typing import List, Dict, Callable, Tuple

class Day1:
    input: List[int]
    def __init__(self, input : List[int]):
        self.input = input

    def _part1(self, input:List[int], sum: int) -> Tuple[int,int,int]:
        for index in range(0, len(input)-1):
            current = input[index]
            rest: List[int] = input[index+1:]
            result = next((x for x in rest if x == sum-current), None)
            if result != None:
                return (current, result, current * result)

    def part1(self) -> Tuple[int,int,int]:
        return self._part1(self.input, 2020)
        for index in range(0, len(self.input)-1):
            current = self.input[index]
            rest: List[int] = self.input[index+1:]
            result = next((x for x in rest if x == 2020-current), None)
            if result != None:
                return (current, result, current * result)

    def part2(self) -> int:
        for index in range(0, len(self.input)-2):
            current = self.input[index]
            rest: List[int] = self.input[index+1:]
            result = self._part1(rest, 2020-current)
            if result != None:
                return (current, result[0],result[1],result[2]*current)


def day2(input:str) -> str:
    print('day2')

_daySelector : Dict[int, Callable] = {
    2 : day2
}

def daySelector(day : int, fileContents : str):
    if day == 1:
        input = list(map(int,filter(lambda x : x != '' ,fileContents.split('\n'))))
        day = Day1(input)
        print('Solving day1 puzzle with the following input:', *input[:10], '...', input[-1])
        pt1 = day.part1()
        pt2 = day.part2()
        print('  Part One: ',f'{pt1[0]} x {pt1[1]} = {pt1[2]}')
        print('  Part Two: ',f'{pt2[0]} x {pt2[1]} x {pt2[2]} = {pt2[3]}')
    if day == 2:
        pass
