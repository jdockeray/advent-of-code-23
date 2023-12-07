from typing import List

words: dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


class NumsIterator:

    def __init__(self, data, reverse=False):
        self.data = data
        self.index = reverse and len(data) - 1 or 0
        self.reverse = reverse

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        reverse = self.reverse
        data = self.data

        if (not reverse and index >= len(data)) or (reverse and index < 0):
            raise StopIteration

        value = data[index]

        if value.isdigit():
            index = reverse and index - 1 or index + 1
            return value

        for word, digit in words.items():
            left = index
            right = index + len(word)

            if reverse:
                left = index - (len(word) - 1)
                right = index + 1

            if data[left:right] == word:
                if reverse:
                    index -= len(word)
                else:
                    index += len(word)
                return digit
        if reverse:
            self.index = index - 1
        else:
            self.index = index + 1

        return self.__next__()


def parse_input(path: str) -> List[str]:
    with open(path, 'r') as f:
        return f.read().splitlines()


def first(input: List[str]) -> str:
    nums = NumsIterator(input)
    next_value = next(nums)
    return next_value


def last(input: List[str]) -> int:
    nums = NumsIterator(input, reverse=True)
    next_value = next(nums)
    return next_value


def convert(strings: List[str]) -> int:
    result: int = 0

    for string in strings:
        result += int(first(string) + last(string))
    return result
