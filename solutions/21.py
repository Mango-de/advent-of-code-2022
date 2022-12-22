import re
from functools import cache
from operator import add, floordiv, mul, sub

from sympy import parse_expr, solve

from utils.runtime import get_runtime

OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv # = //
}

with open('inputs/21') as f:
    data = dict(map(lambda x: re.match(r'([a-z]+): (.+)', x).groups(), f.read().splitlines()))


@cache
def calculate(key: str) -> int:
    if (value := data[key]).isdigit():
        return int(value)

    k1, op, k2 = value.split()
    return OPERATIONS[op](calculate(k1), calculate(k2))


@cache
def make_equation(key: str) -> str:
    if (value := data[key]).isdigit():
        return 'x' if key == 'humn' else value

    k1, op, k2 = value.split()
    return f'({make_equation(k1)}) {op} ({make_equation(k2)})'


@get_runtime
def part_1():
    print(calculate('root'))


@get_runtime
def part_2():
    left, _, right = data['root'].split()
    print(solve(sub(*map(parse_expr, map(make_equation, (left, right)))), 'x')[0])


part_1()
part_2()
