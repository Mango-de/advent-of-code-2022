from utils.runtime import get_runtime


def get_input() -> list[list[str]]:
    with open('inputs/02') as f:
        l = [*map(lambda x: x.split(' '), f.read().splitlines())]

    return l


def solve(l: list[list[str]], scores: dict[str, dict[str, int]]) -> int:
    score = 0

    for a, b in l:
        score += scores[a][b]

    return score


@get_runtime
def part_1(l: list[list[str]]):
    scores = {
        'A': {
            'X': 4,
            'Y': 8,
            'Z': 3
        },
        'B': {
            'X': 1,
            'Y': 5,
            'Z': 9
        },
        'C': {
            'X': 7,
            'Y': 2,
            'Z': 6
        }
    }

    print(solve(l, scores))


@get_runtime
def part_2(l: list[list[str]]):
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

    print(solve(l, scores))


part_1(get_input())
part_2(get_input())
