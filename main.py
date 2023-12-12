import datetime
import threading
import queue
from typing import Dict, List, Iterable, Tuple
from task_input import task_input

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


def parse_seeds_p1(data: str) -> Iterable[int]:
    for line in data.splitlines():
        if line.startswith("seeds:"):
            _, seeds = line.split(": ")
            for seed in seeds.split(" "):
                yield int(seed)


# not used in multithreading
def get_seed_value_from_range_p2(seeds: Iterable[int]) -> Iterable[int]:
    parsed_seeds = [seed for seed in seeds]
    seed_range_lower_bound = parsed_seeds[::2]
    seed_range_upper_bound = [sum(x) for x in zip(parsed_seeds[::2], parsed_seeds[1::2])]
    seed_ranges = zip(seed_range_lower_bound, seed_range_upper_bound)
    for lower_bound, upper_bound in seed_ranges:
        print("lower bound", lower_bound, datetime.datetime.now())
        for seed in range(lower_bound, upper_bound):
            yield seed


def parse_seed_ranges_p2(seeds: Iterable[int]) -> List[Tuple[int, int]]:
    parsed_seeds = [seed for seed in seeds]
    seed_range_lower_bound = parsed_seeds[::2]
    seed_range_upper_bound = [sum(x) for x in zip(parsed_seeds[::2], parsed_seeds[1::2])]
    seed_ranges = zip(seed_range_lower_bound, seed_range_upper_bound)
    return list(seed_ranges)
    # for lower_bound, upper_bound in seed_ranges:
    #     print("lower bound", lower_bound, datetime.datetime.now())
    #     for seed in range(lower_bound, upper_bound):
    #         yield seed


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


def get_min_location_number_p2(seeds: Iterable[int], rules: Dict[str, List[List[int]]]) -> int:
    min_loc_val = None
    for seed_num in get_seed_value_from_range_p2(seeds):
        number = seed_num
        for map_ in maps:
            number = convert_number(initial_number=number, rules=rules.get(map_, []))
        if min_loc_val is None or number < min_loc_val:
            min_loc_val = number
    return min_loc_val


def get_min_location_number_mt_p2(seed_range: Tuple[int, int],
                                  rules: Dict[str, List[List[int]]],
                                  queue_: queue.Queue) -> int:
    start = datetime.datetime.now()
    print("start time", start)
    low, high = seed_range
    # print("low", low, datetime.datetime.now())
    min_loc_val = None
    for seed_num in range(low, high):
        number = seed_num
        for map_ in maps:
            number = convert_number(initial_number=number, rules=rules.get(map_, []))
        if min_loc_val is None or number < min_loc_val:
            min_loc_val = number
    queue_.put(min_loc_val)
    print(min_loc_val)
    end = datetime.datetime.now()
    print("duration", end - start)
    return min_loc_val


def main() -> None:
    rules = parse_mapping_data(data=task_input)
    seeds_p1 = parse_seeds_p1(data=task_input)
    seed_ranges = parse_seed_ranges_p2(seeds=seeds_p1)
    threads = []
    thread_returns = []
    queue_ = queue.Queue()

    for seed_range in seed_ranges:
        thread = threading.Thread(target=get_min_location_number_mt_p2, args=(seed_range, rules, queue_))
        # return_val = queue_.get()
        # thread_returns.append(return_val)
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    while not queue_.empty():
        thread_returns.append(queue_.get())

    if thread_returns:
        print("thread returns", thread_returns)
        print("result", min(thread_returns))


if __name__ == "__main__":
    main()
    # 4225564962 too high
