from typing import Tuple, Dict, List, Iterable

sample_data = """seeds: 79 14 55 13
seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

maps = ("seed-to-soil",
        "soil-to-fertilizer",
        "fertilizer-to-water",
        "water-to-light",
        "light-to-temperature",
        "temperature-to-humidity",
        "humidity-to-location",
        )


def parse_mapping_data(data: str) -> Dict[str, List[List[int]]]:
    result = {}
    name = ""
    for line in data.splitlines():
        if not name and line.endswith("map:"):
            name, _ = line.split(" ")
            # validate name
            if name not in maps:
                raise Exception(f"unknown conversion received: {name}")
            continue

        if not line and name:
            name = ""

        if line and name:
            rules = result.get(name, [])
            rules.append([int(num) for num in line.split(" ")])
            result[name] = rules

    return result


def convert_number(initial_number: int, rules: List[List[int]]) -> int:
    result = 0

    for destination, source, range_len in rules:
        if initial_number in range(source, source + range_len):
            result = initial_number + (destination - source)
            return result
        result = initial_number

    return result


def parse_seeds(data: str) -> Iterable[int]:
    for line in data.splitlines():
        if line.startswith("seeds:"):
            _, seeds = line.split(": ")
            for seed in seeds.split(" "):
                yield int(seed)


def get_min_location_number(seeds: Iterable[int], rules: Dict[str, List[List[int]]]) -> int:
    loc_values = []
    for seed in seeds:
        number = seed
        for map_ in maps:
            number = convert_number(initial_number=number, rules=rules.get(map_, []))
        loc_values.append(number)
    return min(loc_values)


def main() -> None:
    rules = parse_mapping_data(sample_data)
    seeds = parse_seeds(data=sample_data)
    print(get_min_location_number(seeds=seeds, rules=rules))


if __name__ == "__main__":
    main()
