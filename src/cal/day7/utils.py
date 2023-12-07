from enum import Enum
from typing import List

cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


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
    lambda hand: (len(hand) == 5 and len(set(hand)) == 1) or len(hand) == 0,
    Hand.FOUR_OF_A_KIND:
    lambda hand: len(hand) > 3 and
    (hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4),
    Hand.FULL_HOUSE:
    lambda hand: len(hand) == 5 and len(set(hand)) == 2 and not handTerms[
        Hand.FOUR_OF_A_KIND](hand),
    Hand.THREE_OF_A_KIND:
    lambda hand: len(hand) > 2 and
    (hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[
        2]) == 3 and not handTerms[Hand.FULL_HOUSE](hand)),
    Hand.TWO_PAIR:
    lambda hand: len(set(hand)) == 3 and len(hand) == 5 or len(
        hand) == 4 and len(set(hand)) == 2,
    Hand.ONE_PAIR:
    lambda hand: len(hand) > 1 and (len(set(hand)) == len(hand) - 1),
    Hand.HIGH_CARD:
    lambda hand: len(set(hand)) == 5 or len(hand) == 1
}


def get_type_of_hand_with_joker(hand: Hand, jokers: int) -> Hand:
    if jokers == 0:
        return hand
    if jokers == 1:
        if hand == Hand.HIGH_CARD:
            return Hand.ONE_PAIR
        if hand == Hand.ONE_PAIR:
            return Hand.THREE_OF_A_KIND
        if hand == Hand.TWO_PAIR:
            return Hand.FULL_HOUSE
        if hand == Hand.THREE_OF_A_KIND:
            return Hand.FOUR_OF_A_KIND
        if hand == Hand.FOUR_OF_A_KIND:
            return Hand.FIVE_OF_A_KIND
    if jokers == 2:
        if hand == Hand.HIGH_CARD:
            return Hand.THREE_OF_A_KIND
        if hand == Hand.ONE_PAIR:
            return Hand.FOUR_OF_A_KIND
        if hand == Hand.THREE_OF_A_KIND:
            return Hand.FIVE_OF_A_KIND
    if jokers == 3:
        if hand == Hand.HIGH_CARD:
            return Hand.FOUR_OF_A_KIND
        if hand == Hand.ONE_PAIR:
            return Hand.FIVE_OF_A_KIND
    if jokers == 4:
        return Hand.FIVE_OF_A_KIND
    if jokers == 5:
        return Hand.FIVE_OF_A_KIND


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


def compare_hands_with_jokers(l: List[str], r: List[str]):
    return compare_hands(l, r, True)


def compare_hands(l: List[str],
                  r: List[str],
                  jokers_active: bool = False) -> bool:
    l_hand = l[0]
    r_hand = r[0]
    l_type = get_type_of_hand(l_hand)
    r_type = get_type_of_hand(r_hand)
    if jokers_active:
        l_type = get_type_of_hand(l_hand.replace('J', ''))
        r_type = get_type_of_hand(r_hand.replace('J', ''))
        l_type = get_type_of_hand_with_joker(l_type, l_hand.count('J'))
        r_type = get_type_of_hand_with_joker(r_type, r_hand.count('J'))
    if l_type is None or r_type is None:
        raise Exception("An error occurred.")

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
    lines = parse_lines(path)
    hands = split_lines(lines)
    hands = quick_sort_hands(hands, compare_hands_with_jokers)
    s = 0
    for i in range(len(hands)):
        s += hands[i][1] * (i + 1)

    return s
