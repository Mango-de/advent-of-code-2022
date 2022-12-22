import re
from operator import add

with open('inputs/22') as f:
    l = f.read().split('\n\n')

grid = [[x for x in y] for y in l[0].splitlines()]

for i, line in enumerate(grid): # to ensure the grid is shaped as a rectangle
    if (line_len := len(line)) != (max_len := len(max(grid, key=len))):
        grid[i] = line + [' '] * (max_len - line_len)

movements = [*map(int, re.findall(r'\d+', l[1]))]
turnings = re.findall(r'[LR]', l[1]) + [None] # to ensure having the same amount of movements and "turnings" for zipping them together

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part_1():
    pos = (0, grid[0].index('.'))
    direction_index = 0

    for movement, turning in zip(movements, turnings, strict=True):
        direction = directions[direction_index]

        for _ in range(movement):
            y, x = map(add, pos, direction)

            if y == len(grid) or (direction_index == 1 and grid[y][x] == ' '):
                for ny in range(len(grid)):
                    if grid[ny][x] != ' ':
                        y = ny
                        break
            elif y == -1 or (direction_index == 3 and grid[y][x] == ' '):
                for ny in range(len(grid) - 1, -1, -1):
                    if grid[ny][x] != ' ':
                        y = ny
                        break
            elif x == len(grid[0]) or (direction_index == 0 and grid[y][x] == ' '):
                for nx in range(len(grid[0])):
                    if grid[y][nx] != ' ':
                        x = nx
                        break
            elif x == -1 or (direction_index == 2 and grid[y][x] == ' '):
                for nx in range(len(grid[0]) - 1, -1, -1):
                    if grid[y][nx] != ' ':
                        x = nx
                        break

            if grid[y][x] == '#':
                break

            pos = (y, x)

        direction_index = (direction_index + {'L': -1, 'R': 1, None: 0}[turning]) % len(directions)

    print(1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + direction_index)


# def part_2():
    # pass


part_1()
# part_2()
