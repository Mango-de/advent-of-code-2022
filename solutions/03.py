with open('inputs/03') as f:
    l = f.read().splitlines()


def get_priority(item: str) -> int:
    if item.isupper():
        return ord(item) - 38
    elif item.islower():
        return ord(item) - 96


def part_1(l: list[str]):
    priority_sum = 0

    for rucksack in l:
        comp1 = rucksack[:len(rucksack)//2]
        comp2 = rucksack[len(rucksack)//2:]
        item_type = set(comp1).intersection(comp2).pop()
        priority_sum += get_priority(item_type)

    print(priority_sum)


def part_2(l: list[str]):
    priority_sum = 0

    for i in range(0, len(l), 3):
        group_item = set(l[i]).intersection(l[i + 1], l[i + 2]).pop()
        priority_sum += get_priority(group_item)

    print(priority_sum)


part_1(l)
part_2(l)
