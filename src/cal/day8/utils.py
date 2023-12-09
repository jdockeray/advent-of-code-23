from typing import Dict, List


def parse_lines(path: str) -> List[str]:
    with open(path, 'r') as f:
        return f.read().splitlines()


def parse_directions_and_map(lines: List[str]) -> (str, Dict[str, List[str]]):
    instructions = lines[0]
    atlas = {}

    for line in lines[2:]:
        key, value = map(lambda x: x.strip(), line.split(' = '))
        atlas[key] = value[1:-1].split(', ')
    return instructions, atlas


def walk_atlas(instructions: str, atlas: Dict[str, List[str]]) -> int:
    current = 'AAA'
    steps = 0
    next = 0
    while current != 'ZZZ':
        steps += 1
        instruction = instructions[next % len(instructions)]
        if instruction == 'L':
            current = atlas[current][0]
        elif instruction == 'R':
            current = atlas[current][1]
        next += 1
    return steps


def part_one(path: str) -> int:
    lines = parse_lines(path)
    instructions, atlas = parse_directions_and_map(lines)
    return walk_atlas(instructions, atlas)


def part_two(path: str) -> int:
    return 0
