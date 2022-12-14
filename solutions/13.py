with open('inputs/13') as f:
    pairs = [[eval(packet) for packet in p.splitlines()] for p in f.read().split('\n\n')]
    # packets = [eval(packet) for packet in f.read().replace('\n\n', '\n').splitlines()]


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


def part_1(pairs: list[list]):
    indices_sum = 0

    for i, pair in enumerate(pairs, start=1):
        if compare_values(*pair):
            indices_sum += i

    print(indices_sum)


# def part_2(packets: list):
    # packets = [[[2]], [[6]]] + packets


part_1(pairs)
# part_2(packets)
