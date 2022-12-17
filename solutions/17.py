with open('inputs/17') as f:
    instructions = f.read()
    # instructions = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

rocks = (
    [
        [1] * 4
    ],
    [
        [0, 1, 0],
        [1] * 3,
        [0, 1, 0]
    ],
    [
        [0, 0, 1],
        [0, 0, 1],
        [1] * 3
    ],
    [
        [1],
        [1],
        [1],
        [1]
    ],
    [
        [1] * 2,
        [1] * 2
    ]
)


def print_chamber(blocked: set[tuple[int, int]]):
    for i in range(max([y for _, y in blocked]), 0, -1):
        print('|', end='')
        for j in range(7):
            if (j + 1, i) in blocked:
                print('#', end='')
            else:
                print('.', end='')
        print('|' + (' ' + str(i) if i % 5 == 0 else ''))
    print('+-------+')


def part_1(instructions: str):
    max_y = 0
    executed_instructions = 0
    blocked = set()

    for rock_count in range(2022):
        rock = rocks[rock_count % len(rocks)]
        x = 3
        y = max_y + 4

        while True:
            positions = {}
            instruction = instructions[executed_instructions % len(instructions)]
            executed_instructions += 1

            if (instruction == '<'
                and x > 1
                and all((x - 1, y + z) not in blocked for z in range(len(rock))) # if rock[::-1][z][0])
            ):
                x -= 1
            elif (instruction == '>'
                and x + len(rock[0]) < 8
                and all((x + len(rock[0]), y + z) not in blocked for z in range(len(rock))) # if rock[::-1][z][-1])
            ):
                x += 1

            yn = y
            for row in rock[::-1]:
                xn = x
                for value in row:
                    if value:
                        positions[(xn, yn)] = value
                    xn += 1
                yn += 1

            for _x, _y in positions:
                if (_x, _y - 1) in blocked or _y == 1:
                    break
            else:
                y -= 1
                continue
            for _x, _y in positions:
                blocked.add((_x, _y))
                max_y = max(max_y, _y)
            break

    # print_chamber(blocked)
    print(max_y)


def part_2(instructions: str):
    pass


part_1(instructions)
part_2(instructions)
