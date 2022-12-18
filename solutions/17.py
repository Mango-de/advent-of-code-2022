from collections import defaultdict

with open('inputs/17') as f:
    instructions = f.read()

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
        [1] * 3,
        [0, 0, 1],
        [0, 0, 1],
    ], # yes, this one needs to be reversed
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


class ChamberTower:
    def __init__(self, instructions: str):
        self.instructions = instructions

        self.max_y = 0
        self.instruction_index = 0
        self.blocked = set()

        self.rock_index = 0
        self.x = 2
        self.y = 3

        self.settled = 0

    def horizontal_movement_possible(self, instruction: str) -> bool | tuple[bool, int]:
        nx = self.x + {'<': -1, '>': 1}[instruction]

        if nx < 0 or nx > 6:
            return False

        for y, line in enumerate(rocks[self.rock_index]):
            for x, value in enumerate(line):
                if value:
                    if (nx + x, self.y + y) in self.blocked or nx + x > 6:
                        return False

        return True, nx

    def vertical_movement_possible(self) -> bool:
        ny = self.y - 1

        if ny < 0:
            return False

        for y, line in enumerate(rocks[self.rock_index]):
            for x, value in enumerate(line):
                if value:
                    if (self.x + x, ny + y) in self.blocked:
                        return False

        return True

    def move(self) -> bool:
        instruction = self.instructions[self.instruction_index]
        self.instruction_index = (self.instruction_index + 1) % len(instructions)

        if (x := self.horizontal_movement_possible(instruction)):
            self.x = x[1]

        if self.vertical_movement_possible():
            self.y -= 1
            return False

        return True

    def drop_rock(self):
        while True:
            if self.move():
                break

        self.add_rock()

    def get_max_y(self) -> int:
        return max(x[1] for x in self.blocked)

    def add_rock(self):
        for y, l in enumerate(rocks[self.rock_index]):
            for x, c in enumerate(l):
                if c:
                    self.blocked.add((self.x + x, self.y + y))

        self.max_y = self.get_max_y()
        self.x = 2
        self.y = self.max_y + 4

        self.rock_index = (self.rock_index + 1) % len(rocks)
        self.settled += 1

    def find_pattern(self) -> tuple[list[int], dict[int, int]]:
        states = defaultdict(list)
        heights = {}

        while True:
            self.drop_rock()
            max_y = self.get_max_y()

            heights[self.settled] = max_y + 1

            if all((x, max_y) in self.blocked for x in range(7)):
                s = (self.instruction_index, self.rock_index)
                states[s].append(self.settled)
                if len(states[s]) == 2:
                    return states[s], heights

    def print_chamber(self):
        for y in range(max([y for _, y in self.blocked]), -1, -1):
            print('|', end='')
            for x in range(7):
                if (x, y) in self.blocked:
                    print('#', end='')
                else:
                    print('.', end='')
            print('|' + (' ' + str(y + 1) if (y + 1) % 5 == 0 else ''))
        print('+-------+')


def part_1(instructions: str):
    tower = ChamberTower(instructions)

    for _ in range(2022):
        tower.drop_rock()

    print(tower.get_max_y() + 1)


def part_2(instructions: str):
    tower = ChamberTower(instructions)
    pattern, heights = tower.find_pattern()

    cycles = (1_000_000_000_000 - min(pattern)) // (max(pattern) - min(pattern))
    cycle_height = heights[max(pattern)] - heights[min(pattern)]

    rocks = (1_000_000_000_000 - max(pattern)) % (max(pattern) - min(pattern))
    height = heights[min(pattern) + rocks] - heights[min(pattern)]

    initial_height = heights[min(pattern)]

    print(initial_height + height + cycles*cycle_height)


part_1(instructions)
part_2(instructions)
