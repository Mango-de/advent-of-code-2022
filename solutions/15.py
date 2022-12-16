import re
from itertools import chain
from operator import sub
from typing import Iterable

with open('inputs/15') as f:
    coordinates = [tuple(map(int, re.findall(r'=(-?\d+)', line))) for line in f.read().splitlines()]


def get_blocked(closest_distance: int, distance: int) -> int:
    if abs(distance) > closest_distance:
        return 0

    blocked_in_row = -1

    for i in range(closest_distance, -1, -1):
        blocked_in_row += 2
        if i == abs(distance):
            return blocked_in_row


def is_possible(sensors: tuple[int, int, int], x: int, y: int):
    return all(abs(x - sx) + abs(y - sy) > distance for sx, sy, distance in sensors)


def get_line_between_points(x1: int, y1: int, x2: int, y2: int) -> Iterable[tuple[int, int]]:
    x_line = range(min(x1, x2), max(x1, x2) + 1)
    if x1 > x2:
        x_line = x_line[::-1]

    y_line = range(min(y1, y2), max(y1, y2) + 1)
    if y1 > y2:
        y_line = y_line[::-1]

    if x1 == x2:
        x_line = [x1] * len(y_line)
    if y1 == y2:
        y_line = [y1] * len(x_line)

    for x, y in zip(x_line, y_line):
        yield x, y


def part_1(coordinates: list[tuple[int, int, int, int]]):
    # coordinates of sensor and its distance to closest beacon
    sensors = [(sx, sy, sum(map(abs, map(sub, (sx, sy), (bx, by))))) for sx, sy, bx, by in coordinates]

    y = 2_000_000
    no_beacon = set()

    for sx, sy, distance in sensors:
        if (blocked := get_blocked(distance, y - sy)) > 0:
            no_beacon.add(sx)
            for i in range(blocked // 2 + 1):
                no_beacon.add(sx - i)
                no_beacon.add(sx + i)

    print(len(no_beacon - set(e[2] for e in coordinates if e[3] == y))) # if a beacon is in row y, don't consider its position to be impossible


def part_2(coordinates: list[tuple[int, int, int, int]]):
    sensors = [(sx, sy, sum(map(abs, map(sub, (sx, sy), (bx, by))))) for sx, sy, bx, by in coordinates]

    beacon_max = 4_000_000
    min_x = min(e[0] for e in coordinates)
    max_x = max(e[0] for e in coordinates)
    min_y = min(e[1] for e in coordinates)
    max_y = max(e[1] for e in coordinates)

    for sx, sy, distance in sensors:
        for x, y in chain(
            get_line_between_points(sx, sy - distance - 1, sx + distance + 1, sy),
            get_line_between_points(sx, sy + distance + 1, sx - distance - 1, sy),
            get_line_between_points(sx + distance + 1, sy, sx, sy + distance + 1),
            get_line_between_points(sx - distance - 1, sy, sx, sy - distance - 1)
        ):
            if max(0, min_x) <= x <= min(max_x, beacon_max) and max(0, min_y) <= y <= min(max_y, beacon_max) and is_possible(sensors, x, y):
                print(x * 4_000_000 + y)
                return


part_1(coordinates)
part_2(coordinates)
