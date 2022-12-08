from advent_of_code_2022.Day8.day8_solution import parse_input, solution

parse_input("day8_p1_test_input")


def test_first_part():
    assert solution()[0] == 21


def test_second_part():
    assert solution()[1] == 8
