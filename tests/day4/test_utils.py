import pytest
from cal.day4.utils import count_copies, count_winners, get_score, parse_card_number, parse_line, parse_results, part_one, parse_input
from unittest.mock import MagicMock


# Test parse_line function
@pytest.mark.parametrize("line, expected", [
    [
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        (6, ['74', '77', '10', '23', '35', '67', '36', '11'], {
            '31': True,
            '18': True,
            '13': True,
            '56': True,
            '72': True,
        })
    ],
])
def test_parse_line(line, expected):
    number, numbers, winning_numbers = expected
    r_number, r_numbers, r_winning_numbers = parse_line(line)
    assert number == r_number
    assert numbers == r_numbers
    assert winning_numbers == r_winning_numbers


# Test parse_card_number function
@pytest.mark.parametrize(
    "line, expected",
    [["Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11", 6],
     ["Card   9: 21 26 37 87 88 98 50 34 43 39 | 29 77 18 78 36 92", 9],
     ["Card 1: 0 | 0", 1], ["Card  10: 30 26 | 30 26", 10]])
def test_parse_card_number(line, expected):
    assert parse_card_number(line) == expected


# Test parse_results function
@pytest.mark.parametrize("line, expected", [[
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ({
        '31': True,
        '18': True,
        '13': True,
        '56': True,
        '72': True,
    }, ['74', '77', '10', '23', '35', '67', '36', '11'])
]])
def test_parse_results(line, expected):
    assert parse_results(line) == expected


# Test get_score function
@pytest.mark.parametrize("numbers,winning_numbers,expected",
                         [[['74', '77', '10', '23', '35', '67', '36', '11'], {
                             '31': True,
                             '18': True,
                             '13': True,
                             '56': True,
                             '72': True,
                         }, 0],
                          [['41', '48', '83', '86', '17'], {
                              '83': True,
                              '86': True,
                              '6': True,
                              '31': True,
                              '17': True,
                              '9': True,
                              '48': True,
                              '53': True
                          }, 8]])
def test_get_score(numbers, winning_numbers, expected):
    assert expected == get_score(numbers, winning_numbers)


def test_part_one():
    assert 13 == part_one('data/day4/input.test.txt')


@pytest.mark.parametrize("path, expected, result",
                         [[['41', '48', '6', '86', '17'], {
                             '83': True,
                             '86': True,
                             '6': True
                         }, 2]])
def test_count_winners(path, expected, result):
    assert count_winners(path, expected) == result


@pytest.mark.parametrize("path, expected", [[[
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
], {
    1: 1,
    2: 2,
    3: 4,
    4: 8,
    5: 14,
    6: 1
}]])
def test_count_copies(path, expected):
    assert expected == count_copies(path)
