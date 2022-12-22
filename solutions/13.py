from utils.runtime import get_runtime


def get_input() -> list[list]:
    with open('inputs/13') as f:
        l = [[eval(packet) for packet in p.splitlines()] for p in f.read().split('\n\n')]

    return l


def compare_values(v1: int | list, v2: int | list) -> bool | None:
    if isinstance(v1, int) and isinstance(v2, int):
        if v1 < v2:
            return True
        elif v1 > v2:
            return False
        return

    if isinstance(v1, int):
        v1 = [v1]
    if isinstance(v2, int):
        v2 = [v2]

    for e1, e2 in zip(v1, v2):
        result = compare_values(e1, e2)
        if result is not None:
            return result

    if len(v1) < len(v2):
        return True
    elif len(v1) > len(v2):
        return False


@get_runtime
def part_1(pairs: list[list]):
    indices_sum = 0

    for i, pair in enumerate(pairs, start=1):
        if compare_values(*pair):
            indices_sum += i

    print(indices_sum)


# @get_runtime
# def part_2(pairs: list[list]):
    # pass


part_1(get_input())
# part_2(get_input())
