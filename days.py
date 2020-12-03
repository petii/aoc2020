from typing import List, Dict, Callable

def day1(input:List[int]) -> str:
    print(f'day1')
    print(input)

def day2(input:str) -> str:
    print('day2')

_daySelector : Dict[int, Callable] = {
    1 : day1,
    2 : day2
}

def daySelector(day : int, fileContents : str):
    if day == 1:
        input = list(map(int,filter(lambda x : x != '' ,fileContents.split('\n'))))
        return day1(input)
