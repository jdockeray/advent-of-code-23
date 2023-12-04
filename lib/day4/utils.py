"""Utility functions to help solve day 4 of Advent of Code 2023.

advent of code: https://adventofcode.com/2023/day/4
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


def parse_card_number(line: str) -> int:
    return int(line.split(':')[0].split(' ').pop())


def parse_results(line: str) -> (Dict[str, bool], List[str]):
    left, right = line.split(':')[1].split('|')
    winning_numbers = {
        x: True
        for x in filter(lambda x: x.strip().isdigit(), left.split(' '))
    }
    numbers = filter(lambda x: x.strip().isdigit(), right.split(' '))
    return (winning_numbers, numbers)


def parse_line(line: str) -> (int, List[str], Dict[str, bool]):
    """
    Parse the input file and return a list of strings.

    Args:
        path (str): The path to the input file.

    Returns:
        (int, List[str], Dict[str, bool]): A tuple containing the card number, the card numbers and the winning numbers.
    """
    card_number = parse_card_number(line)
    card_winning_numbers, card_numbers = parse_results(line)

    return (card_number, card_numbers, card_winning_numbers)


def get_score(card_numbers: List[str],
              card_winning_numbers: Dict[str, bool]) -> int:
    """
    Calculates the score based on the given card numbers and winning numbers.

    Args:
        card_numbers (List[str]): The list of card numbers.
        card_winning_numbers (Dict[str, bool]): The dictionary of winning numbers.

    Returns:
        int: The calculated score.

    """
    score = -1
    for number in card_numbers:
        if number in card_winning_numbers:
            score += 1
    return 0 if score == -1 else 2**score


def count_winners(card_numbers: List[str],
                  card_winning_numbers: Dict[str, bool]) -> int:
    """
    Counts the number of winning card numbers in the given list of card numbers.

    Args:
        card_numbers (List[str]): A list of card numbers.
        card_winning_numbers (Dict[str, bool]): A dictionary of card numbers and their winning status.

    Returns:
        int: The count of winning card numbers.

    """
    score = 0
    for number in card_numbers:
        if number in card_winning_numbers:
            score += 1
    return score


def part_one(path: str) -> int:
    """
    Parse the input file and return the score

    Args:
        path (str): The path to the input file.

    Returns:
        score (int): The score of the scratch card.
    """
    lines = parse_input(path)
    scores = []

    for line in lines:
        card_number, card_numbers, card_winning_numbers = parse_line(line)
        scores.append(get_score(card_numbers, card_winning_numbers))

    return sum(scores)


def count_copies(lines: List[str]) -> Dict[int, int]:
    """
    Counts the number of copies for each card based on the given lines.

    Args:
        lines (List[str]): The list of lines containing card information.

    Returns:
        Dict[int, int]: A dictionary where the keys are card numbers and the values are the number of copies for each card.
    """
    cards = {}
    cards_winners = {}
    last_card_number = 0

    for line in lines:
        card_number, card_numbers, card_winning_numbers = parse_line(line)

        # account for original card
        cards[card_number] = 1

        # count the winners and last card number
        cards_winners[card_number] = count_winners(card_numbers,
                                                   card_winning_numbers)
        last_card_number = card_number if card_number > last_card_number else last_card_number

    for i in range(1, last_card_number + 1):
        number_of_winners = cards_winners[i]
        for j in range(i + 1, i + number_of_winners + 1):
            number_of_copies = int(cards[i])
            number_of_cards = int(cards[j])
            cards[j] = number_of_copies + number_of_cards
    return cards


def part_two(path: str) -> int:
    """
    Parse the input file and count the copies

    Args:
        path (str): The path to the input file.

    Returns:
        count (int): The number of copies
    """
    lines = parse_input(path)
    copies = count_copies(lines)

    return sum(copies.values())
