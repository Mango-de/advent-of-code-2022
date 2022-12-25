from utils.runtime import get_runtime


def get_input() -> list[str]:
    with open('inputs/25') as f:
        l = f.read().splitlines()

    return l


def snafu_to_decimal(snafu: str) -> int:
    decimal = 0

    for exponent, digit in enumerate(snafu[::-1]):
        factor = 5 ** exponent

        if digit.isdigit():
            decimal += int(digit) * factor
        else:
            decimal -= {'-': 1, '=': 2}[digit] * factor

    return decimal


def decimal_to_snafu(decimal: int) -> str:
    if decimal > 0:
        new_decimal, index = divmod(decimal + 2, 5)
        return decimal_to_snafu(new_decimal) + '=-012'[index]

    return ''


@get_runtime
def part_1(snafu_numbers: list[str]):
    print(decimal_to_snafu(sum(map(snafu_to_decimal, snafu_numbers))))


part_1(get_input())
