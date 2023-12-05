import pytest
from lib.day5.utils import convert_seed_to_source, parse_maps, parse_seeds, parse_seeds_as_ranges, part_one, part_two
import pytest
from lib.day5.utils import convert_seed_to_source


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
