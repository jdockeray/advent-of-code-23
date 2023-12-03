"""Functions to help solve day 2 of Advent of Code 2023.

advent of code: https://adventofcode.com/2023/day/2
"""

from typing import List
from functools import reduce
from typing import List


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


def parse_round(r: str) -> (int, int, int):
    """
    Parses a round string and returns the count of red, blue, and green colors.

    Args:
        r (str): The round string in the format "count color, count color, count color".

    Returns:
        Tuple[int, int, int]: A tuple containing the count of red, blue, and green colors respectively.
    """
    red, blue, green = 0, 0, 0
    combos = r.split(',')
    for combo in combos:
        combo = combo.strip()
        count, color = combo.split(' ')
        count = int(count)
        if color == 'red':
            red += count
        elif color == 'blue':
            blue += count
        elif color == 'green':
            green += count

    return (red, blue, green)


def parse_line(line: str) -> (int, list[(int, int, int)]):
    """
    Parses a line of input and returns a tuple containing the game number and a list of rounds.

    Args:
        line (str): The input line to be parsed.

    Returns:
        tuple: A tuple containing the game number and a list of rounds.

    Example:
        >>> parse_line("Game 1: 1,2,3;4,5,6")
        (1, [(1, 2, 3), (4, 5, 6)])
    """
    left, right = line.split(':')
    game = int(left.split(' ')[1])

    roundsStrs: list[str] = right.split(';')
    rounds: list[(int, int, int)] = []

    for str in roundsStrs:
        rounds.append(parse_round(str))

    return (game, rounds)


def total_rounds(rounds: list[(int, int, int)]) -> (int, int, int):
    """
    Calculates the total of each element in the given list of rounds.

    Parameters:
    rounds (list[(int, int, int)]): A list of tuples representing rounds.

    Returns:
    (int, int, int): A tuple representing the total of each element in the rounds.
    """
    return reduce(lambda x, y: (x[0] + y[0], x[1] + y[1], x[2] + y[2]), rounds)


def compare_scores(left: (int, int, int), right: (int, int, int)) -> bool:
    """
    Compare two scores.

    Args:
        left: A tuple representing the left score.
        right: A tuple representing the right score.

    Returns:
        True if the left score is equal to the right score, False otherwise.
    """
    return left == right


def check_round(max: (int, int, int), round: (int, int, int)) -> bool:
    """
    Check if a given round is within the maximum limits.

    Args:
        max: A tuple representing the maximum limits for each color (red, blue, green).
        round: A tuple representing the values of each color in the round.

    Returns:
        True if the round is within the maximum limits, False otherwise.
    """
    r_red, r_blue, r_green = round
    m_red, m_blue, m_green = max
    return r_red <= m_red and r_blue <= m_blue and r_green <= m_green


def check_rounds(max: list[(int, int, int)],
                 rounds: list[(int, int, int)]) -> bool:
    """
    Check if all rounds in the given list are below the maximum limits.

    Args:
        max (list[(int, int, int)]): A list of tuples representing the maximum values for each round.
        rounds (list[(int, int, int)]): A list of tuples representing the rounds to be checked.

    Returns:
        bool: True if all rounds satisfy the condition, False otherwise.
    """
    return reduce(lambda x, y: x and check_round(max, y), rounds, True)


def get_min_cubes(rounds: list[(int, int, int)]) -> [int, int, int]:
    """
    Get the minimum number of cubes by color needed to play the given rounds.

    Args:
        rounds (list[(int, int, int)]): A list of tuples representing the rounds to be played.

    Returns:
        int: The minimum number of cubes needed to play the given rounds.
    """
    red, blue, green = (0, 0, 0)
    for round in rounds:
        r_red, r_blue, r_green = round
        red = max(red, r_red)
        blue = max(blue, r_blue)
        green = max(green, r_green)

    return (red, blue, green)


def part_one(file):
    """
    Calculate the total score of a game based on the id of legal ganmes.

    Args:
        file (str): The path to the input file.

    Returns:
        int: The total score of the game.
    """
    lines = parse_input(file)
    term = (12, 14, 13)
    total = 0
    for line in lines:
        game, rounds = parse_line(line)
        legal = check_rounds(term, rounds)

        if legal:
            total += game
    return total


def part_two(file):
    """
    Calculate the powers based off the min cubes needed to play the game.

    Args:
        file (str): The path to the input file.

    Returns:
        int: The total score of the powers.
    """
    lines = parse_input(file)
    total = 0
    for line in lines:
        _, rounds = parse_line(line)
        cubes = get_min_cubes(rounds)
        total += reduce(lambda x, y: x * y, cubes, 1)
    return total
