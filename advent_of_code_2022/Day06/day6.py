from advent_of_code_2022.Day6.day6_solution import unique_sequence

file = open("day6_input", mode='r')
line = file.read()

print(unique_sequence(line, 4))
print(unique_sequence(line, 14))
