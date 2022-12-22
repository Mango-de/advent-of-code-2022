from utils.runtime import get_runtime


def get_input() -> list[tuple[int, int]]:
    with open('inputs/04') as f:
        l = [(tuple(map(int, e1.split('-'))), tuple(map(int, e2.split('-')))) for e1, e2 in map(lambda x: x.split(','), f.read().splitlines())]

    return l


@get_runtime
def part_1(l: list[tuple[int, int]]):
    overlapping = 0

    for r1, r2 in l:
        if (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r2[0] <= r1[0] and r2[1] >= r1[1]):
            overlapping += 1

    print(overlapping)


@get_runtime
def part_2(l: list[tuple[int, int]]):
    overlapping = 0

    for r1, r2 in l:
        if (r2[0] <= r1[0] <= r2[1]
            or r2[0] <= r1[1] <= r2[1]
            or r1[0] <= r2[0] <= r1[1]
            or r1[0] <= r2[1] <= r1[1]):
            overlapping += 1

    print(overlapping)


part_1(get_input())
part_2(get_input())
