from functools import reduce
from operator import mul

with open('inputs/08') as f:
    grid = [[int(x) for x in y] for y in f.read().splitlines()]


def part_1(grid: list[list[int]]):
    visible = 2 * len(grid) + 2 * (len(grid[0]) - 2)

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            v = [True] * 4

            yn = y
            while yn > 0: # up
                yn -= 1
                if grid[yn][x] >= grid[y][x]:
                    v[0] = False
                    break
            yn = y
            while yn < len(grid) - 1: # down
                yn += 1
                if grid[yn][x] >= grid[y][x]:
                    v[1] = False
                    break
            xn = x
            while xn > 0: # left
                xn -= 1
                if grid[y][xn] >= grid[y][x]:
                    v[2] = False
                    break
            xn = x
            while xn < len(grid[y]) - 1: # right
                xn += 1
                if grid[y][xn] >= grid[y][x]:
                    v[3] = False
                    break
            visible += int(any(v))

    print(visible)


def part_2(grid: list[list[int]]):
    max_score = 0

    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            scores = [0] * 4

            yn = y
            while yn > 0: # up
                yn -= 1
                scores[0] += 1
                if grid[yn][x] >= grid[y][x]:
                    break
            yn = y
            while yn < len(grid) - 1: # down
                yn += 1
                scores[1] += 1
                if grid[yn][x] >= grid[y][x]:
                    break
            xn = x
            while xn > 0: # left
                xn -= 1
                scores[2] += 1
                if grid[y][xn] >= grid[y][x]:
                    break
            xn = x
            while xn < len(grid[y]) - 1: # right
                xn += 1
                scores[3] += 1
                if grid[y][xn] >= grid[y][x]:
                    break

            if (score := reduce(mul, scores, 1)) > max_score:
                max_score = score

    print(max_score)

part_1(grid)
part_2(grid)
