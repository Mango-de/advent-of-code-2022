import re
from functools import lru_cache
from operator import add, sub, mul, floordiv

with open('inputs/21') as f:
    data = dict(map(lambda x: re.match(r'([a-z]+): (.+)', x).groups(), f.read().splitlines()))

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': floordiv # = //
}


@lru_cache(maxsize=None)
def calculate(key: str):
    if (value := data[key]).isdigit():
        return int(value)

    k1, op, k2 = value.split()
    return operations[op](calculate(k1), calculate(k2))


def part_1():
    print(calculate('root'))


# def part_2():
#     pass


part_1()
# part_2()
