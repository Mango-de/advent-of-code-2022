from utils.runtime import get_runtime


def get_input() -> list[str]:
    with open('inputs/10') as f:
        l = f.read().splitlines()

    return l


@get_runtime
def part_1(l: list[str]):
    x = 1
    cycle = 0
    signal_strength = 0

    for instruction in l:
        if instruction == 'noop':
            cycle += 1
            if cycle % 40 == 20:
                signal_strength += cycle * x
        else:
            cycle += 1
            v = int(instruction.split()[1])
            if cycle % 40 == 20:
                signal_strength += cycle * x
            cycle += 1
            if cycle % 40 == 20:
                signal_strength += cycle * x
            x += v

    print(signal_strength)


@get_runtime
def part_2(l: list[str]):
    x = 1
    cycle = 0
    sprites = ['.'] * 240

    for instruction in l:
        if instruction == 'noop':
            if abs(cycle % 40 - x) <= 1:
                sprites[cycle] = '#'
            cycle += 1
        else:
            v = int(instruction.split()[1])
            if abs(cycle % 40 - x) <= 1:
                sprites[cycle] = '#'
            cycle += 1
            if abs(cycle % 40 - x) <= 1:
                sprites[cycle] = '#'
            cycle += 1
            x += v

    for i in range(0, len(sprites), 40):
        sprite = sprites[i:i + 40]
        print(''.join(sprite))


part_1(get_input())
part_2(get_input())
