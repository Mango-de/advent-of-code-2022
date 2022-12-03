with open('inputs/03') as f:
    l = f.read().splitlines()


def part_1(l):
    priority_sum = 0

    for rucksack in l:
        comp1 = rucksack[:len(rucksack)//2]
        comp2 = rucksack[len(rucksack)//2:]
        item_type = set(comp1).intersection(comp2).pop()
        if item_type.isupper():
            priority_sum += ord(item_type) - 38
        elif item_type.islower():
            priority_sum += ord(item_type) - 96

    print(priority_sum)


def part_2(l):
    priority_sum = 0

    for i in range(0, len(l), 3):
        group_item = set(l[i]).intersection(l[i + 1], l[i + 2]).pop()
        if group_item.isupper():
            priority_sum += ord(group_item) - 38
        elif group_item.islower():
            priority_sum += ord(group_item) - 96

    print(priority_sum)

part_1(l)
part_2(l)
