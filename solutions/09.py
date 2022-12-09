from itertools import pairwise
from operator import add

with open('inputs/09') as f:
    l = [*map(lambda x: (x[0], int(x[1])), map(lambda x: x.split(), f.read().splitlines()))]

directions = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0)
}


def touching(h, t):
    return abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1


def diagonally(h, t):
    return h[0] != t[0] and h[1] != t[1]


def part_1(l):
    h = (0, 0)
    t = (0, 0)

    tail_visited = set()
    tail_visited.add(t)

    for direction, quantity in l:
        instruction = tuple(quantity * x for x in directions[direction])
        h = tuple(map(add, h, instruction))
        if not touching(h, t):
            x, y = t
            if diagonally(h, t):
                if h[0] > x and h[1] < y:
                    x += 1; y -= 1
                elif h[0] > x and h[1] > y:
                    x += 1; y += 1
                elif h[0] < x and h[1] < y:
                    x -= 1; y -= 1
                elif h[0] < x and h[1] > y:
                    x -= 1; y += 1
                t = (x, y)
                tail_visited.add(t)
            while not touching((x, y), h):
                if h[0] > x:
                    x += 1
                elif h[1] > y:
                    y += 1
                elif h[0] < x:
                    x -= 1
                elif h[1] < y:
                    y -= 1
                t = (x, y)
                tail_visited.add(t)

    print(len(tail_visited))


# def part_2(l):
#     knots = [(0, 0)] * 10

#     tail_visited = set()
#     tail_visited.add(knots[-1])

#     for direction, quantity in l:
#         instruction = tuple(quantity * x for x in directions[direction])
#         knots[0] = tuple(map(add, knots[0], instruction))
#         for i in range(9):
#             h, t = knots[i:i + 2]
#             if not touching(h, t):
#                 x, y = t
#                 if diagonally(h, t):
#                     if h[0] > x and h[1] < y:
#                         x += 1; y -= 1
#                     elif h[0] > x and h[1] > y:
#                         x += 1; y += 1
#                     elif h[0] < x and h[1] < y:
#                         x -= 1; y -= 1
#                     elif h[0] < x and h[1] > y:
#                         x -= 1; y += 1
#                     knots[i + 1] = (x, y)
#                     if i == 8:
#                         tail_visited.add((x, y))
#                 while not touching((x, y), h):
#                     if h[0] > x:
#                         x += 1
#                     elif h[1] > y:
#                         y += 1
#                     elif h[0] < x:
#                         x -= 1
#                     elif h[1] < y:
#                         y -= 1
#                     knots[i + 1] = (x, y)
#                     if i == 8:
#                         tail_visited.add((x, y))

#     print(len(tail_visited))

# l = [*map(lambda x: (x[0], int(x[1])), map(lambda x: x.split(), """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20""".splitlines()))]

part_1(l)
# part_2(l)
