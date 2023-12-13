import datetime
from typing import Dict, List, Iterable, Tuple
from task_input import task_input
from multiprocessing import Process

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


def convert_number(initial_number: int,
                   rules: List[List[int]]) -> int:
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


def parse_seed_ranges_p2(seeds: Iterable[int]) -> List[Tuple[int, int]]:
    parsed_seeds = [seed for seed in seeds]
    seed_range_lower_bound = parsed_seeds[::2]
    seed_range_upper_bound = [sum(x) for x in zip(parsed_seeds[::2], parsed_seeds[1::2])]
    seed_ranges = zip(seed_range_lower_bound, seed_range_upper_bound)
    return list(seed_ranges)


def get_min_location_number(seeds: Iterable[int],
                            rules: Dict[str, List[List[int]]]) -> int:
    loc_values = []
    for seed in seeds:
        number = seed
        for map_ in maps:
            number = convert_number(initial_number=number,
                                    rules=rules.get(map_, []))
        loc_values.append(number)
    return min(loc_values)


def get_seed_value(seed_range: Tuple[int, int]) -> Iterable[int]:
    low, high = seed_range
    for seed_val in range(low, high):
        yield seed_val


def get_min_location_number_mp_p2(seed_range: Tuple[int, int],
                                  rules: Dict[str, List[List[int]]],
                                  ) -> int:
    start = datetime.datetime.now()
    print("start time", start)
    low, high = seed_range
    min_loc_val = None
    for seed_num in range(low, high):
        number = seed_num
        for map_ in maps:
            number = convert_number(initial_number=number, rules=rules.get(map_, []))
        if min_loc_val is None or number < min_loc_val:
            min_loc_val = number
    print(min_loc_val)
    end = datetime.datetime.now()
    print("duration", end - start)
    return min_loc_val


def mp_starter(seed_ranges: List[Tuple[int, int]], rules: Dict[str, List[List[int]]]) -> None:
    processes = []

    for seed_range in seed_ranges:
        process = Process(target=get_min_location_number_mp_p2, args=(seed_range, rules))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()


def convert_location_to_destination(loc_num: int, rules: List[List[int]]) -> int:
    # result = 0
    for destination, source, range_len in rules:
        if loc_num in range(destination, destination + range_len):
            result = loc_num - (destination - source)
            return result
    return loc_num


def main() -> None:
    rules = parse_mapping_data(data=task_input)
    seeds = parse_seeds(data=task_input)
    seed_ranges = parse_seed_ranges_p2(seeds=seeds)

    for num in range(1000000000):
        if num % 1000000 == 0:
            print(num/1000000)
        nex_min_src = num
        for map_ in maps[::-1]:
            nex_min_src = convert_location_to_destination(nex_min_src, rules.get(map_, []))

        for l, u in seed_ranges:
            if nex_min_src not in range(l,u):
                continue
            else:
                print(num)
                raise SystemExit("aaa")

        # for low, high in seed_ranges:
        #     if nex_min_src not in range(low, high):
        #         print("found seed", nex_min_src)
        #         break

    # print(min(potential_seeds))


if __name__ == "__main__":
    main()
    # p2 answer 56931769.
