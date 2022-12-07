with open('inputs/06') as f:
    t = f.read()


def part_1(text: str):
    quantity = 4
    for i in range(quantity - 1, len(text)):
        t = ''
        for j in range(quantity):
            if (char := text[i - j]) in t:
                break
            t += char
        if len(t) == quantity:
            print(i + 1)
            break


def part_2(text: str):
    quantity = 14
    for i in range(quantity - 1, len(text)):
        t = ''
        for j in range(quantity):
            if (char := text[i - j]) in t:
                break
            t += char
        if len(t) == quantity:
            print(i + 1)
            break

part_1(t)
part_2(t)
