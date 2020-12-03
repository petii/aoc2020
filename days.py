from pprint import pprint
from typing import List, Dict, Callable, Tuple

class Day1:
    input: List[int]
    def __init__(self, input : List[int]):
        self.input = input

    def part1(self) -> Tuple[int,int,int]:
        for index in range(0, len(self.input)-1):
            current = self.input[index]
            rest: List[int] = self.input[index+1:]
            results = list(filter(lambda x : x+current == 2020, rest))
            if len(results) > 0:
                return (current, results[0], current * results[0])

    def part2(self) -> int:
        pass

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
        print('  Part One: ',f'{pt1[0]} x {pt1[1]} = {pt1[2]}')
        print('  Part Two: ',day.part2())
    if day == 2:
        pass
