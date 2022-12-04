with open('inputs/04') as f:
    l = [(tuple(map(int, e1.split('-'))), tuple(map(int, e2.split('-')))) for e1, e2 in map(lambda x: x.split(','), f.read().splitlines())]


def part_1(l):
    overlapping = 0

    for r1, r2 in l:
        if r1[0] <= r2[0] and r1[1] >= r2[1]:
            overlapping += 1
        elif r2[0] <= r1[0] and r2[1] >= r1[1]:
            overlapping += 1

    print(overlapping)


def part_2(l):
    overlapping = 0

    for r1, r2 in l:
        if r2[0] <= r1[0] <= r2[1] or r2[0] <= r1[1] <= r2[1] or r1[0] <= r2[0] <= r1[1] or r1[0] <= r2[1] <= r1[1]:
            overlapping += 1

    print(overlapping)

part_1(l)
part_2(l)
