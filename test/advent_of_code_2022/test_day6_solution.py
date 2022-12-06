import pytest

from advent_of_code_2022.Day6.day6_solution import unique_sequence

test_first_input_data = [
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)
]

test_second_input_data = [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)
]


@pytest.mark.parametrize("input, expected", test_first_input_data)
def test_first_part(input, expected):
    assert unique_sequence(input, 4)[1] == expected


@pytest.mark.parametrize("input, expected", test_second_input_data)
def test_second_part(input, expected):
    assert unique_sequence(input, 14)[1] == expected
