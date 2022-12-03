import pytest

from advent_of_code_2022.Day3.day3_solution import split_rucksack_item, find_common_elements, get_priority, \
    find_common_badge

test_input_data = [
    ("vJrwpWtwJgWrhcsFMMfFFhFp", "vJrwpWtwJgWr", "hcsFMMfFFhFp"),
    ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
    ("PmmdzqPrVvPwwTWBwg", "PmmdzqPrV", "vPwwTWBwg")
]

common_test_data = [
    ("vJrwpWtwJgWr", "hcsFMMfFFhFp", {"p"}),
    ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL", {"L"}),
    ("PmmdzqPrV", "vPwwTWBwg", {"P"})
]

priority_test_data = [
    ("p", 16), ("L", 38), ("P", 42), ("v", 22), ("t", 20), ("s", 19)
]

badge_test_data = [
    ("vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "r"),
    ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw", "Z")
]


@pytest.mark.parametrize("input, expected1, expected2", test_input_data)
def test_split_rucksack_item(input, expected1, expected2):
    res1, res2 = split_rucksack_item(input)
    assert res1 == expected1 and res2 == expected2


@pytest.mark.parametrize("input1, input2, expected", common_test_data)
def test_find_common_elements(input1, input2, expected):
    assert find_common_elements(input1, input2) == expected


@pytest.mark.parametrize("input, expected", priority_test_data)
def test_get_priority(input, expected):
    assert get_priority(input) == expected


@pytest.mark.parametrize("input1, input2, input3, expected", badge_test_data)
def test_find_common_badge(input1, input2, input3, expected):
    assert find_common_badge(input1, input2, input3) == expected
