elfs = []


def parse_elves():
    calories = 0
    with open("input") as file:
        for line in file:
            line = line.strip()
            if not line:
                elfs.append(calories)
                calories = 0
            else:
                calories += int(line)


def top_elf_calories():
    elfs.sort()
    print(elfs[-1:])


def top3_elves_calories():
    print(sum(elfs[-3:]))


parse_elves()
top_elf_calories()
top3_elves_calories()
