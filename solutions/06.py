from utils.runtime import get_runtime


def get_input() -> str:
    with open('inputs/06') as f:
        l = f.read()

    return l


def solve(text: str, quantity: int) -> int:
    for i in range(quantity - 1, len(text)):
        t = ''
        for j in range(quantity):
            if (char := text[i - j]) in t:
                break
            t += char
        if len(t) == quantity:
            return i + 1


@get_runtime
def part_1(text: str):
    print(solve(text, 4))


@get_runtime
def part_2(text: str):
    print(solve(text, 14))


part_1(get_input())
part_2(get_input())
