with open('inputs/20') as f:
    numbers = [*enumerate(int(x) for x in f.read().splitlines())]


def part_1(numbers: list[tuple[int, int]]):
    order = numbers[:]

    for index, n in order:
        i1 = list(map(lambda x: x[0], numbers)).index(index)

        for _ in range(abs(n)):
            ni = (i1 + (n // abs(n))) % len(numbers)
            numbers[i1], numbers[ni] = numbers[ni], numbers[i1]
            i1 = ni

    i2 = list(map(lambda x: x[1], numbers)).index(0)

    print(sum(numbers[(i2 + (x + 1) * 1000) % len(numbers)][1] for x in range(3)))


def part_2(numbers: list[tuple[int, int]]):
    key = 811589153
    numbers = [(x, y * key) for x, y in numbers]

    order = numbers[:]

    for _ in range(10):
        for index, _ in order:
            i1 = list(map(lambda x: x[0], numbers)).index(index)

            nn = numbers[i1][1] % (len(numbers) - 1)
            for _ in range(abs(nn)):
                ni = (i1 + (nn // abs(nn))) % len(numbers)
                numbers[i1], numbers[ni] = numbers[ni], numbers[i1]
                i1 = ni

    i2 = list(map(lambda x: x[1], numbers)).index(0)

    print(sum(numbers[(i2 + (x + 1) * 1000) % len(numbers)][1] for x in range(3)))


part_1(numbers[:])
part_2(numbers[:])
