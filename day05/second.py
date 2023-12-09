with open("data", "r") as file_handle:
    lines = file_handle.read()

def parse_input(lines):
    lines = lines.split("\n")
    initial_seeds = lines[0].split(": ")[1].strip().split(" ")
    initial_seeds = [int(seed) for seed in initial_seeds]

    lines = "\n".join(lines[2:])

    maps = {}
    map_name = ""
    for map_section in lines.split("\n\n"):
        for line in map_section.splitlines():
            if line.endswith(":"):
                map_name = line[:-5]
                maps[map_name] = []
            else:
                destination_start, source_start, range_length = map(int, line.split(" "))
                values = {"source_start": source_start, "source_end": source_start + range_length - 1, "difference": destination_start - source_start}
                maps[map_name].append(values)
    return initial_seeds, maps

def main():
    initial_seeds, maps = parse_input(lines)
    
    end = "location"
    current = "seed"
    minima_search = []
    min_location = float("inf")
    for seed_start in range(0, len(initial_seeds), 2):
        #Manual iterative approach to search for minima by changing gradually changing the step size
        seed_range = range(initial_seeds[seed_start], initial_seeds[seed_start] + initial_seeds[seed_start + 1],1)
        for seed in seed_range:
            initial_seed = seed
            while True:
                if current == end:
                    if seed < min_location:
                        min_location = seed
                        minima_search.append((initial_seed, seed))
                    current = "seed"
                    break
                map_name = [map_name for map_name in maps.keys() if map_name.startswith(current)][0]
                current = map_name.split("-to-")[1]

                for map_range in maps[map_name]:
                    if map_range["source_start"] <= seed <= map_range["source_end"]:
                        seed = seed + map_range["difference"]
                        break
    return sorted(minima_search, key=lambda x: x[1])


if __name__ == "__main__":
    print(main())
