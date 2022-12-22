import re

from utils.runtime import get_runtime


def get_input() -> tuple[list[list[str]], list[tuple[int, int, int]]]:
    with open('inputs/05') as f:
        l = f.read().split('\n\n')

    crate_count = len(l[0].splitlines()[-1].split('   '))
    crates = []

    for i in range(crate_count):
        for line in l[0].splitlines()[:-1]:
            while len(crates) < crate_count:
                crates.append([])
            content = line[1 + 4 * i]
            if content != ' ':
                crates[i].append(content)
        crates[i].reverse()

    instructions = []

    for instruction in l[1].splitlines():
        match = re.match(r'move (\d+) from (\d+) to (\d+)', instruction)
        instructions.append(tuple(map(int, match.groups())))

    return crates, instructions


@get_runtime
def part_1(crates: list[list[str]], instructions: list[tuple[int, int, int]]):
    for _quantity, _from, _to in instructions:
        crates[_to - 1].extend(crates[_from - 1][-_quantity:][::-1])
        for _ in range(_quantity):
            crates[_from - 1].pop()

    print(''.join(map(lambda x: x[-1], crates)))


@get_runtime
def part_2(crates: list[list[str]], instructions: list[tuple[int, int, int]]):
    for _quantity, _from, _to in instructions:
        crates[_to - 1].extend(crates[_from - 1][-_quantity:])
        for _ in range(_quantity):
            crates[_from - 1].pop()

    print(''.join(map(lambda x: x[-1], crates)))


part_1(*get_input())
part_2(*get_input())
