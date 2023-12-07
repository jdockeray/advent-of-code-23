"""day 7 of Advent of Code 2023.

advent of code: https://adventofcode.com/2023/day/7
"""

import sys
from cal.day7.utils import part_one, part_two

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("""
                Please provide the input file path as a command line argument:

                poetry run python lib/day7/main.py data/day7/input.txt
            """)
        sys.exit(1)

    input_file = sys.argv[1]

    print(part_one(input_file))
    print(part_two(input_file))