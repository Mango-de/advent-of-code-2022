from operator import add

from utils.runtime import get_runtime

DIRECTIONS = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}


def get_input() -> list[tuple[str, int]]:
    with open('inputs/09') as f:
        l = [*map(lambda x: (x[0], int(x[1])), map(lambda x: x.split(), f.read().splitlines()))]

    return l


def touching(h: tuple[int, int], t: tuple[int, int]) -> bool:
    return abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1


def solve(l: list[tuple[str, int]], n: int) -> int:
    knots = [(0, 0)] * n

    tail_visited = set()
    tail_visited.add(knots[-1])

    for direction, quantity in l:
        for _ in range(quantity):
            knots[0] = tuple(map(add, knots[0], DIRECTIONS[direction]))
            for i in range(n - 1):
                h, t = knots[i:i + 2]
                if not touching(h, t):
                    x, y = t
                    while not touching((x, y), h):
                        if h[0] > x:
                            x += 1
                        elif h[0] < x:
                            x -= 1
                        if h[1] > y:
                            y += 1
                        elif h[1] < y:
                            y -= 1
                        knots[i + 1] = (x, y)
                        if i == n - 2:
                            tail_visited.add((x, y))

    return len(tail_visited)


@get_runtime
def part_1(l: list[tuple[str, int]]):
    print(solve(l, 2))


@get_runtime
def part_2(l: list[tuple[str, int]]):
    print(solve(l, 10))


part_1(get_input())
part_2(get_input())
