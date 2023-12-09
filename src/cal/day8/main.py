"""day 8 of Advent of Code 2023.

advent of code: https://adventofcode.com/2023/day/7
"""

import sys
from cal.day8.utils import part_one, part_two

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("""
                Please provide the input file path as a command line argument:

                poetry run python -m cal.day8.main data/day7/input.txt
            """)
        sys.exit(1)

    input_file = sys.argv[1]

    print(part_one(input_file))
    print(part_two(input_file))
