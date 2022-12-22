from utils.runtime import get_runtime


def get_input() -> list[tuple[int, int, int]]:
    with open('inputs/18') as f:
        l = [*map(tuple, map(lambda c: (int(x) for x in c.split(',')), f.read().splitlines()))]

    return l


@get_runtime
def part_1(cubes: list[tuple[int, int, int]]):
    not_connected_sides = 0

    for i, (x1, y1, z1) in enumerate(cubes):
        sides = 6

        for x2, y2, z2 in cubes[:i]:
            if abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) == 1:
                sides -= 2

        not_connected_sides += sides

    print(not_connected_sides)


# def part_2(cubes: list[tuple[int, int, int]]):
#     pass


part_1(get_input())
# part_2(get_input())
