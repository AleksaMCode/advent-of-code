import itertools


def split_rucksack_item(item: str):
    return item[:len(item) // 2], item[len(item) // 2:]


def find_common_elements(first_half: str, second_half: str):
    return set(first_half).intersection(second_half)


def find_common_badge(backpack1: str, backpack2: str, backpack3: str):
    return (set(backpack1) & set(backpack2) & set(backpack3)).pop()


def get_priority(element: str):
    return ord(element) - (96 if element.islower() else 38)


def function1(file_name):
    total_priority = 0
    with open(file_name) as file:
        for line in file:
            first_half, second_half = split_rucksack_item(line.strip())
            common = find_common_elements(first_half, second_half)
            _ = [total_priority := total_priority + get_priority(el) for el in common]

    return total_priority


def function2(file_name):
    total_priority = 0
    with open(file_name) as file:
        for line1, line2, line3 in itertools.zip_longest(*[file] * 3):
            badge = find_common_badge(line1.strip(), line2.strip(), line3.strip())
            total_priority += get_priority(badge)

    return total_priority
