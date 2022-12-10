import re

stacks = []


def build_stack(file_name, size):
    stacks.clear()
    for i in range(size):
        stacks.append([])

    for line in reversed(list(open(file_name))):
        crates = line.strip().split(' ')
        for i in range(len(crates)):
            if crates[i]:
                stacks[i].append(crates[i])


def move_crates_9000(file_name):
    with open(file_name) as file:
        for line in file:
            values = [int(j) for j in re.findall(r'\d+', line)]
            for _ in range(values[0]):
                stacks[int(values[2] - 1)].append(stacks[values[1] - 1].pop())


def move_crates_9001(file_name):
    with open(file_name) as file:
        for line in file:
            values = [int(j) for j in re.findall(r'\d+', line)]
            crates = []
            for _ in range(values[0]):
                crates.append(stacks[values[1] - 1].pop())

            for _ in range(len(crates)):
                stacks[int(values[2] - 1)].append(crates.pop())


def peek():
    result = ""
    for i in range(len(stacks)):
        result += re.sub('[\[\]]', '', stacks[i].pop())

    return result


def crate_mover_9000():
    build_stack("day5_input_stack", 9)
    move_crates_9000("day5_input_moves")
    print(peek())


def crate_mover_9001():
    build_stack("day5_input_stack", 9)
    move_crates_9001("day5_input_moves")
    print(peek())
