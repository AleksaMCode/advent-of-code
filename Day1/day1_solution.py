elfs = []


def get_max_calories():
    calories = 0
    with open("input") as file:
        for line in file:
            line = line.strip()
            if not line:
                elfs.append(calories)
                calories = 0
            else:
                calories += int(line)

    elfs.sort()
    print(elfs[-1:])


def sum_of_top_3():
    print(sum(elfs[-3:]))


get_max_calories()
sum_of_top_3()
