with open('inputs/01') as f:
    l = [*map(sum, (map(int, x.splitlines()) for x in f.read().split('\n\n')))]


def part_1(l):
    print(max(l))


def part_2(l):
    top = [0] * 3

    for s in l:
        for i in range(3):
            if s > top[i]:
                while i > 0:
                    top[i] = top[i - 1]
                    i -= 1
                top[i] = s
                break

    print(sum(top))

part_1()
part_2()
