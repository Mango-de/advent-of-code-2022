from copy import deepcopy
from functools import reduce
from operator import floordiv, mod, mul
from typing import Callable

with open('inputs/11') as f:
    l = f.read().split('\n\n')


def get_monkeys(l: list[str]) -> dict[int, dict[str, list[int] | str]]:
    monkeys = {}

    for i, monkey in enumerate(l):
        monkey = monkey.splitlines()
        m = {}
        m['items'] = list(map(int, monkey[1].strip().split(maxsplit=2)[2].split(', ')))
        m['operation'] = monkey[2].strip().split(maxsplit=3)[3]
        m['test'] = int(monkey[3].strip().split()[-1])
        m['true'] = int(monkey[4].strip().split()[-1])
        m['false'] = int(monkey[5].strip().split()[-1])
        m['inspected_items'] = 0
        monkeys[i] = m

    return monkeys


def solve(monkeys: dict[int, dict[str, list[int] | str]], n: int, operator: Callable[[int, int], int], k: int) -> int:
    for _ in range(n):
        i = 0
        while i != len(monkeys):
            monkey = monkeys[i]
            items = deepcopy(monkey['items'])
            for item in items:
                worry_level = eval(monkey['operation'].replace('old', str(item)))
                worry_level = operator(worry_level, k)
                monkey['items'].remove(item)
                monkey['inspected_items'] += 1
                if worry_level % monkey['test'] == 0:
                    new_monkey = monkeys[monkey['true']]
                else:
                    new_monkey = monkeys[monkey['false']]
                new_monkey['items'].append(worry_level)
            i += 1

    inspected = sorted(list(map(lambda x: x['inspected_items'], monkeys.values())), reverse=True)
    return mul(*inspected[:2])


def part_1(l: list[str]):
    monkeys = get_monkeys(l)

    print(solve(monkeys, 20, floordiv, 3))


def part_2(l: list[str]):
    monkeys = get_monkeys(l)

    print(solve(monkeys, 10_000, mod, reduce(mul, map(lambda x: x['test'], monkeys.values()))))


part_1(l)
part_2(l)
