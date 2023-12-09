from cal.day8.utils import parse_directions_and_map, parse_lines, part_one, walk_atlas


def test_parse_directions_and_map():
    directions, atlas = parse_directions_and_map(
        ['RL', '', 'AAA = (BBB, CCC)', 'BBB = (DDD, EEE)'])
    assert directions == "RL"
    assert atlas == {'AAA': ['BBB', 'CCC'], 'BBB': ['DDD', 'EEE']}


def test_traverse_atlas():
    # instructions, atlas = parse_directions_and_map(parse_lines('data/day8/input.test.txt'))
    directions = "LLR"
    atlas = {
        'AAA': ['BBB', 'BBB'],
        'BBB': ['AAA', 'ZZZ'],
        'ZZZ': ['ZZZ', 'ZZZ']
    }
    assert walk_atlas(directions, atlas) == 6


def test_part_one():
    assert part_one('data/day8/input.test.txt') == 2
