"""Utility functions to help solve day 4 of Advent of Code 2023.

advent of code: https://adventofcode.com/2023/day/4
"""

from typing import Dict, List


def parse_lines(path: str) -> List[str]:
    with open(path, 'r') as f:
        return f.read().splitlines()


def parse_seeds(lines: List[str]) -> List[int]:
    return [int(x) for x in lines[0].split(':')[1].strip().split(' ')]


def parse_seeds_as_ranges(seeds: List[int]) -> List[int]:
    many_seeds = []
    for i in range(0, len(seeds), 2):
        many_seeds.extend(list(range(seeds[i], seeds[i] + seeds[i + 1])))

    return many_seeds


def parse_maps(lines: List[str]) -> (Dict[str, Dict[range, int]], List[int]):
    """
    Parse the input file and return a dict of dicts.

    Args:
        lines (List[str]): The lines of the input file.

    Returns:
        Dict[str, Dict[range, int]]: A dict of dicts, where each dict represents a map.
    """
    maps = {}
    readingKey = False
    k = ''
    keys = []
    # start at index 1 as top of file is seeds
    for line in lines[1:]:
        if line == '':
            readingKey = True
            continue
        elif readingKey:
            k = line.split(' ')[0]
            keys.append(k)
            readingKey = False
        else:
            destination, source, step = map(lambda x: int(x), line.split(' '))
            map_range = range(source, source + step)
            map_increment = destination - source
            if k in maps:
                maps[k][map_range] = map_increment
            else:
                maps[k] = {map_range: map_increment}

    return maps, keys


def convert_seed_to_source(seed: int, maps: Dict[str, Dict[range, int]],
                           keys: List[str]) -> int:
    """
    Convert a seed to a source.

    Args:
        seed (int): The seed to convert.
        maps (Dict[str, Dict[range, int]]): The maps to use for the conversion.
        keys (List[str]): The list of keys.

    Returns:
        int: The source.
    """
    for k in keys:
        m = maps[k]
        matching_range = next((r for r in m.keys() if seed in r), None)
        if matching_range is not None:
            seed = seed + m[matching_range]
    return seed


def part_one(path: str) -> int:
    """
    Solve part one of the puzzle.

    Args:
        path (str): The path to the input file.

    Returns:
        int: The lowest location
    """
    lines = parse_lines(path)
    seeds = parse_seeds(lines)
    maps, keys = parse_maps(lines)
    return min(map(lambda x: convert_seed_to_source(x, maps, keys), seeds))


def part_two(path: str) -> int:
    lines = parse_lines(path)
    seeds = parse_seeds_as_ranges(parse_seeds(lines))
    maps, keys = parse_maps(lines)
    return min(map(lambda x: convert_seed_to_source(x, maps, keys), seeds))
