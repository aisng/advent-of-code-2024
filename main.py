from typing import Tuple, Dict, List

seeds = "79 14 55 13"

sample_data = """seed-to-soil map:
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

maps = ("seed-to-soil"
        "soil-to-fertilizer"
        "fertilizer-to-water"
        "water-to-light"
        "light-to-temperature"
        "temperature-to-humidity"
        "humidity-to-location"
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

    # current_mapping_rules = []
    # current_mapping_start_idx = data.index(mapping_type) + 1
    # for line in data[current_mapping_start_idx:]:
    #     if line:
    #         current_mapping_rules.append(line)
    #     else:
    #         break
    #
    # print("cmr", current_mapping_rules)


def convert_number(seed_number: int, rules: List[List[int]]) -> int:
    print(rules)
    result = 0
    source_ranges = []
    destination_ranges = []
    for rule in rules:
        source_lower = rule[1]
        source_upper = rule[1] + rule[2]
        range_length = rule[2]
        source_range = (source_lower, source_upper)
        destination_lower = rule[0]
        destination_upper = rule[0] + range_length
        destination_range = (destination_lower, destination_upper)
        # if seed_number in source_range:
        #     result = destination_upper - range_length
        source_ranges.append(source_range)
        destination_ranges.append(destination_range)
    # 79-50+52
    print("src", source_ranges, )
    print("dest", destination_ranges )

    return result


def get_seeds():
    return []


def main() -> None:
    rules = parse_mapping_data(sample_data)
    print(convert_number(seed_number=79, rules=rules["seed-to-soil"]))
    # for seed in get_seeds():
    #     number = seed
    #     for map_ in maps:
    #         number = convert_number(number, rules.get(map_, []))
    #     print(f"loc: {number}")  # todo store and get min loc


if __name__ == "__main__":
    main()
