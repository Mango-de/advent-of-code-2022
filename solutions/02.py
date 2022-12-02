with open('inputs/02') as f:
    l = [*map(lambda x: x.split(' '), f.read().splitlines())]


def part_1(l):
    values = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    scores = {
        'A': {
            'X': 3,
            'Y': 6,
            'Z': 0
        },
        'B': {
            'X': 0,
            'Y': 3,
            'Z': 6
        },
        'C': {
            'X': 6,
            'Y': 0,
            'Z': 3
        }
    }

    score = 0

    for a, b in l:
        score += values[b]
        score += scores[a][b]

    print(score)


def part_2(l):
    scores = {
        'A': {
            'X': 3,
            'Y': 4,
            'Z': 8
        },
        'B': {
            'X': 1,
            'Y': 5,
            'Z': 9
        },
        'C': {
            'X': 2,
            'Y': 6,
            'Z': 7
        }
    }

    score = 0

    for a, b in l:
        score += scores[a][b]

    print(score)

part_1(l)
part_2(l)
