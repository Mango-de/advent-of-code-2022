from itertools import pairwise
from operator import add

from utils.runtime import get_runtime

DIRECTIONS = [(0, 1), (-1, 1), (1, 1)]


def get_input() -> list[list[tuple[int, int]]]:
    with open('inputs/14') as f:
        l = [[*map(lambda y: tuple(map(int, y.split(','))), x.split(' -> '))] for x in f.read().splitlines()]

    return l


def get_rocks(paths: list[list[tuple[int, int]]]) -> set:
    rocks = set()

    for path in paths:
        for (x1, y1), (x2, y2) in pairwise(path):
            rocks.add((x1, y1))
            while x1 < x2:
                x1 += 1
                rocks.add((x1, y1))
            while x1 > x2:
                x1 -= 1
                rocks.add((x1, y1))
            while y1 < y2:
                y1 += 1
                rocks.add((x1, y1))
            while y1 > y2:
                y1 -= 1
                rocks.add((x1, y1))

    return rocks


@get_runtime
def part_1(paths: list[list[tuple[int, int]]]):
    blocked = get_rocks(paths)

    success = True
    sand = 0

    while success:
        rest = False
        x, y = 500, 0

        while not rest:
            for direction in DIRECTIONS:
                new_pos = tuple(map(add, (x, y), direction))
                if new_pos[1] > max([r[1] for r in blocked]):
                    rest = True
                    success = False
                    break
                if new_pos not in blocked:
                    x, y = new_pos
                    break
            else:
                blocked.add((x, y))
                sand += 1
                rest = True

    print(sand)


@get_runtime
def part_2(paths: list[list[tuple[int, int]]]):
    blocked = get_rocks(paths)
    ground = 2 + max([r[1] for r in blocked])

    success = True
    sand = 0

    while success:
        rest = False
        x, y = 500, 0

        while not rest:
            for direction in DIRECTIONS:
                new_pos = tuple(map(add, (x, y), direction))
                if new_pos not in blocked and new_pos[1] < ground:
                    x, y = new_pos
                    break
            else:
                blocked.add((x, y))
                sand += 1
                rest = True
                if (x, y) == (500, 0):
                    success = False

    print(sand)


part_1(get_input())
part_2(get_input())
