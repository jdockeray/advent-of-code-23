import pytest
from cal.day2.utils import check_round, check_rounds, compare_scores, get_min_cubes, parse_round, total_rounds


@pytest.mark.parametrize("input,expected_result", [
    ["3 blue, 4 red, 2 green", (4, 3, 2)],
    ["1 red, 2 green, 6 blue", (1, 6, 2)],
    ["2 green", (0, 0, 2)],
])
def test_parse_round(input, expected_result):
    assert parse_round(input) == expected_result


@pytest.mark.parametrize("input,expected_result", [
    [[(4, 3, 0), (1, 6, 2), (0, 0, 2)], (5, 9, 4)],
])
def test_total_rounds(input, expected_result):
    assert total_rounds(input) == expected_result


@pytest.mark.parametrize("left,right,expected_result", [
    [(5, 9, 4), (5, 9, 4), True],
    [(5, 9, 4), (5, 9, 5), False],
    [(5, 9, 4), (5, 9, 3), False],
    [(5, 9, 4), (5, 8, 4), False],
    [(5, 9, 4), (4, 9, 4), False],
])
def test_compare_scores(left, right, expected_result):
    assert compare_scores(left, right) == expected_result


@pytest.mark.parametrize("left,right,expected_result", [
    [(5, 9, 4), (5, 9, 4), True],
    [(4, 9, 4), (5, 9, 4), False],
    [(0, 0, 0), (5, 9, 4), False],
])
def test_check_round(left, right, expected_result):
    assert check_round(max=left, round=right) == expected_result


@pytest.mark.parametrize("max,rounds,expected_result", [
    [(5, 9, 4), [(4, 3, 0), (1, 6, 2), (0, 0, 2)], True],
    [(2, 3, 1), [(4, 3, 0), (1, 6, 2), (0, 0, 3)], False],
    [(5, 9, 1), [(4, 3, 0), (1, 6, 2), (0, 0, 2), (0, 0, 2)], False],
])
def test_check_rounds(max, rounds, expected_result):
    assert check_rounds(max, rounds) == expected_result


@pytest.mark.parametrize("input,expected_result", [
    [[(4, 3, 0), (1, 6, 2), (0, 0, 2)], (4, 6, 2)],
])
def test_get_min_cubes(input, expected_result):
    assert get_min_cubes(input) == expected_result
