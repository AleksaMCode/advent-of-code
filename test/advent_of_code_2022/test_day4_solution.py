import pytest

from advent_of_code_2022.Day4.day4_solution import in_range, overlap

test_input_data_range = [
    ("2-4", "6-8", False),
    ("2-3", "4-5", False),
    ("5-7", "7-9", False),
    ("2-8", "3-7", True),
    ("6-6", "4-6", True),
    ("2-6", "4-8", False),
]

test_input_data_overlap = [
    ("2-4", "6-8", False),
    ("2-3", "4-5", False),
    ("5-7", "7-9", True),
    ("2-8", "3-7", True),
    ("6-6", "4-6", True),
    ("2-6", "4-8", True),
]


@pytest.mark.parametrize("range1, range2, expected", test_input_data_range)
def test_in_range(range1, range2, expected):
    assert in_range(list(map(int, range1.split('-'))), list(map(int, range2.split('-')))) == expected


@pytest.mark.parametrize("range1, range2, expected", test_input_data_overlap)
def test_overlap(range1, range2, expected):
    range1 = list(map(int, range1.strip().split('-')))
    range2 = list(map(int, range2.strip().split('-')))

    assert overlap(range(range1[0], range1[1] + 1), range(range2[0], range2[1] + 1)) == expected
