with open('inputs/07') as f:
    l = f.read().splitlines()


def get_sizes(l: list[str]) -> dict[tuple, int]:
    sizes = {}
    current_path = ()
    used = set()

    for line in l:
        if line.startswith('$'):
            if (groups := line.split())[1] == 'cd':
                destination = groups[2]
                if destination == '/':
                    continue
                elif destination == '..':
                    current_path = current_path[:-1]
                else:
                    current_path = (*current_path, destination)
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


def part_1(l: list[str]):
    sizes = get_sizes(l).values()

    print(sum(filter(lambda x: x <= 100_000, sizes)))


def part_2(l: list[str]):
    sizes = get_sizes(l)

    print(min(filter(lambda x: x >= 30_000_000 - (70_000_000 - sizes[()]), sizes.values())))


part_1(l)
part_2(l)
