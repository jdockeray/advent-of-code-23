from typing import List


def parse_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        return f.read().splitlines()


def convert(strings: List[str]) -> int:
    result = 0

    for string in strings:
        filtered = list(filter(lambda char: char.isdigit(), string))
        result += int(filtered[0] + filtered[-1])
    return result
