elfs = []


def parse_elves(file_name: str):
    calories = 0
    with open(file_name) as file:
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


parse_elves("day1_input")
top_elf_calories()
top3_elves_calories()
