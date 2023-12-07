from enum import Enum
from typing import List

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


class Hand(Enum):
    FIVE_OF_A_KIND = 700
    FOUR_OF_A_KIND = 600
    FULL_HOUSE = 500
    THREE_OF_A_KIND = 400
    TWO_PAIR = 300
    ONE_PAIR = 200
    HIGH_CARD = 100


handTerms = {
    Hand.FIVE_OF_A_KIND:
    lambda hand: len(set(hand)) == 1,
    Hand.FOUR_OF_A_KIND:
    lambda hand: hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4,
    Hand.FULL_HOUSE:
    lambda hand: len(set(hand)) == 2 and not handTerms[Hand.FOUR_OF_A_KIND]
    (hand),
    Hand.THREE_OF_A_KIND:
    lambda hand: hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.
    count(hand[2]) == 3 and not handTerms[Hand.FULL_HOUSE](hand),
    Hand.TWO_PAIR:
    lambda hand: len(set(hand)) == 3 and not handTerms[Hand.THREE_OF_A_KIND]
    (hand),
    Hand.ONE_PAIR:
    lambda hand: len(set(hand)) == 4,
    Hand.HIGH_CARD:
    lambda hand: len(set(hand)) == 5
}


def parse_lines(path: str) -> List[str]:
    with open(path, 'r') as f:
        return f.read().splitlines()


def split_lines(lines: List[str]) -> List[List[str]]:
    result = []
    for line in lines:
        tmp = line.split(' ')
        result.append([tmp[0], int(tmp[1])])
    return result


def get_type_of_hand(hand: str) -> Hand:
    for handType in Hand:
        if handTerms[handType](hand):
            return handType
    return Hand.HIGH_CARD


def compare_cards(l: str, r: str) -> bool:
    l_score = cards.index(l[0])
    r_score = cards.index(r[0])
    idx = 1
    while l_score == r_score and idx != len(l):
        l_score = cards.index(l[idx])
        r_score = cards.index(r[idx])
        idx += 1
    return cards.index(l[idx - 1]) >= cards.index(r[idx - 1])


def compare_hands(l: List[str], r: List[str]):
    l_hand = l[0]
    r_hand = r[0]
    l_type = get_type_of_hand(l_hand)
    r_type = get_type_of_hand(r_hand)
    if l_type == r_type:
        return compare_cards(r_hand, l_hand)
    return l_type.value < r_type.value


def quick_sort_hands(array, comparator):
    if len(array) < 2:
        return array
    left, right = ([], [])
    pivot = array[0]
    for item in array[1:]:
        if comparator(item, pivot):
            left.append(item)
        else:
            right.append(item)
    return quick_sort_hands(left, comparator) + [pivot] + quick_sort_hands(
        right, comparator)


def part_one(path: str) -> int:
    lines = parse_lines(path)
    hands = split_lines(lines)
    hands = quick_sort_hands(hands, compare_hands)
    s = 0
    for i in range(len(hands)):
        s += hands[i][1] * (i + 1)

    return s


def part_two(path: str) -> int:
    return 0
