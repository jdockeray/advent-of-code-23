import pytest
from cal.day1.utils import convert, parse_input, first, last
from unittest.mock import mock_open, patch
from typing import List


@pytest.mark.parametrize(
    "input,expected", [[["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"],
                        142], [["two1nine"], 29], [["eightwothree"], 83]])
def test_convert_simple(input, expected) -> None:
    result: int = convert(input)
    assert result == expected, "Conversion failed"


def test_read_file() -> None:
    with patch('builtins.open', mock_open(read_data='1\n2\n3')) as mock_file:
        result = parse_input('file.txt')
        assert result == ["1", "2", "3"], "Reading file failed"
        mock_file.assert_called_once_with('file.txt', 'r')


@pytest.mark.parametrize("str,expected",
                         [["1abc2", "1"], ["two1nine", "2"],
                          ["eightwothree", "8"], ["treb7uchet", "7"]])
def test_first(str, expected) -> None:
    result: int = first(str)
    assert result == expected, "First element is incorrect"


@pytest.mark.parametrize(
    "str,expected",
    [["1abc2", "2"], ["two1nine", "9"], ["eightwothree", "3"],
     ["treb7uchet", "7"], ["6lpxrrhvdslxgpjblcmgsgbdpdkfmzkr", "6"]])
def test_last(str, expected) -> None:
    result: int = last(str)
    assert result == expected, "Last element is incorrect"
