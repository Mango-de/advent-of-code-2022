from utils.runtime import get_runtime


def get_input() -> list[int]:
    with open('inputs/01') as f:
        l = [*map(sum, (map(int, x.splitlines()) for x in f.read().split('\n\n')))]

    return l


@get_runtime
def part_1(l: list[int]):
    print(max(l))


@get_runtime
def part_2(l: list[int]):
    top = [0] * 3

    for s in l:
        for i in range(3):
            if s > top[i]:
                while i > 0:
                    top[i] = top[i - 1]
                    i -= 1
                top[i] = s
                break

    print(sum(top))


part_1(get_input())
part_2(get_input())
