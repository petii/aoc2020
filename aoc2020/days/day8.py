from typing import List, Callable, Dict
from pprint import pprint
from collections import namedtuple, deque


def part1(input: List[str]) -> int:
    try:
        execute([
            Instruction(name=x[0], value=int(x[1]))
            for x in map(lambda x: x.split(' '), input)
        ])
    except InfiniteLoopException as e:
        return e.args[0]['accumulator']


def part2(input: List[str]) -> int:
    bootcode = [
        Instruction(name=x[0], value=int(x[1]))
        for x in map(lambda x: x.split(' '), input)
    ]
    # pprint(bootcode)
    try:
        execute(bootcode)
    except InfiniteLoopException as e:
        changeable = [
            lineNo for lineNo in e.args[0]['history']
            if bootcode[lineNo].name in ['jmp', 'nop']
        ]
    changeable.reverse()
    while len(changeable) > 0:
        lineToTry = changeable[0]
        currentLine = bootcode[lineToTry]
        newInstruction = Instruction(
            name='jmp', value=currentLine.value
        ) if currentLine.name == 'nop' else Instruction(
            name='nop', value=currentLine.value)
        newBootCode = bootcode[:lineToTry] + [newInstruction
                                              ] + bootcode[lineToTry + 1:]
        try:
            return execute(newBootCode)
        except InfiniteLoopException as e:
            pass
        changeable = changeable[1:]
    raise InfiniteLoopException('Did not find the fix')


Instruction = namedtuple('Instruction', field_names=['name', 'value'])
State = namedtuple('State', field_names=['sp', 'ac'])


class InfiniteLoopException(Exception):
    pass


_instructionMap: Dict[str, Callable] = {
    'nop': lambda state, param: State(state.sp + 1, state.ac),
    'acc': lambda state, param: State(state.sp + 1, state.ac + param),
    'jmp': lambda state, param: State(state.sp + param, state.ac),
}


def execute(bootcode: List[Instruction]) -> int:
    s = State(sp=0, ac=0)
    history: List[int] = []
    while s.sp < len(bootcode):
        if s.sp in history:
            raise InfiniteLoopException({
                'stackpointer': s.sp,
                'accumulator': s.ac,
                'history': history
            })
        history.append(s.sp)
        current = bootcode[s.sp]
        s = _instructionMap[current.name](s, current.value)
    return s.ac