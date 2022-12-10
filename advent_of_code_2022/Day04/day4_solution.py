def in_range(range1, range2) -> bool:
    return range1[1] <= range2[1] and range1[0] >= range2[0] or \
           range2[1] <= range1[1] and range2[0] >= range1[0]


def overlap(range1, range2) -> bool:
    return bool(set(range1) & set(range2))


def function1(file_name):
    count = 0
    with open(file_name) as file:
        for line in file:
            range1, range2 = line.split(',')
            if in_range(list(map(int, range1.strip().split('-'))), list(map(int, range2.strip().split('-')))):
                count += 1

    return count


def function2(file_name):
    count = 0
    with open(file_name) as file:
        for line in file:
            ranges = line.split(',')
            range1 = list(map(int, ranges[0].strip().split('-')))
            range2 = list(map(int, ranges[1].strip().split('-')))
            if overlap(range(range1[0], range1[1] + 1), range(range2[0], range2[1] + 1)):
                count += 1

    return count
