"""Utility functions to help solve day 4 of Advent of Code 2023.

advent of code: https://adventofcode.com/2023/day/4
"""

from typing import Dict, List


def parse_lines(path: str) -> List[str]:
    with open(path, 'r') as f:
        return f.read().splitlines()


def parse_seeds(lines: List[str]) -> List[int]:
    return [int(x) for x in lines[0].split(':')[1].strip().split(' ')]


def parse_seeds_as_ranges(seeds: List[int]) -> List[range]:
    ranges = []
    for i in range(0, len(seeds), 2):
        cr = range(seeds[i], seeds[i] + seeds[i + 1])
        ranges.append(cr)
    return ranges


def split_seed_range(
        l: range, r: range,
        steps: int) -> ((range, range, range), (range, range, range)):
    """
    Splits the seed ranges into processed and unprocessed ranges based on certain conditions.

    Args:
        l (range): The map range.
        r (range): The seed range (the numbers being acted on)
        steps (int): The number of steps to add to the processed ranges.

    Returns:
        tuple: (processed, unprocessed)
    """
    processed = (None, None, None)
    unprocessed = (None, None, None)
    if l.start < r.start and l.stop > r.stop:
        processed = (None, range(r.start + steps, r.stop + steps), None)
    elif l.stop <= r.start or l.start >= r.stop:
        processed = (None, None, None)
        unprocessed = (None, r, None)
    elif l.start > r.start and l.stop < r.stop:
        processed = (None, range(l.start + steps, l.stop + steps), None)
        unprocessed = (range(r.start, l.start), None, range(l.stop, r.stop))
    elif l.start == r.start and l.stop < r.stop:
        processed = (range(l.start + steps, l.stop + steps), None, None)
        unprocessed = (None, range(l.stop, r.stop), None)
    elif l.start < r.start and l.stop == r.stop:
        processed = (None, range(r.start + steps, r.stop + steps), None)
    elif l.start < r.start and l.stop < r.stop:
        processed = (None, range(r.start + steps, l.stop + steps), None)
        unprocessed = (None, None, range(l.stop, r.stop))
    elif l.start > r.start and l.stop > r.stop:
        processed = (None, range(l.start + steps, r.stop + steps), None)
        unprocessed = (range(r.start, l.start), None, None)
    elif l.start > r.start and l.stop == r.stop:
        processed = (None, range(l.start, r.stop), None)
        unprocessed = (range(r.start, l.start), None, None)
    elif l.start == r.start and l.stop == r.stop:
        processed = (None, range(l.start + steps, r.stop + steps), None)
        unprocessed = (None, None, None)
    elif l.start == r.start and l.stop > r.stop:
        processed = (None, range(r.start + steps, r.stop + steps), None)
        unprocessed = (None, None, None)
    return (processed, unprocessed)


def parse_maps(lines: List[str]) -> (Dict[str, Dict[range, int]], List[int]):
    """
    Parses the given lines to create maps and keys.

    Args:
        lines (List[str]): The lines to parse.

    Returns:
        Tuple[Dict[str, Dict[range, int]], List[int]]: A tuple containing the maps and keys.
            - maps: A dictionary where the keys are strings and the values are dictionaries.
                    Each inner dictionary represents a range of integers and its corresponding increment value.
            - keys: A list of strings representing the keys.

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


def convert_seeds_to_sources(seeds: List[range], maps: Dict[str, Dict[range,
                                                                      int]],
                             keys: List[str]) -> List[range]:
    """
    Convert the given seeds to sources based on the provided maps and keys.

    Args:
        seeds (List[range]): The initial seed ranges.
        maps (Dict[str, Dict[range, int]]): The maps containing the range increments for each key.
        keys (List[str]): The keys to process.

    Returns:
        List[range]: The processed ranges after conversion.

    Raises:
        Exception: If the output length does not match the input length.

    """
    processed = []
    unprocessed = seeds
    for k in keys:
        m = maps[k]
        available = unprocessed
        processed = []
        for check_r, incr in m.items():
            next_available = []
            for r in available:
                in_len = len(r)
                (p, u) = split_seed_range(l=check_r, r=r, steps=incr)
                p = [x for x in p if x is not None]
                u = [x for x in u if x is not None]
                p_len = sum([len(x) for x in p])
                u_len = sum([len(x) for x in u])
                out_len = p_len + u_len
                if out_len != in_len:
                    raise Exception(
                        f'Out length {out_len} does not match in length {in_len}'
                    )

                next_available.extend(u)
                processed.extend(p)
            available = next_available
        unprocessed = processed
        unprocessed.extend(available)

    processed = [p for p in processed if p is not None]
    return processed


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
    sources = convert_seeds_to_sources(seeds, maps, keys)

    return min(map(lambda x: x.start, sources))
