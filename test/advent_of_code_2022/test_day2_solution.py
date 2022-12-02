import pytest

from advent_of_code_2022.Day2.day2_solution import RockPaperScissors

function1_test_data = [
    ("A", "Y", 8),
    ("B", "X", 1),
    ("C", "Z", 6)
]

function2_test_data = [
    ("A", "Y", 4),
    ("B", "X", 1),
    ("C", "Z", 7)
]


@pytest.mark.parametrize("input1, input2, expected", function1_test_data)
def test_function1(input1, input2, expected):
    result = RockPaperScissors.function1(RockPaperScissors(input2), input1)
    assert result == expected


@pytest.mark.parametrize("input1, input2, expected", function2_test_data)
def test_function2(input1, input2, expected):
    result = RockPaperScissors.function2(RockPaperScissors(input2), input1)
    assert result == expected
