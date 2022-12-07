import re

with open('inputs/07') as f:
    l = f.read().splitlines()


def get_sizes(l):
    sizes = {}
    current_path = ()
    used = set()

    for line in l:
        if line.startswith('$'):
            groups = re.match(r'\$ ([a-z]+) ?(\S+)?', line).groups()
            if groups[0] == 'cd':
                if groups[1] == '/':
                    continue
                elif groups[1] == '..':
                    current_path = current_path[:-1]
                else:
                    current_path = (*current_path, groups[1])
        else:
            size, name = line.split()
            if size.isdigit():
                if (new_path := (current_path, name)) in used:
                    continue
                used.add(new_path)

                path = current_path
                while True:
                    sizes[path] = sizes.get(path, 0) + int(size)
                    if len(path) == 0:
                        break
                    path = path[:-1]

    return sizes


def part_1(l):
    sizes = get_sizes(l)

    print(sum(filter(lambda x: x <= 100_000, sizes.values())))


def part_2(l):
    sizes = get_sizes(l)

    print(min(filter(lambda x: x >= 30_000_000 - (70_000_000 - sizes[()]), sizes.values())))

part_1(l)
part_2(l)
