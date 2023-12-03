import pytest
from lib.day3.utils import get_parts_and_gears, match_parts, part_two


@pytest.mark.parametrize(
    "grid, expected",
    [[["467..114..", "...*......", "..35..633.", "......#...", "617*......"],
      ([467, 35, 633, 617], {})]])
def test_get_parts(grid, expected):
    expected_parts, _ = expected
    assert get_parts_and_gears(grid)[0] == expected_parts


@pytest.mark.parametrize("grid, x_list, y, expected",
                         [[["467..114..", "...*......"],
                           range(0, 3), 0, [("*", 3, 1)]],
                          [[".@.", ".1.", "..."],
                           range(1, 2), 1, [("@", 1, 0)]],
                          [["..@", ".1.", "..."],
                           range(1, 2), 1, [("@", 2, 0)]],
                          [["...", ".1@", "..."],
                           range(1, 2), 1, [("@", 2, 1)]],
                          [["...", ".1.", "..@"],
                           range(1, 2), 1, [("@", 2, 2)]],
                          [["...", ".1.", ".@."],
                           range(1, 2), 1, [("@", 1, 2)]],
                          [["...", ".1.", "@.."],
                           range(1, 2), 1, [("@", 0, 2)]],
                          [["...", "@1.", "..."],
                           range(1, 2), 1, [("@", 0, 1)]],
                          [["@..", ".1.", "..."],
                           range(1, 2), 1, [("@", 0, 0)]]])
def test_is_part(grid, x_list, y, expected):
    char, x, y = match_parts(grid, x_list, y)[0]
    assert char == expected[0][0]
    assert x == expected[0][1]
    assert y == expected[0][2]


def test_is_part_empty():
    assert match_parts(["..."], range(0, 3), 0) == []


def test_is_part_two_matches():
    assert match_parts(["@1@.."], range(1, 2), 0) == [("@", 2, 0), ("@", 0, 0)]


def test_part_two():
    assert part_two("data/day3/input.test.txt") == 467835
