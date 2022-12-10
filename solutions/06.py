with open('inputs/06') as f:
    t = f.read()


def solve(text: str, quantity: int):
    for i in range(quantity - 1, len(text)):
        t = ''
        for j in range(quantity):
            if (char := text[i - j]) in t:
                break
            t += char
        if len(t) == quantity:
            return i + 1


def part_1(text: str):
    print(solve(text, 4))


def part_2(text: str):
    print(solve(text, 14))

part_1(t)
part_2(t)
