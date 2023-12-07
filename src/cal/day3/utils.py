"""Utility functions to help solve day 3 of Advent of Code 2023.

advent of code: https://adventofcode.com/2023/day/3
"""
from typing import Dict, List


def parse_input(path: str) -> List[str]:
    """
    Parse the input file and return a list of strings.

    Args:
        path (str): The path to the input file.

    Returns:
        List[str]: A list of strings, where each string represents a line in the file.
    """
    with open(path, 'r') as f:
        return f.read().splitlines()


is_special = lambda x: (not x.isdigit()) and x != '.'


def match_parts(grid: List[str], x_list: List[int],
                y: int) -> list[(str, int, int)]:
    """
    Check if the given series of x coordinates and one y coordinate
    are adjacent to a speacial character. Parts are adjacent if they
    have a special character north, north east, east, south east, south,
    south west, and north west of them.

    Args:
        grid (List[str]): The grid to check.
        x List[int]: The x coordinates.
        y (int): The y coordinate.

    Returns:
        List[(str, int, int)]: A list of tuples containing the special character and coordinates.
    """
    col_size = len(grid)
    row_size = len(grid[0])

    items = []
    for x in x_list:
        # North
        if y > 0 and is_special(grid[y - 1][x]):
            items.append((grid[y - 1][x], x, y - 1))

        # North East
        if y > 0 and x < row_size - 1 and is_special(grid[y - 1][x + 1]):
            items.append((grid[y - 1][x + 1], x + 1, y - 1))

        # East
        if x < row_size - 1 and is_special(grid[y][x + 1]):
            items.append((grid[y][x + 1], x + 1, y))

        # South East
        if y < col_size - 1 and x < row_size - 1 and is_special(
                grid[y + 1][x + 1]):
            items.append((grid[y + 1][x + 1], x + 1, y + 1))

        # South
        if y < col_size - 1 and is_special(grid[y + 1][x]):
            items.append((grid[y + 1][x], x, y + 1))

        # South West
        if y < col_size - 1 and x > 0 and is_special(grid[y + 1][x - 1]):
            items.append((grid[y + 1][x - 1], x - 1, y + 1))

        # West
        if x > 0 and is_special(grid[y][x - 1]):
            items.append((grid[y][x - 1], x - 1, y))

        # North West
        if y > 0 and x > 0 and is_special(grid[y - 1][x - 1]):
            items.append((grid[y - 1][x - 1], x - 1, y - 1))
    return items


def get_parts_and_gears(
    grid: List[str]
) -> (List[int], Dict[str, List[int]], Dict[str, List[int]]):
    """
    Get the parts and gears of the grid.

    Args:
        grid (List[str]): The grid to be split.

    Returns:
        List[int]: A list of parts of the grid.
    """
    parts = []
    x_start = -1
    reading = False

    gearMap = {}

    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            is_end = False

            if char.isdigit() and not reading:
                x_start = col
                reading = True

            if col == len(line) - 1 or not line[col + 1].isdigit():
                is_end = True

            if is_end and reading:
                reading = False
                matches = match_parts(grid, range(x_start, col + 1), row)
                num = int(line[x_start:col + 1])
                for match in matches:
                    char, x, y = match
                    if char == "*":
                        key = f"{x},{y}"
                        if key not in gearMap:
                            gearMap[key] = []
                        gearMap[key].append(num)

                if len(matches) > 0:
                    parts.append(num)

    return (parts, gearMap)


def part_one(path: str) -> int:
    """
    Get the sum of the parts of the grid.

    Args:
        path (str): The path to the input file.

    Returns:
        int: The sum of the parts of the grid.
    """
    grid = parse_input(path)
    parts, _ = get_parts_and_gears(grid)
    return sum(parts)


def part_two(path: str) -> int:
    """
    Get the sum of the gears of the grid.

    Args:
        path (str): The path to the input file.

    Returns:
        int: The sum of the gears of the grid.
    """
    grid = parse_input(path)
    _, gearMap = get_parts_and_gears(grid)
    sum = 0

    for key, vals in gearMap.items():
        vals_set = set(vals)
        if len(vals_set) == 2:
            product = 1
            for val in vals_set:
                product *= val
            sum += product
    return sum
