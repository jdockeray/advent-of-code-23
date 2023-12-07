import pytest
from cal.day7.utils import Hand, compare_cards, compare_hands, get_type_of_hand, part_one, part_two, quick_sort_hands, split_lines


def test_split_lines():
    assert split_lines(['32T3K 765', 'QQQJA 483']) == [['32T3K', 765],
                                                       ['QQQJA', 483]]


@pytest.mark.parametrize("hand, expected_type",
                         [('AAAAA', Hand.FIVE_OF_A_KIND),
                          ('AA8AA', Hand.FOUR_OF_A_KIND),
                          ('23332', Hand.FULL_HOUSE),
                          ('TTT98', Hand.THREE_OF_A_KIND),
                          ('23432', Hand.TWO_PAIR), ('A23A4', Hand.ONE_PAIR),
                          ('23456', Hand.HIGH_CARD), ('2', Hand.HIGH_CARD),
                          ('AAKK', Hand.TWO_PAIR), ('33', Hand.ONE_PAIR),
                          ('KKK', Hand.THREE_OF_A_KIND),
                          ('JJJJJ', Hand.FIVE_OF_A_KIND)])
def test_get_type_of_hand(hand, expected_type):
    assert get_type_of_hand(hand) == expected_type


def test_quick_sort_hands():
    assert quick_sort_hands([1, 2, 7, 2], lambda x, y: x < y) == [1, 2, 2, 7]


def test_compare_cards():
    assert compare_cards('A', 'K')
    assert compare_cards('A', 'A')
    assert compare_cards('KA', 'K2')
    assert not compare_cards('K', 'A')
    assert not compare_cards('2', '4')


def test_compare_hands():
    assert not compare_hands(['AAAAA', 1], ['KKKKK', 2])
    assert not compare_hands(['A3456', 1], ['K3456', 2])
    assert not compare_hands(['33456', 1], ['K3456', 2])
    assert compare_hands(['AAAA2', 1], ['AAAA3', 2])


def test_part_one():
    assert part_one('data/day7/input.test.txt') == 6440


def test_part_two():
    assert part_two('data/day7/input.txt') == 6440


# def test_get_type_of_hand_with_joker()
