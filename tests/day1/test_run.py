from typing import List
from lib.day1.utils import convert, parse_input
from unittest.mock import mock_open, patch

sample: List[str] = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]


def test_convert() -> None:
    result: int = convert(sample)
    assert result == 142, "Conversion failed"


def test_read_file() -> None:
    with patch('builtins.open', mock_open(read_data='1\n2\n3')) as mock_file:
        result = parse_input('file.txt')
        assert result == ["1", "2", "3"], "Reading file failed"
        mock_file.assert_called_once_with('file.txt', 'r')
