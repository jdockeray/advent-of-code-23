import pytest
from cal.day5.utils import convert_seed_to_source, convert_seeds_to_sources, parse_maps, parse_seeds, parse_seeds_as_ranges, part_one, part_two, split_seed_range

from cal.day5.utils import convert_seed_to_source


def test_parse_seeds():
    assert parse_seeds(['# seeds: 79 14 55 13']) == [79, 14, 55, 13]


@pytest.mark.parametrize(
    'lines, expected',
    [[["seeds: 79 14 55 13", "", "seed-to-soil map:", "50 98 2", "52 50 48"],
      ({
          'seed-to-soil': {
              range(98, 100): -48,
              range(50, 98): 2
          }
      }, ['seed-to-soil'])],
     [[
         "seeds: 79 14 55 13", "", "seed-to-soil map:", "50 98 2", "52 50 48",
         "", "fertilizer-to-water map:", "49 53 8", "0 11 42", ""
     ],
      ({
          'seed-to-soil': {
              range(98, 100): -48,
              range(50, 98): 2
          },
          'fertilizer-to-water': {
              range(53, 61): -4,
              range(11, 53): -11
          }
      }, ['seed-to-soil', 'fertilizer-to-water'])]])
def test_parse_maps(lines, expected):
    assert parse_maps(lines) == expected


@pytest.mark.parametrize('seed, keys, maps, expected',
                         [(55, ['seed-to-soil', 'fertilizer-to-water'], {
                             'seed-to-soil': {
                                 range(98, 100): -48,
                                 range(50, 98): 2
                             },
                             'fertilizer-to-water': {
                                 range(53, 61): -4,
                                 range(11, 53): -11
                             }
                         }, 53)])
def test_convert_seed_to_source(seed, keys, maps, expected):
    assert convert_seed_to_source(seed=seed, keys=keys, maps=maps) == expected


def test_part_one():
    assert part_one("data/day5/input.test.txt") == 35


def test_parse_seeds_as_ranges():
    assert parse_seeds_as_ranges([1, 2, 5, 1]) == [1, 2, 5]


def test_part_two():
    assert part_two("data/day5/input.txt") == 46


@pytest.mark.parametrize('seeds, maps, keys, expected', [
    ([range(1, 5)], {
        'seed-to-soil': {
            range(2, 4): 100
        }
    }, ['seed-to-soil'], [range(
        102, 104), range(1, 2), range(4, 5)]),
    ([range(1, 5)], {
        'seed-to-soil': {
            range(2, 4): 100
        },
        'fertilizer-to-water': {
            range(20, 25): 10
        }
    }, ['seed-to-soil', 'fertilizer-to-water'],
     [range(102, 104), range(1, 2), range(4, 5)]),
])
def test_convert_seeds_to_sources(seeds, maps, keys, expected):
    assert convert_seeds_to_sources(seeds, maps, keys) == expected


@pytest.mark.parametrize(
    'l, r, steps, processed, unprocessed',
    [(range(1, 5), range(10, 11), 3, (None, None, None),
      (None, range(10, 11), None)),
     (range(1, 100), range(10, 11), 300, (None, range(310, 311), None),
      (None, None, None)),
     (range(10, 11), range(1, 100), 300, (None, range(310, 311), None),
      (range(1, 10), None, range(11, 100))),
     (range(1, 11), range(1, 100), 300, (range(301, 311), None, None),
      (None, range(11, 100), None)),
     (range(1, 100), range(99, 100), 300, (None, range(399, 400), None),
      (None, None, None)),
     (range(53, 61), range(57, 70), 2, (None, range(59, 63), None),
      (None, None, range(61, 70))),
     (range(77, 100), range(74, 88), 0, (None, range(77, 88), None),
      (range(74, 77), None, None)),
     (range(10, 20), range(5, 20), 0, (None, range(10, 20), None),
      (range(5, 10), None, None)),
     (range(10, 20), range(10, 20), 0, (None, range(10, 20), None),
      (None, None, None)),
     (range(10, 30), range(10, 20), 0, (None, range(10, 20), None),
      (None, None, None))])
def test_split_seed_range(l, r, steps, processed, unprocessed):
    assert split_seed_range(l=l, r=r, steps=steps)[0] == processed
    assert split_seed_range(l=l, r=r, steps=steps)[1] == unprocessed
